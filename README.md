# python-honcho
Python endpoint to kill, bounce, and start processes. Based on PSUtil: http://psutil.readthedocs.io

## list all processes:
`/processes`

## kill a process:
`/kill/<process>`

## bounce a process:
_Now has multiple OS support_

`/bounce/<process>`

## start a process:
`/start/<process>`

## experimentally start any OS process:
_Now has experimental support for all OS's_

`/startExperimental/<process>`

## mac bounce a process
`/mac/bounce/<process>`

## mac start a process
`/mac/start/<process>`

## restart IIS
`/iis`
