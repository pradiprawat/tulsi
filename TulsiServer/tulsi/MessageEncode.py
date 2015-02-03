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

import socket
import json


class MessageEncode():

    # Function to create encoded json format message . It includes the following
    # Json format
    # { "hostname": name of host
    #    "conf_ring": the configuration from container.ring.gz
    #    "conf_ring_ip":the ip's in configuration from container.ring.gz
    #    "host_ip": the ip of host system
    #    "services": the status of services of host system
    #    "drives" : the drives of services of host system }
    def create_message(self,  my_ring_conf, ring_conf_ip, ip_array,
                       service, drives):

        self.my_ring_conf = my_ring_conf
        self.ring_conf_ip = ring_conf_ip
        self.ip_array = ip_array
        self.service = service
        self.drives = drives
        self.host = socket.gethostname()
        self.data = {"hostname": self.host, "conf_ring": self.my_ring_conf,
                     "conf_ring_ip" : self.ring_conf_ip,
                     "host_ip": self.ip_array,
                     "services": self.service, "drives": self.drives}
        self.message = json.dumps(self.data)
        return self.message


