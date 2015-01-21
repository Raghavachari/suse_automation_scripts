#!/bin/bash

cd /root/tempest/
nosetests -v tempest.thirdparty.infoblox.scenarios.test_ext_floating_ip
sleep 5
nosetests -v tempest.thirdparty.infoblox.scenarios.test_create_del_snets
sleep 5
nosetests -v tempest.thirdparty.infoblox.scenarios.test_snet_range
sleep 5
nosetests -v tempest.thirdparty.infoblox.scenarios.test2
sleep 5
nosetests -v tempest.thirdparty.infoblox.scenarios.test_scenario
