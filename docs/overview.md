The Python package has been generated using the [OpenAPI Generator](https:/openapi-generator.tech/). On top of the generated API, a helper file, mozart_client.py, has been made that makes the API more pythonic. We recommend using this.

Another file, mozart_cli.py, has been made for using the Mozart API in a simple CLI program. This has been set as the "entry point" for the Python package.

## Installation

The Mozart Open API can be installed with pip. For more information about required Python version, check the [PyPI page](https://pypi.org/project/mozart-api/).

Install using pip:

```terminal
pip3 install mozart-api
```

## API usage

To use the Python API:

- Create a MozartClient object
- Choose which (if any) WebSocket events to listen to
- Connect to the WebSocket notification channel (if needed)
- Use any of the endpoints

### Example

<!--
type: tab
title: Synchronous
-->

<!-- title: "Synchronous API usage example"
lineNumbers: true
-->

```python
from mozart_api.models import VolumeLevel
from mozart_api.mozart_client import MozartClient


def all_notifications(notification):
    """Notification handler."""
    print(notification)

# Setup API and WebSocket listener
mozart_client = MozartClient(host="192.168.0.1")
mozart_client.get_all_notifications(all_notifications)

# Connect to the WebSocket notification channel
mozart_client.connect_notifications(remote_control=True)

# Run commands
mozart_client.set_current_volume_level(volume_level=VolumeLevel(level=50))
mozart_client.activate_preset(id=2)
mozart_client.post_beolink_expand(jid="1234.1234567.12345678@products.bang-olufsen.com")

listeners = mozart_client.get_beolink_listeners()
print(listeners)
```

<!--
type: tab
title: Asynchronous
-->

<!-- title: "Asynchronous API usage example"
lineNumbers: true
-->

```python
from mozart_api.models import VolumeLevel
from mozart_api.mozart_client import MozartClient


def all_notifications(notification):
    """Notification handler."""
    print(notification)

# Setup API and WebSocket listener
mozart_client = MozartClient(host="192.168.0.1")
mozart_client.get_all_notifications(all_notifications)

# Connect to the WebSocket notification channel
mozart_client.connect_notifications(remote_control=True)

# Run commands
mozart_client.set_current_volume_level(volume_level=VolumeLevel(level=50), async_req=True)
mozart_client.activate_preset(id=2, async_req=True)
mozart_client.post_beolink_expand(jid="1234.1234567.12345678@products.bang-olufsen.com", async_req=True)

listeners = mozart_client.get_beolink_listeners(async_req=True).get()
print(listeners)
```

<!-- type: tab-end -->

Where `192.168.0.1` is a Mozart device's IP-address.

### Beware
<!-- TODO: replace link with Github pages URL-->

Some of the classes defined in the Mozart API are aliases to other data types, for example: [ActionList](http://127.0.0.1:3000/docs/index.html#/schemas/ActionList) is an array of [Action](http://127.0.0.1:3000/docs/index.html#/schemas/Action) objects. These classes are not generated and can therefore not be used in the Python API. instead, use the built in Python data types, for example when defining an ActionList, simply use a `list` instead.

## Example CLI program

The CLI program carries out one command and then exits afterwards. The program needs to do a device-discovery on each command, which in noisy environments could take some time. If speed is important, an IP-address can be used instead.

Additionally since the CLI uses MDNS for device discovery, port number 5353 needs to be open.

### Usage example

This example shows device discovery and afterwards joining a Beolink session with WebSocket events being printed.

![example gif](/docs/discovery_join.gif)

### Device discovery

<!--
type: tab
title: Discover
-->

#### discover

Discover Mozart devices on the network.

```terminal
mozart_api discover
```

<!--
type: tab
title: Serial number
-->

#### serial number

Ensure that the serial number is reachable on the network.

```terminal
mozart_api 12345678
```

<!-- type: tab-end -->

### Options

<!--
type: tab
title: Verbose
-->

#### verbose

Add as option to add verbose output.

```terminal
mozart_api serial_number command command_args -v

mozart_api serial_number command command_args --verbose
```

<!--
type: tab
title: Timeout
-->

#### timeout

Add as option with parameter to modify MDNS discovery timeout.

Optionally use '-1' to have a user-interrupted device discovery:

```terminal
mozart_api serial_number command command_args -t 20

mozart_api serial_number command command_args --timeout 20

mozart_api serial_number command command_args --timeout -1
```

<!--
type: tab
title: WebSocket
-->

#### websocket

Add as option to show WebSocket notifications before and after command execution.

Upon connection the overall state of the device will be immediately transferred.

```terminal
mozart_api serial_number command command_args -w

mozart_api serial_number command command_args --websocket
```

<!-- type: tab-end -->

### Commands

<!--
type: tab
title: Playback
-->

#### preset

Will activate the _preset_ command.

```terminal
mozart_api 12345678 preset 1
```

#### play

Will activate the _play_ playback command.

```terminal
mozart_api 12345678 play
```

#### pause

Will activate the _pause_ playback command.

```terminal
mozart_api 12345678 pause
```

#### next

Will activate the _next_ playback command.

```terminal
mozart_api 12345678 next
```

#### previous

Will activate the _previous_ playback command.

```terminal
mozart_api 12345678 previous
```

<!--
type: tab
title: Volume
-->

#### mute

Will activate the mute command.

```terminal
mozart_api 12345678 mute
```

#### unmute

Will activate the unmute command.

```terminal
mozart_api 12345678 unmute
```

#### volume

Will activate the modify volume level command on the device (0-100).

```terminal
mozart_api 12345678 volume 50
```

<!--
type: tab
title: Beolink
-->

#### join

Will join a Beolink experience if available or will join a specific Beolink experience if available.

```terminal
mozart_api 12345678 join

mozart_api 12345678 join 23456789
```

#### allstandby

Will set all connected Beolink devices to networkStandby.

```terminal
mozart_api 12345678 allstandby
```

<!--
type: tab
title: Miscellaneous
-->

#### info

Will print device information.

```terminal
mozart_api 12345678 info
```

<!-- type: tab-end -->