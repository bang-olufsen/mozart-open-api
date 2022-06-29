"""Main Mozart CLI document."""

import re
import time
from threading import Thread

from mozart_api.api.mozart_api import MozartApi
from mozart_api.models import (
    BeolinkJoinRequest,
    BeolinkPeer,
    PairedRemoteResponse,
    PowerStateEnum,
    VolumeLevel,
    VolumeMute,
)

from const import (
    DISCOVER_MODE,
    MDNS_TIMEOUT,
    MozartDevice,
    generate_mozart_api,
    init_argument_parser,
    valid_ip_address,
    websocket_listener,
)
from discovery import discover_devices


class MozartApiCli:
    """Mozart CLI client."""

    def __init__(self) -> None:
        """Init the Mozart CLI."""
        self.timeout: int = MDNS_TIMEOUT
        self.verbose: bool = False
        self.websocket: bool = False
        self.remote: bool = False
        self.mode: str = ""
        self.command: str = ""
        self.host: str = ""
        self.mozart_api: MozartApi = MozartApi()
        self.command_args: list[str] = []
        self.mozart_devices: list[MozartDevice] = []

        parser = init_argument_parser()
        args = parser.parse_args()

        if args.timeout:
            self.timeout = int(args.timeout)

        self.verbose = bool(args.verbose)
        self.websocket = bool(args.websocket)
        self.remote = bool(args.remote)
        self.mode = args.mode
        self.command = args.command
        self.command_args = args.command_args

        # Check if the mode defined is an ip address
        if valid_ip_address(self.mode):
            self.host = self.mode

        # Ensure that the mode's serial number has the correct format or 'discover' mode.
        elif self.mode != DISCOVER_MODE and re.fullmatch(r"\d{8}", self.mode) is None:
            # Check if the mode is then an ip address
            raise ValueError(
                f"'{self.mode}' has an invalid value. Must either be a serial number, ip address or 'discover'."
            )

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

        # Ensure that no commands are run in discover mode or no command has been defined.
        if self.mode == DISCOVER_MODE or self.command == "":
            return

        # If the desired device wasn't found then exit the CLI.
        if self.host == "":
            return

        # Generate MozartApi object for calling API endpoints.
        self.mozart_api = generate_mozart_api(self.host)

        # Connect to the websocket notification channel if defined
        if self.websocket:
            websocket_thread = Thread(
                target=websocket_listener, args=(f"ws://{self.host}:9339/",)
            )
            websocket_thread.daemon = True
            websocket_thread.start()

        # Connect to the remote control websocket notification channel if defined
        if self.remote:

            # Check if a remote control is available
            remote_list: PairedRemoteResponse = self.mozart_api.get_bluetooth_remotes()

            if len(remote_list.items) == 0:
                print("No available remotes paired.")

            else:
                remote_thread = Thread(
                    target=websocket_listener,
                    args=(f"ws://{self.host}:9339/remoteControl",),
                )
                remote_thread.daemon = True
                remote_thread.start()

        self._command_handler()

        # If websocket listener is enabled, then wait for keypress before exiting the CLI
        if (self.websocket or self.remote) and input("Press any key to exit CLI.\n\r"):
            return

    def _command_handler(self):
        """Handle commands."""

        print(
            f"Sending command: '{self.command}' to device. with args {self.command_args}"
        )

        if self.command == "preset":
            preset_id = int(self.command_args[0])
            self.mozart_api.activate_preset(id=preset_id)

        elif self.command in ("play", "pause", "next", "previous"):
            self.mozart_api.post_playback_command(command=self.command)

        elif self.command == "mute":
            self.mozart_api.set_volume_mute(volume_mute=VolumeMute(muted=True))

        elif self.command == "unmute":
            self.mozart_api.set_volume_mute(volume_mute=VolumeMute(muted=False))

        elif self.command == "volume":
            volume_level = int(self.command_args[0])
            self.mozart_api.set_current_volume_level(
                volume_level=VolumeLevel(level=volume_level)
            )

        elif self.command == "join":

            # If no JID is specified, then join an active experience if available
            if len(self.command_args) == 0:
                status: BeolinkJoinRequest = (
                    self.mozart_api.join_latest_beolink_experience()
                )

            else:
                serial_number = self.command_args[0]

                # Check if a device with specified serial number
                # is available as a peer and get JID if available
                peers: list[BeolinkPeer] = self.mozart_api.get_beolink_peers()

                # The peers may be outdated and still have now unavailable devices.
                if len(peers) == 0:
                    print("No available Beolink peers.")
                    return

                jid = [peer for peer in peers if serial_number in peer.jid][0].jid

                status: BeolinkJoinRequest = self.mozart_api.join_beolink_peer(jid=jid)

            if self.verbose:
                # Wait for the join-result to be available
                time.sleep(1)
                print("Beolink Join status:")
                print(self.mozart_api.get_beolink_join_result(id=status.request_id))

        elif self.command == "reset":
            status = self.mozart_api.post_factory_reset()

            if self.verbose:
                print(status)

        # Currently show playback metadata, product_info, battery state, power state, deezer state
        # product_info will not be a part of the initial public API
        elif self.command == "info":

            battery_state = self.mozart_api.get_battery_state()
            print(f"Battery state: {battery_state}")

            power_state = self.mozart_api.get_power_state()
            print(f"Power state: {power_state}")

            deezer_token_state = self.mozart_api.get_deezer_has_token()
            print(f"Deezer token state: {deezer_token_state}")

            playback_state = self.mozart_api.get_playback_state()
            print(f"Playback state: {playback_state}")

            product_info = self.mozart_api.get_product_info()
            print(f"Product info: {product_info}")

        elif self.command == "standby":
            self.mozart_api.set_power_state(
                power_state_enum=PowerStateEnum("networkStandby")
            )

        elif self.command == "allstandby":
            self.mozart_api.post_beolink_allstandby()


if __name__ == "__main__":
    MozartApiCli()
