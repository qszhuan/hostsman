[![Build Status](https://travis-ci.org/qszhuan/hoste.svg?branch=master)](https://travis-ci.org/qszhuan/hoste)

### hoste
=====


add, remove or list mappings in hosts file

### Installation

You can use pip to install this tool.

Run `pip install hoste`


### Usage

#### $ running `hoste` without any arguments will print out the help doc.
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

* check one hostname

hoste -c hostname

* check multiple hostnames

host -c hostname1 hostname2

it will print out the mappings for given hostnames


#### $ insert new mapping

* Add single mapping

hoste -i my.local:192.1.1.3 # will insert 192.1.1.3     my.local

* If the ip not given, it will use 127.0.0.1 by default:

hoste -i my.local   # will insert 127.0.0.1     my.local

* You can also add multiple mappings in one go.

hoste -r my.local my.local2:192.1.1.3

#### $ remove mapping

hoste -r my.local

A backup file will be created for every removal operation(when the hostname is existed)





