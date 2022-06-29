# Mozart Open API

The Mozart API is a auto-generated REST API with async capabilities and WebSocket notification channel for immediate state information.

## Installation

The Mozart Open API can be installed with pip. For more information about required Python version, check the PyPI page.

Install using pip:

__NOT WORKING__

```terminal
pip3 install mozart-api
```

## Example CLI program

The CLI program carries out one command and then exits afterwards. This and the fact that the serial number is used to specify devices sometimes results in slow MDNS discovery times.

### verbose

Add as option to add verbose output.

```terminal
mozart_cli.py command command_args -v

mozart_cli.py command command_args --verbose
```

### timeout

Add as option with parameter to modify MDNS discovery timeout.

Optionally use '-1' to have a user-interrupted device discovery:

```terminal
mozart_cli.py command command_args -t 20

mozart_cli.py command command_args --timeout 20

mozart_cli.py command command_args --timeout -1
```

### websocket

Add as option to show websocket notifications before and after command execution.

Upon connection the overall state of the device will be immediately transferred.

```terminal
mozart_cli.py command command_args -w

mozart_cli.py command command_args --websocket
```

### remote

Add as option to show remote control websocket notifications.

```terminal
mozart_cli.py command command_args -r

mozart_cli.py command command_args --remote
```

### discover

Discover Mozart devices on the network.

```terminal
mozart_cli.py discover
```

### serial number

Ensure that the serial number is reachable on the network.

```terminal
mozart_cli.py 12345678
```

### preset

```terminal
mozart_cli.py 12345678 preset 1
```

Will activate preset 1

### play

```terminal
mozart_cli.py 12345678 play
```

Will activate the _play_ playback command.

### pause

```terminal
mozart_cli.py 12345678 pause
```

Will activate the _pause_ playback command.

### next

```terminal
mozart_cli.py 12345678 next
```

Will activate the _next_ playback command.

### previous

```terminal
mozart_cli.py 12345678 previous
```

Will activate the _previous_ playback command.

### mute

```terminal
mozart_cli.py 12345678 mute
```

Will mute the device.

### unmute

```terminal
mozart_cli.py 12345678 unmute
```

Will unmute the device.

### volume

```terminal
mozart_cli.py 12345678 volume 50
```

Will modify the volume level on the device (0-100).

### join

Will join a Beolink experience if available or will join a specific Beolink experience if available.

```terminal
mozart_cli.py 12345678 join

mozart_cli.py 12345678 join 23456789
```

### reset

```terminal
mozart_cli.py 12345678 reset
```

Will factory reset a Mozart device.

### info

```terminal
mozart_cli.py 12345678 info
```

Will print device information.

### standby

```terminal
mozart_cli.py 12345678 standby
```

Will set a Mozart device to networkStandby.

### allstandby

```terminal
mozart_cli.py 12345678 allstandby
```

Will set all connected Beolink devices to networkStandby.
