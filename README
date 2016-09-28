[![Build Status](https://travis-ci.org/qszhuan/hoste.svg?branch=master)](https://travis-ci.org/qszhuan/hoste)

### hoste
=====


add, remove or list mappings in hosts file

### Usage

#### Help
```

usage: hoste [-h] [-l | -c HOSTNAME [HOSTNAME ...] | -i HOSTNAME[:IP]
               [HOSTNAME[:IP] ...] | -r HOSTNAME [HOSTNAME ...]]

add, remove or list mappings in hosts file

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            Show the content of hosts file
  -c HOSTNAME [HOSTNAME ...], --check HOSTNAME [HOSTNAME ...]
                        Check if the host name existed in the host file
  -i HOSTNAME[:IP] [HOSTNAME[:IP] ...], --insert HOSTNAME[:IP] [HOSTNAME[:IP] ...]
                        Insert HOSTNAME[:IP] mappings
  -r HOSTNAME [HOSTNAME ...], --remove HOSTNAME [HOSTNAME ...]
                        Remove mapping for HOSTNAME from hosts file.
```

#### $ list content of host file

hoste -l


#### $ check if hostname is configured in hosts file

hoste -c hostname


#### $ insert new mapping

hoste -c my.local:192.1.1.3 my.local3

#### $ remove mapping

hoste -r my.local

A backup file will be created for every removal operation(when the hostname is existed)





