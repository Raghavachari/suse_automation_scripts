#/bin/bash

DEPLOYMENT_SERVICES=ioa
IP=$1
ib_patch=$2
wapi=https://192.168.124.159/wapi/v1.4.1
members='[{"ipv4addr": "192.168.124.159", "name": "master.com"}, {"ipv4addr": "192.168.124.162", "name": "member2.com"}, {"ipv4addr": "192.168.124.163", "name": "member3.com"}]'
if [ x$IP == x ]; then
echo "IP address is not specified"
fi

if [ x$ib_patch == x ]; then
echo "patch is not specified"
exit 0
fi

eth_port=`ifconfig -a |grep eth0 |awk '{print $1}' | sed s/\\..*// | sort -u`
patch_file=`basename $ib_patch`
zypper in expect
sleep 10

patch_folder=`echo $patch_file | sed -r 's/\.[[:alnum:]]+\.[[:alnum:]]+$//'`
tar -mxf $patch_file
f1="/root/$patch_folder/ib_localrc"
f2="/root/$patch_folder/ib_ioarc"

sed -i 's/export DEPLOYMENT_SERVICES=.*/export DEPLOYMENT_SERVICES='$DEPLOYMENT_SERVICES'/' $f1

sed -i 's+export\ WAPI=.*+export\ WAPI=https:\/\/192.168.124.159\/wapi\/v1.4.1\/+' $f2
sed -i "s/export IB_MEMBERS=.*/export IB_MEMBERS='$members'/" $f2
sed -i 's/export IOA_HOST_IP=.*/export IOA_HOST_IP='$IP'/' $f2
sed -i 's/export IOA_HOST_GATEWAY=.*/export IOA_HOST_GATEWAY=192.168.124.1/' $f2
sed -i 's/export IOA_HOST_NETMASK=.*/export IOA_HOST_NETMASK=255.255.255.0/' $f2
sed -i 's/export IOA_HOST_DNS=.*/export IOA_HOST_DNS=192.168.124.159/' $f2
sed -i 's/export IOA_INTERFACE=.*/export IOA_INTERFACE='$eth_port'/' $f2                                                                        
sed -i 's/IOA_SKIP_IPV6_DISABLING=.*/IOA_SKIP_IPV6_DISABLING=true/' $f2
echo "file patched sucessfully going to deploy..."

echo "Tempest Pre-requisite packages install.."
zypper --non-interactive in git-core
 
