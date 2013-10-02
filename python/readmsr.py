#!/usr/bin/env python
import sys
import struct

MSR_FILE_FMT="/dev/cpu/%d/msr"
MSR_READ_BYTES=8    # if you change, also change print in main(),
                    # and unpacking in read_msr()

def read_msr(cpu, offs) :
    msr_filename = MSR_FILE_FMT % cpu
    try : 
        f = open(msr_filename, "r", 0)  # 0 -> unbuffered
    except Exception as ex :
        print "Make sure you run as root, and modprobe msr."
        print " open(%s) failed:" % msr_filename
        raise ex

    f.seek(offs)
    val = f.read(MSR_READ_BYTES)
    return struct.unpack("II", val)

def usage() :
    print ("Usage: %s <cpu-num> <offset>\n\tReads %d bytes from cpu's msr "
        + "at offset.") % (sys.argv[0], MSR_READ_BYTES)
    print "\tMake sure you run as root."
    sys.exit()

def main() :
    if len(sys.argv) != 3 :
        usage()
    cpu = int(sys.argv[1])
    offs = long(sys.argv[2], 0)
    (lo, hi) = read_msr(cpu, offs)
    print "%0x %0x" % (hi,lo) 

if __name__ == "__main__" :
    main()

# vim: ai ts=4 sts=4 et sw=4
