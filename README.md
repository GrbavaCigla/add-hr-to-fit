# fit-tools
A collection of tools for working with FIT files.
> Note: works only on .fit files!

## How it works
It looks for overlapping timestamps in two activities and adds `heart_rate` data from `hr` to `main` activity.

## Usage
```
usage: add-hr-to-fit [-h] main hr [out]

Small simple project to add HR data from one activity to another. Used for when my HR strap stops working.

positional arguments:
  main        file to which the heart data will be added.
  hr          file which holds heart data.
  out         output file of the combined activities.

options:
  -h, --help  show this help message and exit
```
