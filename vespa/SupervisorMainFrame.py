# -*- coding: utf-8 -*-
#
# Module name: SupervisorMainFrame.py
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

"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import wx
from . import view_core
import types
import time
from .model import Model

EVT_RESULT_ID = wx.NewId()


def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

# Implementing MainFrame


class SupervisorMainFrame(view_core.MainFrame):

    def __init__(self, parent, model):
        view_core.MainFrame.__init__(self, parent)
        self.model = model
        self.displayTree(self.model)
        EVT_RESULT(self, self.onResult)
        self._result_event_id = EVT_RESULT_ID

        # Tests
        # self.paintCutVM1()
        self.UVMInfected = False
        self.UVMCleaning = False
        self.UVMCutConn = False
        self.globalText = ""
        # self.moveRect( self.rectVM1Pong, 475, 125 )
        # while self.rectVM1Pong.x != 475:
        #    time.sleep(5)
        # self.moveRect( self.rectVM1Pong, 125, 125 )
        # self.UVMInfected = True
        self.lnumber = 0
        self.InfoGrid.AppendCols(2)
        self.ioports = {}
        self.Refresh()
        self.displayConsole("Initialisation terminee.")

    # Handlers for MainFrame events.
    def onClose(self, event):
        dlg = wx.MessageDialog(self,
                               "Do you really want to close this application?",
                               "Confirm Exit",
                               wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.model.destroy()
            self.Destroy()
            pass

    def onResult(self, event):
        """Show Result status."""
        if event.data is None:
            # Thread aborted (using our convention of None return)
            self.displayConsole('uh ?')
        else:
            # Process results here
            # if not "alert" in event.data:
            #    self.displayConsole("%s" % event.data)
            # Dispatch GlobalView on paint
            #    self.globalText = event.data[3:]
            msg = event.data
            source = msg.split("|")[1].split(">")[-2]
            message = msg.split(">")[-1]
            if "iosresults" in message:
                '''
                port = message.split(" ")[2].split("=")[-1]
                valeur = message.split(" ")[3].split("=")[-1]
                '''
                # print(repr(message))
                fulllist = eval(message.split('#')[-1])
                # TODO Fix bug.so
                # fulllist = fulllist[1:]
                for itm in fulllist:
                    # print("item:%s" % repr(itm))
                    port = itm.split(" ")[1].split('=')[-1]
                    valeur = itm.split(" ")[2].split("=")[-1]
                    # self.displayConsole("%s" % event.data)
                    # Unroll for speed
                    # self.appendInfoGrid(port, valeur)
                    self.ioports[port] = valeur

                if self.InfoGrid.GetNumberRows() < len(self.ioports):
                    self.InfoGrid.AppendRows(
                        len(self.ioports) - self.InfoGrid.GetNumberRows())

                self.lnumber = 0
                for iop in self.ioports:
                    port = iop
                    valeur = self.ioports[port]
                    self.InfoGrid.SetCellValue(
                        self.lnumber,
                        0,
                        port.decode("latin-1"))
                    self.InfoGrid.SetCellValue(
                        self.lnumber,
                        1,
                        valeur.decode("latin-1"))
                    self.lnumber += 1
            # if "fuzz_status=" in message:
            if "archi=" in message:
                self.displayConsole("[Archi] %s: %s" %
                                    (source, message.split("=")[-1]))
                self.displayTree(self.model)
            else:
                # self.displayConsole("[%s] %s" % (source, message))
                self.displayConsole("[%s] %s..." % (source, message[0:500]))
            self.InfoGrid.AutoSizeColumns()
            self.Refresh()

    def paintInit(self):
        self.rectPong = wx.Rect(100, 100, 300, 400)
        self.rectVM1Pong = wx.Rect(125, 125, 100, 100)
        self.rectVM2Pong = wx.Rect(275, 125, 100, 100)
        self.rectHypPong = wx.Rect(125, 250, 250, 100)
        self.rectPhyPong = wx.Rect(125, 375, 250, 100)
        self.rectPing = wx.Rect(450, 100, 300, 400)
        # rectVM1Ping = wx.Rect(475, 125, 100, 100)
        self.rectVM2Ping = wx.Rect(625, 125, 100, 100)
        self.rectHypPing = wx.Rect(475, 250, 250, 100)
        self.rectPhyPing = wx.Rect(475, 375, 250, 100)

    def on_paint(self, event):
        # establish the painting surface
        self.dc = wx.PaintDC(self.GlobalViewPanel)
        self.dc.SetPen(wx.Pen('blue', 4))
        # draw a blue line (thickness = 4)
        # self.dc.DrawLine(50, 20, 300, 20)
        self.dc.SetPen(wx.Pen('red', 1))
        # Machine physique pong
        # draw a red rounded-rectangle
        # rect = wx.Rect(50, 50, 100, 100)
        # self.dc.DrawRoundedRectangleRect(rect, 8)
        # draw a red circle with yellow fill
        # self.dc.SetBrush(wx.Brush('yellow'))
        # x = 250
        # y = 100
        # r = 50
        # self.dc.DrawCircle(x, y, r)
        self.dc.DrawText("Etat: %s" % self.globalText, 100, 525)

    def paintCutVM1(self):
        self.dc.DrawCircle(self.rectVM1Pong.x + self.rectVM1Pong.width / 2,
                           self.rectVM1Pong.y + self.rectVM1Pong.height +
                           (self.rectHypPong.y -
                            (self.rectVM1Pong.y + self.rectVM1Pong.height))/2,
                           8)

    def moveRect(self, rect, x, y):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.__moveRectTimer, self.timer)
        self.timerRect = rect
        self.timerMoveX = x
        self.timerMoveY = y
        self.timer.Start(10)

    def __moveRectTimer(self, event):
        padd = 1
        rect = self.timerRect
        x = self.timerMoveX
        y = self.timerMoveY
        if rect.x == x:
            if rect.y == y:
                self.timer.Stop()
            else:
                diff = rect.y - y
                if rect.y + padd > diff:
                    rect.y += padd
                else:
                    rect.y -= padd
        else:
            diff = rect.x - x
            if diff < 0:
                rect.x += padd
            else:
                rect.x -= padd
        self.Refresh()

    def drawTreeItemMenu(self, event):
        # Get orders from Node
        item, flags = self.archiTree.HitTest(event.GetPoint())
        # if not flags & wxTREE_HITTEST_NOWHERE:
        self.archiTree.SelectItem(item)
        text = self.archiTree.GetItemText(item)
        data = self.archiTree.GetItemData(item).GetData()

        menu = wx.Menu()
        name, host, port = data
        node = self.model.findNode(name)
        # print repr( self.model.sendRemote(node, ("help|"))[0].split('#') )
        list_commands = eval(
            self.model.sendRemote(
                node,
                ("help|")))[0].split('#')
        self.menuPopup = []
        self.nodePopup = node
        for command in list_commands:
            if command == "":
                continue
            menuItem = wx.MenuItem(menu, len(self.menuPopup), command)
            self.menuPopup.append(command)
            menu.AppendItem(menuItem)
            wx.EVT_MENU(menu, menuItem.GetId(), self.menuSelection)
        self.PopupMenu(menu, event.GetPoint())

    def menuSelection(self, event):
        command = self.menuPopup[event.GetId()]
        self.displayConsole("Executing \"%s\"" % command)
        result = eval(self.model.sendRemote(self.nodePopup, command + "|"))
        self.displayConsole(" >>> %s" % repr(result))
        # FIXME
        # self.displayNodeResult( result )

    def updateTreeSelection(self, event):
        # Mise Ã  jour informations
        pass

    def displayConsole(self, msg):
        self.richTextConsole.AppendText(str(repr(msg)) + "\n")
        self.richTextConsole.ShowPosition(
            self.richTextConsole.GetLastPosition())

    def displayTree(self, model):
        self.archiTree.DeleteAllItems()
        root = self.archiTree.AddRoot("Architecture")
        # FIXME
        vo = self.model.slaves[0]
        data = wx.TreeItemData(vo)
        vo_name, vo_host, vo_port = vo
        node_vo = self.archiTree.AppendItem(root, vo_name, 0, 0, data)
        vo_slaves_raw = self.model.sendRemote(vo, "list_slaves|")
        vo_slaves = eval(vo_slaves_raw)
        for ho in vo_slaves:
            data = wx.TreeItemData(ho)
            ho_name, ho_host, ho_port = ho
            node_ho = self.archiTree.AppendItem(node_vo, ho_name, 0, 0, data)
            ho_slaves_raw = self.model.sendRemote(ho, "list_slaves|")
            try:
                ho_slaves = eval(ho_slaves_raw)
            except SyntaxError:
                ho_slaves = []
            for agent_name, agent_host, agent_port in ho_slaves:
                data = wx.TreeItemData((agent_name, agent_host, agent_port))
                node_agent = self.archiTree.AppendItem(
                    node_ho,
                    agent_name,
                    0,
                    0,
                    data)
        self.archiTree.ExpandAll()
        self.Refresh()

    def displayNodeResult(self, title_result):
        line_number = 0
        title_tuple = title_result[0]
        result = title_result[1:]
        for item in result:
            column_number = 0
            if isinstance(item, types.TupleType):
                if line_number == 0:
                    # Set grid
                    self.clearInfoGrid()
                    title_num_col = 0
                    for title_value in title_tuple:
                        self.InfoGrid.SetColLabelValue(
                            title_num_col,
                            title_tuple[title_num_col])
                        title_num_col += 1
                    self.InfoGrid.AppendRows(len(result))
                    self.InfoGrid.AppendCols(len(result[0]))
                for value in item:
                    self.InfoGrid.SetCellValue(
                        line_number,
                        column_number,
                        value.decode("latin-1"))
                    if "FOUND" in value:
                        for col in range(0, self.InfoGrid.GetNumberCols()):
                            self.InfoGrid.SetCellBackgroundColour(
                                line_number,
                                col,
                                wx.RED)
                    else:
                        self.InfoGrid.SetCellBackgroundColour(
                            line_number,
                            column_number,
                            wx.GREEN)
                    column_number += 1
            elif isinstance(item, types.StringType):
                self.displayConsole("Result: " + item.replace("|", ""))
            else:
                self.displayConsole("Result: " +
                                    repr(item) +
                                    " " +
                                    str(type(item)))
            line_number += 1
        self.InfoGrid.AutoSizeColumns()

    def appendInfoGrid(self, port, value):
        self.InfoGrid.AppendRows(1)
        self.InfoGrid.SetCellValue(self.lnumber, 0, port.decode("latin-1"))
        self.InfoGrid.SetCellValue(self.lnumber, 1, value.decode("latin-1"))
        self.lnumber += 1
        self.InfoGrid.AutoSizeColumns()

    def clearInfoGrid(self):
        if self.InfoGrid.GetNumberCols() > 0:
            self.InfoGrid.DeleteCols(0, self.InfoGrid.GetNumberCols())
        if self.InfoGrid.GetNumberRows() > 0:
            self.InfoGrid.DeleteRows(0, self.InfoGrid.GetNumberRows())