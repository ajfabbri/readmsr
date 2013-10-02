readmsr
=======

Command line tool to read CPU Model Specific Registers (MSR).

For example, to read the Time Stamp Counter (in a very inefficient manner),
on CPU #0 (x86):

$ sudo ./readmsr.py 0 0x10
191f 1c7032c8

I'm using it to read the SMI (system management interrupt) counter on 
Nehalem and newer Intel CPUs:

$ sudo ./readmsr.py 0 0x34
0 310

