#!/usr/bin/env python

from os import system

def run(cmd):
  print cmd
  system(cmd)

from pois import POIs 

#job_opts = ' --sub-opts "-q hep.q -l h_rt=10:0:0 -l h_vmem=12G" '
job_opts = ' --sub-opts "-q hep.q -l h_rt=3:0:0 -l h_vmem=24G" '

for poi in POIs:
  fitCmd = 'combineTool.py --task-name JobsFor_%s -M MultiDimFit -m 125 -d allAnalyses.root --floatOtherPOIs 1 --expectSignal 1 -t -1  -n _scanOf_%s --saveSpecifiedNuis all --saveInactivePOI 1 -P %s --algo grid --points 5 --alignEdges 1 --split-points 1 --cminDefaultMinimizerStrategy 0 --job-mode SGE %s --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2'%(poi,poi,poi,job_opts)
  run(fitCmd)
