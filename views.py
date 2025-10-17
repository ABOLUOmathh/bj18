#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: root
# Date: 2025-10-17
# File: views.py
# Description: <description>
from django.http import HttpResponse


def index(request):
    return HttpResponse('index')
