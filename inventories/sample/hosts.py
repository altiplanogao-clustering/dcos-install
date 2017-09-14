#!/usr/bin/env python


import sys, os, imp
# sys.path.append('..')
xinv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "XInv.py")
XInv = imp.load_source('XInv', xinv_path)

this_path = os.path.dirname(os.path.realpath(__file__))

XInv.XInv(host_files = [
    os.path.join(this_path, "_hosts.yml")
], group_files = [
    os.path.join(this_path, "_groups.yml")
])