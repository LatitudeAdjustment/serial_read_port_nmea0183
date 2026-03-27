# README.md

Claude-created Python application to read and output serial NMEA 0183 data.

Data was collected from GlobalSat BU-353S4 via USB port.

## Configuration

The port configuration is hard-coded in the Python file:

```Python
        ser = serial.Serial(                         
            port=port,
            baudrate=4800,                                 
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ON,
            timeout=1                           
        )   
```

## References

<https://en.wikipedia.org/wiki/NMEA_0183>

Additional information at ~/Documents/BU-353S4.

## Show Ports

```bash
$ ls /dev/tty.*
/dev/tty.Bluetooth-Incoming-Port /dev/tty.SoundcoreSpaceA40
/dev/tty.debug-console   /dev/tty.usbserial-1110
```

```bash
$ ls -l /dev/tty.*
crw-rw-rw-  1 root  wheel  0x9000004 Dec  4 10:05 /dev/tty.Bluetooth-Incoming-Port
crw-rw-rw-  1 root  wheel  0x9000000 Dec  4 10:03 /dev/tty.debug-console
crw-rw-rw-  1 root  wheel  0x9000002 Dec  4 10:05 /dev/tty.SoundcoreSpaceA40
crw-rw-rw-  1 root  wheel  0x900001c Mar 23 12:26 /dev/tty.usbserial-1110
```

## Run Program

```bash
python serial_read_port_nmea0183.py /dev/tty.usbserial-XXXX
```

```bash
python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
```

### Import Issue

```bash
$ python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
  File "serial_read_port_nmea0183.py", line 16
    print(f"Listening on {port} at 4800 baud... (Ctrl+C to quit)")                                                
                                                                ^
SyntaxError: invalid syntax
```

A virtual environment is required.
Set up the virtual environment as follows (done previously):

```bash
$ python3 -m venv ~/serial-venv
$ source ~/serial-venv/bin/activate
$ pip install pyserial
Requirement already satisfied: pyserial in /Users/username/serial-venv/lib/python3.14/site-packages (3.5)

[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
$ python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
Listening on /dev/tty.usbserial-1110 at 4800 baud... (Ctrl+C to quit)
kc���c��F��
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPGSV,3,1,12,01,00,000,,02,00,000,,03,00,000,,04,00,000,*7C
$GPGSV,3,2,12,05,00,000,,06,00,000,,07,00,000,,08,00,000,*77
$GPGSV,3,3,12,09,00,000,,10,00,000,,11,00,000,,12,00,000,*71
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPGSV,3,1,12,01,00,000,,02,00,000,,03,00,000,,04,00,000,*7C
$GPGSV,3,2,12,05,00,000,,06,00,000,,07,00,000,,08,00,000,*77
$GPGSV,3,3,12,09,00,000,,10,00,000,,11,00,000,,12,00,000,*71
$GPRMC,,V,,,,,,,,,,N*53
^C
Stopped.
```

### Subsequent Execution

```bash
$ source ~/serial-venv/bin/activate
$ python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
Listening on /dev/tty.usbserial-1110 at 4800 baud... (Ctrl+C to quit)
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPRMC,,V,,,,,,,,,,N*53
$GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48
$GPGSA,M,1,,,,,,,,,,,,,,,*12
$GPGSV,3,1,12,05,00,000,14,12,00,000,14,15,00,000,18,23,00,000,18*7B
$GPGSV,3,2,12,26,00,000,17,01,00,000,,02,00,000,,03,00,000,*79
$GPGSV,3,3,12,04,00,000,,06,00,000,,07,00,000,,08,00,000,*77
^C
Stopped.
```

### Pipe to File

```bash
python serial_read_port_nmea0183.py /dev/tty.usbserial-1110 > BU-353S4_Output_001.log
```

## Stop Program

Entry Ctrl-z to stop the program:

```bash
$GPRMC,161008.000,A,4104.4935,N,07326.7605,W,0.17,281.20,270326,,,A*71
$GPGGA,161009.000,4104.4934,N,07326.7607,W,1,08,2.4,19.7,M,-34.3,M,,0000*54
^Z
[1]+  Stopped                 python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
```
