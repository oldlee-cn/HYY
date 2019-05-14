# -*- coding: utf-8 -*-
__author__ = 'oldlee'
__date__ = '2019-05-13 15:56'

from xadmin import views
import xadmin
from .models import Category


class CategoryAdmin(object):
    pass


xadmin.site.register(Category,CategoryAdmin)