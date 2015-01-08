#!/bin/bash

cd /root/tempest/
nosetests -v tempest/thirdparty/infoblox/scenarios/*

