#!/usr/bin/env python

from os import system

def run(cmd):
  print cmd
  system(cmd)

from pois import POIs 

for poi in POIs:
  haddCmd = 'hadd fullScanOf_%s.root higgsCombine_scanOf_%s.POINTS.*.*.MultiDimFit.mH125.root'%(poi,poi)
  run(haddCmd)
  plotCmd = 'plot1DScan.py fullScanOf_%s.root --y-cut 40 -o Plots/llScanOf_%s --POI %s '%(poi,poi,poi)
  run(plotCmd)
