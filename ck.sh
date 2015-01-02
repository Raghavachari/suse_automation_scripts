#/bin/bash
echo $1
export machine_ip=$1
/opt/stack/vm-scripts/copy_key
echo "copying done....."
