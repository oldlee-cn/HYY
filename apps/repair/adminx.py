# -*- coding: utf-8 -*-
__author__ = 'oldlee'
__date__ = '2019-05-13 15:48'

from xadmin import views
import xadmin
from .models import Repair


class RepairAdmin(object):
    pass


xadmin.site.register(Repair,RepairAdmin)
