#!/usr/bin/env python

# Copyright (c) 2015 Vedams Software Solutions PVT LTD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import netifaces
import os
import commands


class HostInfo(object):
    '''
    class Docs
    '''

    def __init__(self):
        self.name_server = ['swift-proxy', 'swift-object',
                            'swift-object-replicator',
                            'swift-object-updater', 'swift-object-auditor',
                            'swift-container', 'swift-container-replicator',
                            'swift-container-updater',
                            'swift-container-auditor',
                            'swift-account', 'swift-account-replicator',
                            'swift-account-reaper', 'swift-account-auditor']

    # Function to read the ip's of host systems
    def read_ip(self):
        self.ip_array = []
        self.x = netifaces.interfaces()
        for i in self.x:
            k = netifaces.ifaddresses(i)
            z = k[2][0]['addr']
            self.ip_array.append(z)
        
        return self.ip_array

    # Function to read swift services and check their status of the host system
    def read_services(self):
        self.service = []
        for z in self.name_server:
            self.command = "service %s status" % z
            self.output = commands.getoutput(self.command)
            self.test_command = "%s: unrecognized service" % z
            self.test_command_1 = "%s stop/waiting" % z
            if((self.test_command == self.output)
               or (self.test_command_1 == self.output)):
                self.service.append("%s:False" % z)
            else:
                self.service.append("%s:True" % z)

        return self.service

    # function to create drives

    def read_drives(self, drives):
        self.drives = drives
        self.line = os.popen("blkid").read()
        self.k = self.line.split("\n")
        for i in self.k:
            self.m = i.split(":")
            self.command_drive = "mount | grep -c " + self.m[0]
            if((commands.getoutput(self.command_drive)) == "1"):
                self.j = self.m[0].split("/")
                self.drives.append(self.j[len(self.j)-1])
        return self.drives
