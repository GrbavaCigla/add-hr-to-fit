# fit-tools
A collection of tools for working with FIT files.
> Note: works only on .fit files!

## How it works
It looks for overlapping timestamps in two activities and adds `heart_rate` data from `hr` to `main` activity.

## Usage
```
usage: fit-tools [-h] {add-hr} ...

A collection of tools for working with FIT files.

positional arguments:
  {add-hr}
    add-hr    Add heart rate data from one FIT file to another.

options:
  -h, --help  show this help message and exit
```
