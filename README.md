[![Build Status](https://travis-ci.org/qszhuan/hoste.svg?branch=master)](https://travis-ci.org/qszhuan/hoste)

hoste
=====

add, remove or list mappings in hosts file

## INSTALLATION

You can use pip to install this tool.

Run `pip install hoste`.


## Usage

### $ Help

Run `hoste` or `hoste -h` to check the help doc:

```
(pypi) ➜  hoste git:(master) ✗ hoste
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

hosts file location: /etc/hosts
```
The last line of help gives the hosts file location on your pc.

### $ List mappings in hosts file

Run **`hoste -l`** to list out the content of hosts file.

``` 
127.0.0.1      	localhost
255.255.255.255	broadcasthost
::1             localhost
fe80::1%lo0    	localhost
127.0.0.1      	my.local
```

### $ Check HOSTNAME

#### check if a hostname is configured in hosts file.

Run `hoste -c hostname`,

It will return the result if `hostname` is in hosts file:

```
# Search result:
127.0.0.1      	localhost
::1             localhost
fe80::1%lo0    	localhost
```

#### check multiple hostnames

Run `host -c my.local my.local2`

it will print out the mappings for given hostnames

```
# Search result:
127.0.0.1      	my.local
127.0.0.1      	my.local2
```

### Insert mappings

#### Add single mapping

Run `hoste -i my.local3:192.1.1.3`, it will insert new mapping:

`192.1.1.3		my.local3`

If not given ip, the default value `127.0.0.1` will be used:

Run `hoste -i my.local4`, it will insert mapping: 

`127.0.0.1 		my.local4`


#### Add multiple mappings.

`hoste -r my.local my.local2:192.1.1.3`

### $ Remove mapping

`hoste -r my.local`

__ A backup file will be created for every removal operation(when the hostname is existed) __




