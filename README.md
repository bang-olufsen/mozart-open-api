# Mozart Open API

The Mozart API is a auto-generated REST API with async capabilities and WebSocket notification channel for immediate state information.

## Installation

The Mozart Open API can be installed with pip. For more information about required Python version, check the [PyPI page](https://pypi.org/project/mozart-api/).

Install using pip:

```terminal
pip3 install mozart-api
```

## Example CLI program

The CLI program carries out one command and then exits afterwards. This and the fact that the serial number is used to specify devices sometimes results in slow MDNS discovery times.

### Usage example

![example gif](demo.gif)

### Device discovery

<!--
type: tab
title: Discover
-->

#### discover

Discover Mozart devices on the network.

```terminal
python3 mozart_cli.py discover
```

<!--
type: tab
title: Serial number
-->

#### serial number

Ensure that the serial number is reachable on the network.

```terminal
python3 mozart_cli.py 12345678
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
python3 mozart_cli.py serial_number command command_args -v

python3 mozart_cli.py serial_number command command_args --verbose
```

<!--
type: tab
title: Timeout
-->

#### timeout

Add as option with parameter to modify MDNS discovery timeout.

Optionally use '-1' to have a user-interrupted device discovery:

```terminal
python3 mozart_cli.py serial_number command command_args -t 20

python3 mozart_cli.py serial_number command command_args --timeout 20

python3 mozart_cli.py serial_number command command_args --timeout -1
```

<!--
type: tab
title: WebSocket
-->

#### websocket

Add as option to show websocket notifications before and after command execution.

Upon connection the overall state of the device will be immediately transferred.

```terminal
python3 mozart_cli.py serial_number command command_args -w

python3 mozart_cli.py serial_number command command_args --websocket
```

<!--
type: tab
title: Remote
-->

#### remote

Add as option to show remote control websocket notifications.

```terminal
python3 mozart_cli.py serial_number command command_args -r

python3 mozart_cli.py serial_number command command_args --remote
```

<!-- type: tab-end -->

### Commands

<!--
type: tab
title: Preset
-->

#### preset

Will activate the _preset_ command.

```terminal
python3 mozart_cli.py 12345678 preset 1
```

<!--
type: tab
title: Play
-->

#### play

Will activate the _play_ playback command.

```terminal
python3 mozart_cli.py 12345678 play
```

<!--
type: tab
title: Pause
-->

#### pause

Will activate the _pause_ playback command.

```terminal
python3 mozart_cli.py 12345678 pause
```

<!--
type: tab
title: Next
-->

#### next

Will activate the _next_ playback command.

```terminal
python3 mozart_cli.py 12345678 next
```

<!--
type: tab
title: Previous
-->

#### previous

Will activate the _previous_ playback command.

```terminal
python3 mozart_cli.py 12345678 previous
```

<!--
type: tab
title: Mute
-->

#### mute

Will activate the mute command.

```terminal
python3 mozart_cli.py 12345678 mute
```

<!--
type: tab
title: Unmute
-->

#### unmute

Will activate the unmute command.

```terminal
python3 mozart_cli.py 12345678 unmute
```

<!--
type: tab
title: Volume
-->

#### volume

Will activate the modify volume level command on the device (0-100).

```terminal
python3 mozart_cli.py 12345678 volume 50
```

<!--
type: tab
title: Join
-->

#### join

Will join a Beolink experience if available or will join a specific Beolink experience if available.

```terminal
python3 mozart_cli.py 12345678 join

python3 mozart_cli.py 12345678 join 23456789
```

<!--
type: tab
title: Reset
-->

#### reset

Will factory reset a Mozart device.

```terminal
python3 mozart_cli.py 12345678 reset
```

<!--
type: tab
title: Info
-->

#### info

Will print device information.

```terminal
python3 mozart_cli.py 12345678 info
```

<!--
type: tab
title: Standby
-->

#### standby

Will set a Mozart device to networkStandby.

```terminal
python3 mozart_cli.py 12345678 standby
```

<!--
type: tab
title: Allstandby
-->

#### allstandby

Will set all connected Beolink devices to networkStandby.

```terminal
python3 mozart_cli.py 12345678 allstandby
```

<!-- type: tab-end -->
