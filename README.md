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
```

### Subsequent Execution

```bash
$ python serial_read_port_nmea0183.py /dev/tty.usbserial-1110
Listening on /dev/tty.usbserial-1110 at 4800 baud... (Ctrl+C to quit)
7973,W,1,05,4.2,13.4,M,-34.3,M,,0000*56
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPRMC,191955.000,A,4104.4964,N,07326.7973,W,1.49,191.52,270326,,,A*78
$GPGGA,191956.000,4104.4965,N,07326.7959,W,1,05,4.2,13.2,M,-34.3,M,,0000*5A
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPRMC,191956.000,A,4104.4965,N,07326.7959,W,1.36,171.98,270326,,,A*72
$GPGGA,191957.000,4104.4971,N,07326.7951,W,1,05,4.2,12.9,M,-34.3,M,,0000*5C
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPRMC,191957.000,A,4104.4971,N,07326.7951,W,1.49,153.88,270326,,,A*77
$GPGGA,191958.000,4104.4976,N,07326.7941,W,1,05,4.2,12.7,M,-34.3,M,,0000*5B
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPGSV,3,1,12,06,70,015,13,19,64,092,13,17,37,109,14,21,25,197,20*7A
$GPGSV,3,2,12,22,18,169,15,51,31,225,,28,26,173,,09,18,099,*70
$GPGSV,3,3,12,04,14,067,,25,08,323,,03,07,036,,23,05,148,*7F
$GPRMC,191958.000,A,4104.4976,N,07326.7941,W,1.77,136.04,270326,,,A*74
$GPGGA,191959.000,4104.4982,N,07326.7939,W,1,05,4.2,12.3,M,-34.3,M,,0000*5A
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPRMC,191959.000,A,4104.4982,N,07326.7939,W,1.74,125.27,270326,,,A*71
$GPGGA,192000.000,4104.4985,N,07326.7944,W,1,05,4.2,12.3,M,-34.3,M,,0000*51
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.2,7.3*3B
$GPRMC,192000.000,A,4104.4985,N,07326.7944,W,1.22,121.09,270326,,,A*71
$GPGGA,192001.000,4104.4987,N,07326.7942,W,1,05,4.1,12.0,M,-34.3,M,,0000*54
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192001.000,A,4104.4987,N,07326.7942,W,1.12,121.09,270326,,,A*77
$GPGGA,192002.000,4104.4990,N,07326.7947,W,1,05,4.1,11.6,M,-34.3,M,,0000*51
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192002.000,A,4104.4990,N,07326.7947,W,0.71,121.09,270326,,,A*73
$GPGGA,192003.000,4104.4993,N,07326.7954,W,1,05,4.1,11.1,M,-34.3,M,,0000*56
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPGSV,3,1,12,06,70,015,13,19,64,092,13,17,37,109,15,21,25,197,20*7B
$GPGSV,3,2,12,22,18,169,15,51,31,225,,28,26,173,,09,18,099,*70
$GPGSV,3,3,12,04,14,067,,25,08,323,,03,07,036,,23,05,148,*7F
$GPRMC,192003.000,A,4104.4993,N,07326.7954,W,0.58,121.09,270326,,,A*78
$GPGGA,192004.000,4104.4994,N,07326.7960,W,1,05,4.1,10.7,M,-34.3,M,,0000*56
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192004.000,A,4104.4994,N,07326.7960,W,0.22,121.09,270326,,,A*72
$GPGGA,192005.000,4104.4992,N,07326.7962,W,1,05,4.1,10.3,M,-34.3,M,,0000*57
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192005.000,A,4104.4992,N,07326.7962,W,0.21,121.09,270326,,,A*74
$GPGGA,192006.000,4104.4991,N,07326.7972,W,1,05,4.1,10.2,M,-34.3,M,,0000*57
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192006.000,A,4104.4991,N,07326.7972,W,0.13,121.09,270326,,,A*74
$GPGGA,192007.000,4104.4987,N,07326.7979,W,1,05,4.1,9.9,M,-34.3,M,,0000*69
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192007.000,A,4104.4987,N,07326.7979,W,0.10,121.09,270326,,,A*7A
$GPGGA,192008.000,4104.4978,N,07326.7981,W,1,04,2.3,12.2,M,-34.3,M,,0000*55
$GPGSA,M,3,06,17,21,22,,,,,,,,,3.9,2.3,3.1*34
$GPGSV,3,1,12,06,70,015,13,17,37,109,15,21,25,197,20,22,18,169,14*7A
$GPGSV,3,2,12,19,64,092,10,51,31,225,,28,26,173,,09,18,099,*73
$GPGSV,3,3,12,04,14,067,,25,08,323,,03,07,036,,23,05,148,*7F
$GPRMC,192008.000,A,4104.4978,N,07326.7981,W,0.39,121.09,270326,,,A*79
$GPGGA,192009.000,4104.4973,N,07326.7981,W,1,04,2.3,12.9,M,-34.3,M,,0000*54
$GPGSA,M,3,06,17,21,22,,,,,,,,,3.9,2.3,3.1*34
$GPRMC,192009.000,A,4104.4973,N,07326.7981,W,0.16,121.09,270326,,,A*7E
$GPGGA,192010.000,4104.4969,N,07326.7988,W,1,05,4.1,12.8,M,-34.3,M,,0000*5A
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.4,4.1,7.3*38
$GPRMC,192010.000,A,4104.4969,N,07326.7988,W,0.61,121.09,270326,,,A*74
$GPGGA,192011.000,4104.4965,N,07326.7993,W,1,04,2.3,13.4,M,-34.3,M,,0000*55
$GPGSA,M,3,06,17,21,22,,,,,,,,,3.9,2.3,3.1*34
$GPRMC,192011.000,A,4104.4965,N,07326.7993,W,1.12,121.09,270326,,,A*76
$GPGGA,192012.000,4104.4961,N,07326.8000,W,1,05,4.1,13.3,M,-34.3,M,,0000*5C
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.3,4.1,7.3*3F
$GPRMC,192012.000,A,4104.4961,N,07326.8000,W,1.05,121.09,270326,,,A*7B
$GPGGA,192013.000,4104.4957,N,07326.8004,W,1,05,4.1,13.3,M,-34.3,M,,0000*5C
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.3,4.1,7.3*3F
$GPGSV,3,1,12,06,70,015,13,19,64,092,12,17,37,109,14,21,25,197,20*7B
$GPGSV,3,2,12,22,18,169,16,51,31,225,,28,26,173,,09,18,099,*73
$GPGSV,3,3,12,04,14,067,,25,08,323,,03,07,036,,23,05,148,*7F
$GPRMC,192013.000,A,4104.4957,N,07326.8004,W,0.70,121.09,270326,,,A*78
$GPGGA,192014.000,4104.4954,N,07326.8006,W,1,05,4.1,13.1,M,-34.3,M,,0000*58
$GPGSA,M,3,06,19,17,21,22,,,,,,,,8.3,4.1,7.2*3E
$GPRMC,192014.000,A,4104.4954,N,07326.8006,W,0.05,121.09,270326,,,A*7C
$GPGGA,192015.000,4104.4949,N,07326.8003,W,1,04,2.3,13.4,M,-34.3,M,,0000*50

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
