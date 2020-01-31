#!/bin/sh
ulimit -s unlimited
set -e
cd /vols/build/cms/es811/FreshStart/HggAnalysis/Pass1/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /vols/build/cms/es811/FreshStart/HggAnalysis/Pass1/CMSSW_10_2_13/src/flashggFinalFit/Plots/FinalResults/moreFitsForFreezing
combine -M MultiDimFit -m 125 -d allAnalyses.root --floatOtherPOIs 1 --expectSignal 1 -t -1  -n _robustHesse --saveSpecifiedNuis all --saveInactivePOI 1 -P r_ggH_0J_low --robustHesse 1 --robustHesseSave 1 --saveFitResult --cminDefaultMinimizerStrategy 0 -v 3 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
