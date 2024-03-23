"""Main Mozart CLI document."""

# pylint: disable= too-few-public-methods too-many-instance-attributes

import argparse
import asyncio
import ipaddress
import re
import sys
import threading
from dataclasses import dataclass
from typing import Final, cast

from aioconsole import ainput  # type: ignore
from mozart_api import __version__ as MOZART_API_VERSION
from mozart_api.models import VolumeLevel, VolumeMute
from mozart_api.mozart_client import MozartClient
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

MOZART_MDNS_TYPE: Final[str] = "_bangolufsen._tcp.local."
MDNS_TIMEOUT: Final[int] = 10
DISCOVER_MODE: Final[str] = "discover"
VERSION_MODE: Final[str] = "version"

AVAILABLE_COMMANDS: Final[list[str]] = [
    "preset",
    "play",
    "pause",
    "next",
    "previous",
    "mute",
    "unmute",
    "volume",
    "join",
    "info",
    "standby",
    "allstandby",
    "timer",
]


@dataclass
class MozartDevice:
    """Dataclass for describing Zeroconf discovered Mozart devices."""

    friendly_name: str | None = ""
    model_name: str = ""
    serial_number: str = ""
    ip_address: str = ""
    sw_version: str = ""


mozart_devices: list[MozartDevice] = []


class MozartListener(ServiceListener):
    """Listener for Zeroconf discovery of Mozart devices."""

    def __init__(self, mode: str, verbose: bool, event: threading.Event) -> None:
        super().__init__()
        self.mode = mode
        self.verbose = verbose
        self.event = event

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Unused."""

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Unused."""

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Add discovered Mozart device."""

        info = zc.get_service_info(type_, name)

        # Sometimes service info is None.
        if not info:
            print(f"Error getting {name}")
            return

        # Create MozartDevice object from MDNS discovered information.
        ip_address = info.parsed_addresses()[0]
        serial_number = cast(bytes, info.properties.get(b"sn")).decode("utf-8")
        model_name = cast(str, info.server)[:-16].replace("-", " ")
        sw_version = cast(bytes, info.properties.get(b"fv")).decode("utf-8")

        friendly_name = info.properties.get(b"fn")

        # MDNS devices other than Mozart devices may not have friendly names
        if friendly_name is not None:
            friendly_name = cast(bytes, friendly_name).decode("utf-8")

        mozart_device = MozartDevice(
            friendly_name, model_name, serial_number, ip_address, sw_version
        )

        mozart_devices.append(mozart_device)

        # Stop discovery if the desired Mozart device has been found.
        if self.mode == serial_number:
            print(f"Desired Mozart device: {self.mode} found: {mozart_device}")
            self.event.set()

        # Only print the discovered devices if in 'discover' mode or verbose is enabled.
        elif self.mode == DISCOVER_MODE or self.verbose:
            print(mozart_device)


def discover_devices(mode: str, timeout: int, verbose: bool) -> list[MozartDevice]:
    """MDNS discovery of devices on the current network."""
    event = threading.Event()

    zeroconf = Zeroconf()
    listener = MozartListener(mode, verbose, event)
    browser = ServiceBrowser(zeroconf, MOZART_MDNS_TYPE, listener)

    if mode == "discover" or verbose:
        print("Discovering Mozart devices. Scanning _bangolufsen._tcp.local.")

    if timeout == -1:
        input("Press 'enter' to stop discovery.\n\r")

    else:
        # Stop if the serial number has been found with MDNS
        timeout_status = event.wait(timeout)

        if not timeout_status:
            print(f"Discovery timed out with timeout of {timeout} seconds.")

    browser.cancel()
    zeroconf.close()

    return mozart_devices


def init_argument_parser() -> argparse.ArgumentParser:
    """Initialize  and add arguments."""
    parser = argparse.ArgumentParser(
        prog="mozart-cli",
        description="CLI for sending simple commands to Mozart devices.",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Specify if the output should be verbose.",
    )

    parser.add_argument(
        "--websocket",
        "-w",
        action="store_true",
        help="Specify if the websocket listener should be active.",
    )

    parser.add_argument(
        "--timeout",
        "-t",
        action="store",
        help="""Specify Zeroconf discovery timeout.
                '-1' for input-interrupted discovery in 'discover' mode.""",
    )

    parser.add_argument(
        "mode",
        help="""Specify the serial number or IP address for command execution
                or 'discover' for Zeroconf discovery of Mozart devices.""",
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=AVAILABLE_COMMANDS,
        help="Specify the command.",
    )

    parser.add_argument(
        "command_args",
        nargs="*",
        help="Specify the command arguments if needed.",
    )
    return parser


class MozartApiCli:
    """Mozart CLI client."""

    def __init__(self) -> None:
        """Init the Mozart CLI."""
        self.timeout = MDNS_TIMEOUT
        self.verbose = False
        self.websocket = False
        self.mode = ""
        self.command = ""
        self.host = ""
        self.command_args: list[str] = []
        self.mozart_devices: list[MozartDevice] = []

        parser = init_argument_parser()
        args = parser.parse_args()

        if args.timeout:
            self.timeout = int(args.timeout)

        self.verbose = bool(args.verbose)
        self.websocket = bool(args.websocket)
        self.mode = args.mode
        self.command = args.command
        self.command_args = args.command_args

        # Check if the API version should be printed
        if self.mode == VERSION_MODE:
            print(MOZART_API_VERSION)
            sys.exit(0)

        # Check if the mode defined is an ip address
        try:
            ipaddress.ip_address(self.mode)
            self.host = self.mode
        except ValueError as exception:
            # Ensure that the mode's serial number has the correct format or 'discover' mode.
            if self.mode != DISCOVER_MODE and re.fullmatch(r"\d{8}", self.mode) is None:
                # Check if the mode is then an ip address
                raise ValueError(
                    f""""{self.mode}" has an invalid value. 
                    Must either be a serial number, ip address, "discover" or "version"."""
                ) from exception

        # Discover devices if host has not been defined
        if not self.host:
            self.mozart_devices = discover_devices(
                self.mode, self.timeout, self.verbose
            )

            # Get the ip address from the devices Mozart devices
            self.host = next(
                (
                    device
                    for device in self.mozart_devices
                    if device.serial_number == self.mode
                ),
                MozartDevice(),
            ).ip_address

        # Exit if in discover mode, no command has been defined or desired host can't be found.
        if self.mode == DISCOVER_MODE or self.command == "" or self.host == "":
            sys.exit(0)

        asyncio.run(self._run_api())

        sys.exit(0)

    async def _run_api(self):
        """Run async API command handling"""
        # Generate MozartApi object for calling API endpoints.
        self.mozart_client = MozartClient(self.host)

        # Connect to the websocket notification channel if defined
        if self.websocket:
            print("Connecting to WebSocket channel")
            self.mozart_client.get_all_notifications(self.all_notifications)
            await self.mozart_client.connect_notifications(remote_control=True)

        # Handle command
        await self._command_handler()

        # If websocket listener is enabled, then wait for keypress before exiting the CLI
        if self.websocket:
            await ainput(
                "Listening to WebSocket events. Press any key to exit CLI.\n\r"
            )
            self.mozart_client.disconnect_notifications()

        await self.mozart_client.close_api_client()

    async def _beolink_join(self):
        """Showcase async API usage of the Beolink command."""
        # If no JID is specified, then join an active experience if available
        if len(self.command_args) == 0:
            status = await self.mozart_client.join_latest_beolink_experience()

        else:
            serial_number = self.command_args[0]

            # Check if a device with specified serial number
            # is available as a peer and get JID if available
            peers = await self.mozart_client.get_beolink_peers()

            # The peers may be outdated and still have now unavailable devices.
            if len(peers) == 0:
                print("No available Beolink peers.")
                return

            jid = [peer for peer in peers if serial_number in peer.jid][0].jid

            status = await self.mozart_client.join_beolink_peer(jid=jid)

        return status

    def all_notifications(self, notification, notification_type):
        """Handle all notifications."""
        print(notification_type, notification)

    async def _command_handler(self):
        """Handle commands."""

        print(
            f"Sending command: '{self.command}' to device with args {self.command_args}."
        )
        status = None

        if self.command == "preset":
            preset_id = int(self.command_args[0])
            await self.mozart_client.activate_preset(id=preset_id)

        elif self.command in ("play", "pause", "next", "previous"):
            await self.mozart_client.post_playback_command(command=self.command)

        elif self.command == "mute":
            await self.mozart_client.set_volume_mute(volume_mute=VolumeMute(muted=True))

        elif self.command == "unmute":
            await self.mozart_client.set_volume_mute(
                volume_mute=VolumeMute(muted=False)
            )

        elif self.command == "volume":
            volume_level = int(self.command_args[0])
            await self.mozart_client.set_current_volume_level(
                volume_level=VolumeLevel(level=volume_level)
            )

        elif self.command == "join":
            status = await self._beolink_join()

        # Currently show battery state, product state
        elif self.command == "info":
            battery_state = await self.mozart_client.get_battery_state()
            print(f"Battery state: {battery_state}")

            power_state = await self.mozart_client.get_product_state()
            print(f"Product state: {power_state}")

        elif self.command == "allstandby":
            await self.mozart_client.post_beolink_allstandby()

        else:
            print(f"Invalid command {self.command}.")
            return

        # Print verbose status information if defined.
        if self.verbose and self.command == "join":
            # Wait for the join-result to be available
            await asyncio.sleep(1)
            print("Beolink Join status:")
            print(
                await self.mozart_client.get_beolink_join_result(id=status.request_id)
            )
