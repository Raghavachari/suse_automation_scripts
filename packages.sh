#!/bin/bash
echo "Installing GIT Package:"
zypper --non-interactive in git-core

echo "Changing the Gateway to access internet from SUSE:"
route del default gw 192.168.126.1
route add default gw 192.168.124.1

echo "Installing pre requisite packages for Tempest"
easy_install testscenarios
easy_install discover
easy_install unittest2
easy_install testresources
easy_install testtools
easy_install fixtures
easy_install nose



