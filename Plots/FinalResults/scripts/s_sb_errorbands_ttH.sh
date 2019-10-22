#!/bin/bash

# Usage of this scipt
#./s_sb_errorbands.sh <index> <working directory> <MHhat> <Muhat>
# your input rool file must be called inputfile.root
nToys=1
MHhat=$3
Muhat=$4
dir=$2 
((startIndex=$1*10000))
index=$startIndex

#STOREDIR="/eos/home-e/escott/Stage1STXS/Pass7/ToysForSplusB"
STOREDIR="$PWD/tempSplusBoutput"

cd $dir
eval `scramv1 runtime -sh`

while (( $index < $startIndex+ $nToys)); 
do
echo "combine inputfile.root  -m $MHhat --snapshotName MultiDimFit -M GenerateOnly --saveWorkspace --toysFrequentist --bypassFrequentistFit -t 1 --expectSignal=$Muhat -n combout_step0_$index --saveToys"
combine $STOREDIR/inputfile.root  -m $MHhat --snapshotName MultiDimFit -M GenerateOnly --toysFrequentist --bypassFrequentistFit -t 1 --expectSignal=1 --setPhysicsModelParameters r_ttH=$Muhat -n combout_step0_$index --saveToys -s -1

mv higgsCombinecombout_step0_${index}.GenerateOnly*.root $STOREDIR/higgsCombinecombout_step0_done_$index.root

echo "combine inputfile.root --toysFile higgsCombinecombout_step0_done_$index.root -m $MHhat -M MultiDimFit --floatOtherPOIs=1 --saveWorkspace -t 1 -n combout_step1_$index"
combine $STOREDIR/inputfile.root --toysFile $STOREDIR/higgsCombinecombout_step0_done_$index.root -m $MHhat -M MultiDimFit -P r_ttH --floatOtherPOIs=1 --saveWorkspace -t 1 -n combout_step1_$index

mv higgsCombinecombout_step1_${index}.MultiDimFit*.root $STOREDIR/higgsCombinecombout_step1_done_$index.root

echo "combine higgsCombinecombout_step1_done_$index.root -m $MHhat --snapshotName MultiDimFit -M GenerateOnly --saveToys --toysFrequentist --bypassFrequentistFit -t -1 -n combout_step2_$index --expectSignal=0"
combine $STOREDIR/higgsCombinecombout_step1_done_$index.root -m $MHhat --snapshotName MultiDimFit -M GenerateOnly --saveToys -t -1 -n combout_step2_$index --expectSignal=0

mv higgsCombinecombout_step2_${index}.GenerateOnly*.root $STOREDIR/higgsCombinecombout_step2_done_$index.root

(( index=$index+1))
done;
