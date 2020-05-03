# dark.fail notifier

This is a crude Python (>3.7) script for checking the status of a site on dark.fail.

## Installation

The requirements of this script are managed with [Pipenv](https://github.com/pypa/pipenv).

It's requirements are `requests` and `loguru`.

## Usage
Usage of this script is self-explanatory. It is described by executing `notifier.py -h`.

```
usage: notifier.py [-h] [-i INTERVAL] site

This is a dark.fail site notifier

positional arguments:
  site         Site to target (e.g. empire)

optional arguments:
  -h, --help   show this help message and exit
  -i INTERVAL  Scraping interval in seconds (default: 5 seconds)
```

## Contributing

Feel free to tinker/fork/change this script to your needs.
This is only a very bare and simple script without much error-checking/validation.
