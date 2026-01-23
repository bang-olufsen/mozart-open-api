"""Main Mozart CLI document."""

import argparse
import asyncio
import contextlib
import ipaddress
import logging
import pprint
import sys
import threading
from dataclasses import dataclass
from typing import Final, cast

from aioconsole import ainput
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

from mozart_api import __version__
from mozart_api.models import BeolinkJoinRequest, VolumeLevel, VolumeMute
from mozart_api.mozart_client import (
    MozartClient,
    WebSocketEventType,
    check_valid_serial_number,
)

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
    "allstandby",
]


@dataclass
class MozartDevice:
    """Dataclass for describing Zeroconf discovered Mozart devices."""

    friendly_name: str | None = ""
    model_name: str = ""
    serial_number: str = ""
    ip_address: str = ""
    sw_version: str = ""

    def __str__(self) -> str:
        """Format for easier viewing."""
        return f"""
friendly_name: {self.friendly_name}
model_name: {self.model_name}
serial_number: {self.serial_number}
ip_address: {self.ip_address}
sw_version: {self.sw_version}
"""


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629."""

    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    reset = "\x1b[0m"

    def __init__(self) -> None:
        """Initialize custom logger."""
        super().__init__()
        fmt = "%(asctime)s - %(message)s"

        # The levels are used for color coding
        self.FORMATS = {
            logging.DEBUG: self.blue + fmt + self.reset,
            logging.INFO: self.green + fmt + self.reset,
            logging.WARNING: self.yellow + fmt + self.reset,
            logging.ERROR: fmt,
            logging.CRITICAL: self.red + fmt + self.reset,
        }

    def format(self, record: logging.LogRecord) -> str:
        """Format log message."""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomLogger(logging.Logger):
    """Custom logger with color coding."""

    def __init__(self, name: str) -> None:
        """Init the logger."""
        super().__init__(name)
        self.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(CustomFormatter())

        self.addHandler(stream_handler)


mozart_devices: list[MozartDevice] = []

logger = CustomLogger(__name__)


class MozartListener(ServiceListener):
    """Listener for Zeroconf discovery of Mozart devices."""

    def __init__(self, mode: str, verbose: bool, event: threading.Event) -> None:
        """Initialize listener."""
        super().__init__()
        self._mode = mode
        self._verbose = verbose
        self._event = event

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Unused."""

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Unused."""

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        """Add discovered Mozart device."""
        info = zc.get_service_info(type_, name)

        # Sometimes service info is None.
        if not info:
            logger.info("Error getting %s", name)
            return

        # Create MozartDevice object from MDNS discovered information.
        ip_address = info.parsed_addresses()[0]
        serial_number = cast("bytes", info.properties.get(b"sn")).decode("utf-8")
        model_name = cast("str", info.server)[:-16].replace("-", " ")
        sw_version = cast("bytes", info.properties.get(b"fv")).decode("utf-8")

        friendly_name = info.properties.get(b"fn")

        mozart_device = MozartDevice(
            friendly_name.decode("utf-8") if friendly_name is not None else None,
            model_name,
            serial_number,
            ip_address,
            sw_version,
        )

        mozart_devices.append(mozart_device)

        # Stop discovery if the desired Mozart device has been found.
        if self._mode == serial_number:
            logger.error(
                "Desired Mozart device: %s found: %s", self._mode, mozart_device
            )
            self._event.set()

        # Only print the discovered devices if in 'discover' mode or verbose is enabled.
        elif self._mode == DISCOVER_MODE or self._verbose:
            logger.error("%s", mozart_device)


def discover_devices(mode: str, timeout: int, verbose: bool) -> list[MozartDevice]:
    """MDNS discovery of devices on the current network."""
    event = threading.Event()

    zeroconf = Zeroconf()
    listener = MozartListener(mode, verbose, event)
    browser = ServiceBrowser(zeroconf, MOZART_MDNS_TYPE, listener)

    if mode == "discover" or verbose:
        logger.error("Discovering Mozart devices. Scanning _bangolufsen._tcp.local.")

    if timeout == -1:
        with contextlib.suppress(KeyboardInterrupt):
            input("Press the 'enter' key to stop discovery.\n\r")
    else:
        # Stop if the serial number has been found with MDNS
        timeout_status = event.wait(timeout)

        if not timeout_status:
            logger.error("Discovery timed out with timeout of %s seconds.", timeout)

    browser.cancel()
    zeroconf.close()

    return mozart_devices


def parse_mode(mode: str) -> str:
    """Parse mode input."""
    # Check for valid mode, serial number or IP address
    if (
        mode in (DISCOVER_MODE, VERSION_MODE)
        or check_valid_serial_number(mode)
        or ipaddress.ip_address(mode)
    ):
        return mode
    raise argparse.ArgumentTypeError


def init_argument_parser() -> argparse.ArgumentParser:
    """Initialize  and add arguments."""
    parser = argparse.ArgumentParser(
        prog="mozart_api",
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
        type=parse_mode,
        help=f"""Specify the serial number or IP address for command execution
                ,'{DISCOVER_MODE}' for Zeroconf discovery of Mozart devices or "{VERSION_MODE}" to get the API client version.""",
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
        self._timeout = MDNS_TIMEOUT
        self._verbose = False
        self._websocket = False
        self._mode = ""
        self._command = ""
        self._host = ""
        self._command_args: list[str] = []
        self._mozart_devices: list[MozartDevice] = []

        parser = init_argument_parser()
        args = parser.parse_args()

        if args.timeout:
            self._timeout = int(args.timeout)

        self._verbose = bool(args.verbose)
        self._websocket = bool(args.websocket)
        self._mode = args.mode
        self._command = args.command
        self._command_args = args.command_args

        # Check if the API version should be printed
        if self._mode == VERSION_MODE:
            logger.error("%s", __version__)
            sys.exit(0)

        # Check if the mode defined is an ip address
        with contextlib.suppress(ValueError):
            ipaddress.ip_address(self._mode)
            self._host = self._mode

        # Discover devices if host has not been defined
        if not self._host:
            self._mozart_devices = discover_devices(
                self._mode,
                self._timeout,
                self._verbose,
            )

            # Get the ip address from the devices Mozart devices
            self._host = next(
                (
                    device
                    for device in self._mozart_devices
                    if device.serial_number == self._mode
                ),
                MozartDevice(),
            ).ip_address

        # Exit if in discover mode, no command has been defined
        # or desired host can't be found.
        if self._mode == DISCOVER_MODE or self._command == "" or self._host == "":
            sys.exit(0)

        asyncio.run(self._run_api())

        sys.exit(0)

    async def _run_api(self) -> None:
        """Run async API command handling."""
        # Generate MozartApi object for calling API endpoints.
        self.mozart_client = MozartClient(self._host)

        # Connect to the websocket notification channel if defined
        if self._websocket:
            logger.error("Connecting to WebSocket channel")
            self.mozart_client.get_all_notifications(self.all_notifications)
            self.mozart_client.get_on_connection(self.on_connection)
            self.mozart_client.get_on_connection_lost(self.on_connection_lost)
            await self.mozart_client.connect_notifications(
                remote_control=True, reconnect=True
            )

        # Handle command
        await self._command_handler()

        # If WebSocket listener is enabled,
        # then wait for keypress before exiting the CLI
        if self._websocket:
            with contextlib.suppress(KeyboardInterrupt):
                await ainput(
                    "Listening to WebSocket events. Press the 'enter' key to exit CLI.\n\r"
                )
            self.mozart_client.disconnect_notifications()

        await self.mozart_client.close_api_client()

    async def _beolink_join(self) -> BeolinkJoinRequest | None:
        """Showcase async API usage of the Beolink command."""
        # If no JID is specified, then join an active experience if available
        if len(self._command_args) == 0:
            status = await self.mozart_client.join_latest_beolink_experience()

        else:
            serial_number = self._command_args[0]

            # Check if a device with specified serial number
            # is available as a peer and get JID if available
            peers = await self.mozart_client.get_beolink_peers()

            # The peers may be outdated and still have now unavailable devices.
            if len(peers) == 0:
                logger.error("No available Beolink peers.")
                return None

            jid = next(peer for peer in peers if serial_number in peer.jid).jid

            status = await self.mozart_client.join_beolink_peer(jid=jid)

        return status

    def all_notifications(
        self,
        notification: WebSocketEventType,
        _: str,
    ) -> None:
        """Handle all notifications."""
        logger.debug("WebSocket:\n\r%s", pprint.pformat(notification))

    def on_connection(self) -> None:
        """Handle connection made."""
        logger.error("WebSocket connection established.")

    def on_connection_lost(self) -> None:
        """Handle connection lost."""
        logger.warning(
            "WebSocket connection lost. Attempting to reconnect to %s...", self._host
        )

    async def _command_handler(self) -> None:
        """Handle commands."""
        logger.error(
            "Sending command: '%s' to device with args %s.",
            self._command,
            self._command_args,
        )
        status = None

        if self._command == "preset":
            preset_id = int(self._command_args[0])
            await self.mozart_client.activate_preset(id=preset_id)

        elif self._command in ("play", "pause", "next", "previous"):
            await self.mozart_client.post_playback_command(command=self._command)

        elif self._command == "mute":
            await self.mozart_client.set_volume_mute(volume_mute=VolumeMute(muted=True))

        elif self._command == "unmute":
            await self.mozart_client.set_volume_mute(
                volume_mute=VolumeMute(muted=False),
            )

        elif self._command == "volume":
            volume_level = int(self._command_args[0])
            await self.mozart_client.set_current_volume_level(
                volume_level=VolumeLevel(level=volume_level),
            )

        elif self._command == "join":
            status = await self._beolink_join()

        # Currently show battery state, product state
        elif self._command == "info":
            battery_state = await self.mozart_client.get_battery_state()
            logger.info(
                "Info - battery state:\n\r%s",
                pprint.pformat(battery_state.model_dump()),
            )

            power_state = await self.mozart_client.get_product_state()
            logger.info(
                "Info - product state:\n\r%s", pprint.pformat(power_state.model_dump())
            )

        elif self._command == "allstandby":
            await self.mozart_client.post_beolink_allstandby()

        else:
            logger.error("Invalid command %s.", self._command)
            return

        # Print verbose status information if defined.
        if self._verbose and self._command == "join":
            # Wait for the join-result to be available
            await asyncio.sleep(1)
            if status:
                join_result = await self.mozart_client.get_beolink_join_result(
                    id=status.request_id
                )
                logger.info(
                    "Beolink Join status: %s", pprint.pformat(join_result.model_dump())
                )
