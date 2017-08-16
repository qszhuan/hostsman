[![Build Status](https://travis-ci.org/qszhuan/hostsman.svg?branch=master)](https://travis-ci.org/qszhuan/hostsman)

<!-- TOC -->

- [hostsman](#hostsman)
    - [INSTALLATION](#installation)
    - [USAGE](#usage)
        - [Help](#help)
        - [List mappings in hosts file](#list-mappings-in-hosts-file)
        - [Check HOSTNAME](#check-hostname)
            - [Check if a hostname is configured in hosts file.](#check-if-a-hostname-is-configured-in-hosts-file)
            - [Check multiple hostnames](#check-multiple-hostnames)
        - [Insert mappings](#insert-mappings)
            - [Add single mapping](#add-single-mapping)
            - [Add multiple mappings.](#add-multiple-mappings)
        - [Remove mapping](#remove-mapping)

<!-- /TOC -->


# hostsman

`hostsman` is a cross-platform command line tool for adding, removing or listing mappings in hosts file.
It's written in python.

![image](/hostsman.png)
## INSTALLATION

You can use pip to install this tool.
Run `pip install hostsman`.

You can also find the packages by this link: [hostsman](https://pypi.python.org/pypi/hostsman)

It works on python 2.6, python 2.7, and python 3.x.

## USAGE

### Help

Run `hostsman` or `hostsman -h` to check the help doc:

```
(pypi) ➜  hosts git:(master) ✗ hostsman
usage: hostsman [-h] [-l | -c HOSTNAME [HOSTNAME ...] | -i HOSTNAME[:IP]
             [HOSTNAME[:IP] ...] | -r HOSTNAME [HOSTNAME ...]]

Add, remove or list mappings in hosts file

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

###  List mappings in hosts file

Run **`hostsman -l`** to list out the content of hosts file.

``` 
127.0.0.1      	localhost
255.255.255.255	broadcasthost
::1             localhost
fe80::1%lo0    	localhost
127.0.0.1      	my.local
```

###  Check HOSTNAME

#### Check if a hostname is configured in hosts file.

Run `hostsman -c localhost`,

It will return the result if `localhost` is in hosts file:

```
# Search result:
127.0.0.1      	localhost
::1             localhost
fe80::1%lo0    	localhost
```

#### Check multiple hostnames

Run `hostsman -c my.local my.local2`,

It will print out the mappings for given hostnames

```
# Search result:
127.0.0.1      	my.local
127.0.0.1      	my.local2
```

### Insert mappings

#### Add single mapping

Run `hostsman -i my.local3:192.1.1.3`, it will insert new mapping:

`192.1.1.3		my.local3`

If ip is not given, the default value `127.0.0.1` will be used:

Run `hostsman -i my.local4`, it will insert mapping: 

`127.0.0.1 		my.local4`

If the ip is already existed in hosts file, the insert operation will add the hostname on the same line of the ip, for example:

Run `hostsman -i my.local5`, the hosts file will be:

`127.0.0.1 		my.local4 my.local5`


#### Add multiple mappings.

Run `hostsman -i my.local my.local2:192.1.1.3`, it will insert:

```
127.0.0.1 		my.local
192.1.1.3     my.local2
```

### Remove mapping

Run `hostsman -r my.local` to remove `my.local`;

If the ip is only mapping to one host name, remove the host name will also remove the whole line.

For example, this the hosts file:

```
127.0.0.1 		my.local
192.1.1.3     my.local2 my.local3
```
After run `hostsman -r my.local`, the file will be:

```
192.1.1.3     my.local2 my.local3
```

After run `hostsman -r my.local2`, the file will be:

```
192.1.1.3     my.local3
```

**A backup file will be created for every add/remove operation(when the hostname is existed)**




