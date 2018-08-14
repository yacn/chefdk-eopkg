#!/usr/bin/python

# Create For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf chefdk_%s-1_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.gz")
    shelltools.system("tar xvf control.tar.gz")

def install():
    pisitools.insinto("/opt", "opt/chefdk")
    shelltools.system("sh postinst")
