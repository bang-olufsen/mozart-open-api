"""File for Mozart device discovery."""

import threading

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

from const import MOZART_MDNS_TYPE, MozartDevice

mozart_devices: list[MozartDevice] = []


class MozartListener(ServiceListener):
    """Listener for Zeroconf discovery of Mozart devices."""

    def __init__(self, mode: str, verbose: bool, event: threading.Event) -> None:
        super().__init__()
        self.mode = mode
        self.verbose = verbose
        self.event = event

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        # Unused
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        # Unused
        pass

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)

        # Create MozartDevice object from MDNS discovered information.
        friendly_name = info.properties.get(b"fn").decode("utf-8")
        model_name = info.server[:-16].replace("-", " ")
        serial_number = info.properties.get(b"sn").decode("utf-8")
        ip_address = info.parsed_addresses()[0]

        mozart_device = MozartDevice(
            friendly_name, model_name, serial_number, ip_address
        )

        mozart_devices.append(mozart_device)

        # Stop discovery if the desired Mozart device has been found.
        if self.mode == serial_number:
            print(f"Desired Mozart device: {self.mode} found: {mozart_device}")
            self.event.set()

        # Only print the discovered devices if in 'discover' mode or verbose is enabled.
        elif self.mode == "discover" or self.verbose:
            print(mozart_device)


def discover_devices(mode: str, timeout: int, verbose: bool) -> list[MozartDevice]:
    """MDNS discovery of devices on the current network."""
    event = threading.Event()

    zeroconf = Zeroconf()
    listener = MozartListener(mode, verbose, event)
    browser = ServiceBrowser(zeroconf, MOZART_MDNS_TYPE, listener)

    if mode == "discover" or verbose:
        print("Discovering Mozart devices.")

    if timeout == -1:
        input("Press enter to stop discovery.\n\r")

    else:
        # Stop if the serial number has been found with MDNS
        timeout_status = event.wait(timeout)

        if not timeout_status:
            print(f"Discovery timed out with timeout of {timeout} seconds.")
            return []

    browser.cancel()
    zeroconf.close()

    return mozart_devices
