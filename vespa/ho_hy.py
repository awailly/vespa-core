# -*- coding: utf-8 -*-
#
# Module name: ho_hy.py
# Version:     1.0
# Created:     29/04/2014 by Aurélien Wailly <aurelien.wailly@orange.com>
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
Horizontal orchestrator
"""
import socket
from log_pipe import debug1
from agent import Agent
from ho import HO


class HO_HY(HO):
    """Create an horizontal orchestrator to handle agents at the hypervisor
    level.

    :return: The HO to gather and react on hypervisor agents.
    :rtype: Node
    """

    def __init__(self, name, host, port, master, run=True):
        super(HO_HY, self).__init__(name, host, port, master, run)
        self.have_backend = False

    def send(self, msg):
        """Overload the internal send() to capture and send messages to the
        backend

        :param str msg: The massage to process and to send
        :return: The backend response
        :rtype: str
        """
        data = super(HO_HY, self).send(msg)
        # self.sendRemote( self.master, data )
        return data

    def ninjaMethod(self):
        """Empty function for tests
        """
        pass
