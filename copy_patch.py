import pexpect
import sys
import os

try:
    patch_path = str(sys.argv[1])
    base=os.path.basename(patch_path)
    os.system('rm -rf ' +base)
    print "File exist previously and removed"
except:
    print "file did not exist previously so trying to download again"

ssh_newkey = 'Are you sure you want to continue connecting'
# my ssh command line
p=pexpect.spawn('scp nramukannan@nramukannan-vm.inca.infoblox.com:' +  str(sys.argv[1]) + ' .')

i=p.expect([ssh_newkey,'password:',pexpect.EOF])
if i==0:
    p.sendline('yes')
    i=p.expect([ssh_newkey,'password:',pexpect.EOF])
if i==1:
    p.sendline("resetm33")
    p.expect(pexpect.EOF)
    #p.sendline("/home/jenkins/./test.sh")
    print p.before
elif i==2:
    print "I either got key or connection timeout"
    pass
print p.before 
