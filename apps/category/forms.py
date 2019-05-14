# -*- coding: utf-8 -*-
__author__ = 'oldlee'
__date__ = '2019-05-14 15:35'
from django import forms


class RepairForm(forms.Form):
    # email字段为必填
    name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    userage = forms.IntegerField(required=True)
    repairregion = forms.CharField(required=True)
    repaircategory = forms.CharField(required=True)
    repaircontent = forms.CharField(required=True)

