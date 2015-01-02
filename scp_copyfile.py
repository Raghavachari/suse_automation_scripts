import pexpect
import sys
import os

try:
    source_file_path = str(sys.argv[1])
    local_path = str(sys.argv[2])
    base=os.path.basename(local_path)
    os.system('rm -rf ' +base)
    remote_machine1 = str(sys.argv[3])
    remote_machine2 = str(sys.argv[4])
    remote_key1 = str(sys.argv[5])
    remote_key2 = str(sys.argv[6])
    if (len(sys.argv)==7):
       print "Argument count is Matching"
except:
       print "Enter the valid arguments to Execute \n 1.Source file path \n 2.Destination file path \n 3.Source machine \n 4. Destination machine \n 5.Remote machine 1 password \n 6.Remote machine 2 password)"

ssh_newkey = 'Are you sure you want to continue connecting'
password1 = remote_machine1 + '\'s password:'
password2 = remote_machine2 + '\'s password:'
# my ssh command line
p=pexpect.spawn('scp ' + str(sys.argv[3]) + ':' +  str(sys.argv[1]) + ' ' + str(sys.argv[4]) + ':' + str(sys.argv[2]) )

i=p.expect([ssh_newkey,password1,password2,pexpect.EOF])
if i==0:
    p.sendline('yes')
    i=p.expect([ssh_newkey,password1,password2,pexpect.EOF])
if i==1:
    p.sendline(str(remote_key1))
    i=p.expect([ssh_newkey,password1,password2,pexpect.EOF])
if i==2:
    p.sendline(str(remote_key2))
    p.expect(pexpect.EOF)
    print p.before
elif i==3:
    print "Username and Password is not valid"
    pass
print p.before
