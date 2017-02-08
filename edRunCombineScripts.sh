#!/bin/bash

FILE="/vols/cms/szenz/ws_826b/output_GluGluHToGG_M120_13TeV_amcatnloFXFX_pythia8.root,/vols/cms/szenz/ws_826b/output_VBFHToGG_M120_13TeV_amcatnlo_pythia8.root,/vols/cms/szenz/ws_826b/output_WHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ZHToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ttHJetToGG_M120_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root,/vols/cms/szenz/ws_826b/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root,/vols/cms/szenz/ws_826b/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_GluGluHToGG_M130_13TeV_amcatnloFXFX_pythia8.root,/vols/cms/szenz/ws_826b/output_VBFHToGG_M130_13TeV_amcatnlo_pythia8.root,/vols/cms/szenz/ws_826b/output_WHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ZHToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ttHJetToGG_M130_13TeV_amcatnloFXFX_madspin_pythia8.root"

DATA="/vols/cms/szenz/ws_826b/allData.root"

FILE125="/vols/cms/szenz/ws_826b/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root,/vols/cms/szenz/ws_826b/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root,/vols/cms/szenz/ws_826b/output_WHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ZHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root,/vols/cms/szenz/ws_826b/output_ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8.root"

#EXT="AllTags06Feb_nGausSSForder1"
EXT="AllTags06Feb_nGausSSFfinetuned"
echo "Ext is $EXT"
PROCS="ggh,vbf,tth,wh,zh"
echo "Procs are $PROCS"
#CATS="UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,VBFTag_0,VBFTag_1,TTHHadronicTag,TTHLeptonicTag,ZHLeptonicTag,WHLeptonicTag,VHLeptonicLooseTag,VHHadronicTag,VHMetTag"
CATS="UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,VBFTag_0,VBFTag_1,VBFTag_2,TTHHadronicTag,TTHLeptonicTag,ZHLeptonicTag,WHLeptonicTag,VHLeptonicLooseTag,VHHadronicTag,VHMetTag"
echo "Cats are $CATS"
INTLUMI=36.8
echo "Intlumi is $INTLUMI"
BATCH="IC"
echo "Batch is $BATCH"
QUEUE="hep.q"
echo "Batch is $QUEUE"
BSWIDTH=3.400000
echo "Bswidth is $BSWIDTH"
NBINS=320
echo "Nbins is $NBINS"

SCALES="HighR9EB,HighR9EE,LowR9EB,LowR9EE"
SCALESCORR="MaterialCentral,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"
SCALESGLOBAL="NonLinearity:UntaggedTag_0:2,Geant4"
SMEARS="HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho"

#MASSLIST="120,123,124,125,126,127,130"
MASSLIST="120,125,130"
MLOW=120
MHIGH=130
echo "Masslist is $MASSLIST"
SIGFILE="/vols/build/cms/es811/FreshStart/Pass1/AllTags/CMSSW_7_4_7/src/flashggFinalFit/Signal/outdir_${EXT}/CMS-HGG_sigfit_${EXT}.root"

#./runFinalFitsScripts.sh -i $FILE125 -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --datacardOnly \
#                         --smears $SMEARS --scales $SCALES --scalesCorr $SCALESCORR --scalesGlobal $SCALESGLOBAL 
./runFinalFitsScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --combineOnly
#./runFinalFitsScripts.sh -i $FILE -p $PROCS -f $CATS --ext $EXT --intLumi $INTLUMI --batch $BATCH --dataFile $DATA --isData --combinePlotsOnly

#./yieldsTable.py -w $FILE125 -s Signal/signumbers_${EXT}.txt -u Background/CMS-HGG_multipdf_$EXT.root --factor $INTLUMI -f $CATS --order "Total,ggh,vbf,wh,zh,tth:Untagged Tag 0,Untagged Tag 1,Untagged Tag 2,Untagged Tag 3,VBF Tag 0,VBF Tag 1,VBF Tag 2,TTH Hadronic Tag,TTH Leptonic Tag,ZH Leptonic Tag,WH Leptonic Tag,VH LeptonicLoose Tag,VH Hadronic Tag,VH Met Tag,Total"
#./makeEffAcc.py $FILE Signal/outdir_${EXT}/sigfit/effAccCheck_all.root $INTLUMI
