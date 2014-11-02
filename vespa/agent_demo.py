# -*- coding: utf-8 -*-
# 
# Module name: agent.py
# Version:     1.0
# Created:     29/04/2014 by Aur�lien Wailly <aurelien.wailly@orange.com>
#
# Copyright (C) 2010-2014 Orange
#
# This file is part of VESPA.
#
# VESPA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation version 2.1.
#
# VESPA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with VESPA.  If not, see <http://www.gnu.org/licenses/>.

"""
Agent representation
"""
import socket
from node import Node

class Agent_Node(Agent):
    def __init__(self, name, host, port, master, run=True):
        super(Agent_Node, self,).__init__(name, host, port, master, run)

    def follow(thefile):
	thefile.seek(0,2)      # Go to the end of the file
	while True:
	     line = thefile.readline()
	     if not line:
		 time.sleep(0.1)    # Sleep briefly
		 continue
	     yield line

    def launch(self):
	logfile = open("/home/dad/file")
	loglines = follow(logfile)
	keyword = "bilou"
	for line in loglines:
	    if keyword in line:
		self.sendAlert("new_line#%s" % line)