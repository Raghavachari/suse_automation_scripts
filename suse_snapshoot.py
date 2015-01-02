#!/usr/bin/python

from pysphere import VIServer
import re
import sys

server = VIServer()
server.connect("10.39.19.100","root","vmware",trace_file="debug.txt")

vmlist = server.get_registered_vms()
for i in vmlist:
    if re.search(sys.argv[1],i):
        vm =  i

vm1 = server.get_vm_by_path(vm)

vm1.create_snapshot(sys.argv[2], description=sys.argv[2])

