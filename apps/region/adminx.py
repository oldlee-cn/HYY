# -*- coding: utf-8 -*-
__author__ = 'oldlee'
__date__ = '2019-05-13 15:55'

from xadmin import views
import xadmin
from .models import Region


class RegionAdmin(object):
    pass

xadmin.site.register(Region,RegionAdmin)