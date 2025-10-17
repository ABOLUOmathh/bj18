#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: root
# Date: 2025-10-17
# File: views.py
# Description: <description>
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')
