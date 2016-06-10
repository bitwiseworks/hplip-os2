# -*- coding: utf-8 -*-
#
# (c) Copyright 2001-2015 HP Development Company, L.P.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# Author: Don Welch
#

# Std Lib
from base.g import *

# Local
from .ui_utils import load_pixmap

# Qt
from qt import *
from .paperedgealignform_base import PaperEdgeAlignForm_base



class PaperEdgeAlignForm(PaperEdgeAlignForm_base):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        PaperEdgeAlignForm_base.__init__(self,parent,name,modal,fl)
        self.Icon.setPixmap(load_pixmap("zca.png", 'other'))
        self.value = 1


    def buttonGroup_clicked(self,a0):
        self.value = a0 + 1
