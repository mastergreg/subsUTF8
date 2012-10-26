#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : subsUTF8.py
#
#* Purpose :
#
#* Creation Date : 02-10-2011
#
#* Last Modified : Fri 26 Oct 2012 04:45:40 PM EEST
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
  print "Usage: subsUTF8.py fileIn.srt (optional fileOut.srt)"


def main():
  if len(sys.argv)==2:
    pathIn = sys.argv[1]
    pathOut = "".join(sys.argv[1].split(".")[:-1])+"_converted_.srt"
    convert(pathIn,pathOut)
  elif len(sys.argv)==3:
    pathIn = sys.argv[1]
    pathOut = sys.argv[2]
    convert(pathIn,pathOut)
  else:
    printUsage()
    return 1


  





if __name__=="__main__":
  main()
