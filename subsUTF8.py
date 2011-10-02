#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : subsUTF8.py
#
#* Purpose :
#
#* Creation Date : 02-10-2011
#
#* Last Modified : Sun 02 Oct 2011 02:17:46 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/


import sys
import chardet


def convert(pathIn,pathOut):
  f=open(pathIn,"r")
  r=f.read()
  f.close()
  chardict = chardet.detect(r)
  charset = chardict['encoding']
  certainty = chardict['confidence']
  print "Converting to UTF-8 from "+charset +" confidence "+str(certainty)
  content = unicode(r,charset)
  f=open(pathOut,"w")
  f.write(content.encode('utf-8'))
  f.close()

def printUsage():
  print "Usage: +