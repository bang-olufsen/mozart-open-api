"""Constants for Mozart CLI."""

import argparse
from dataclasses import dataclass
from typing import Final

import websocket
from mozart_api.api.mozart_api import MozartApi
from mozart_api.api_client import ApiClient
from mozart_api.configuration import Configuration

MOZART_MDNS_TYPE: Final[str] = "_bangolufsen._tcp.local."
MDNS_TIMEOUT: Final[int] = 10
DISCOVER_MODE: Final[str] = "discover"


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
    "reset",
    "info",
    "standby",
    "reset",
    "allstandby",
]


@dataclass
class MozartDevice:
    """Dataclass for describing Zeroconf discovered Mozart devices."""

    friendly_name: str = ""
    model_name: str = ""
    serial_number: str = ""
    ip_address: str = ""


def generate_mozart_api(host: str) -> MozartApi:
    """Initialize the MozartApi object."""
    configuration = Configuration()
    configuration.host = host
    configuration.verify_ssl = False
    return MozartApi(ApiClient(configuration))


def websocket_listener(websocket_url: str) -> None:
    """Connect to the WebSocket notification channel."""
    websocket_object = websocket.WebSocket()
    websocket_object.connect(websocket_url)

    # While true for listening to notifications. Will be stopped when the CLI exits.
    while True:
        print(websocket_object.recv())


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
        "--remote",
        "-r",
        action="store_true",
        help="Specify if the remote control websocket listener should be active.",
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
        help="""Specify the serial number for command execution
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
