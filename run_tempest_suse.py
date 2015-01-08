import time
import subprocess
import os
import sys
import pexpect

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()

    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise ProcessException(command, exitCode, output)

try:
    machineip = str(sys.argv[1])
except:
   print "please pass the machine ip"
   exit (0)


command = 'scp ' + os.getcwd() + '/packages.sh ' + ' ' + 'root@' + machineip  + ':/root/' 
execute([command])
time.sleep(2)
command = 'ssh root@' + machineip + ' /root/packages.sh '
execute([command])
command = 'ssh root@' + machineip + ' ' + 'git clone https://github.com/Raghavachari/tempest-infoblox.git'
execute([command])
time.sleep(5)
command = 'ssh root@' + machineip + ' ' + 'chmod +x /root/tempest-infoblox/update_config_suse.sh'
execute([command])
time.sleep(5)
command = 'ssh root@' + machineip + ' ' + '/root/tempest-infoblox/./update_config_suse.sh'
execute([command])
time.sleep(5)
command = 'scp ' + os.getcwd() + '/run_tempest.sh' + ' ' + 'root@' + machineip  + ':/root/'
execute([command])
command = 'ssh root@' + machineip + ' ' + '/root/./run_tempest.sh'
execute([command])
time.sleep(5)

