# python-killer
Python endpoint to kill a process

## usage
this will listen on the port you define. To kill a process send a GET request to /kill/<processname>. A JSON will be returned to confirm process killed.
  
Based on psutil for cross platform support: https://psutil.readthedocs.io/en/latest/
