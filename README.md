# hoste
add, remove or list mappings in hosts file

```

usage: host.py [-h] [-l | -c HOSTNAME [HOSTNAME ...] | -i HOSTNAME[:IP]
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