#!/usr/bin/env python

#commands to send to the monolithic runFinalFits.sh script
from os import system, walk

justPrint=False
unblind = False
fTestOnly = False
bkgPlotsOnly = False

#justPrint=True
#unblind = True
fTestOnly = True
#bkgPlotsOnly = True

print 'About to run background scripts'
print 'fTestOnly = %s, bkgPlotsOnly = %s'%(str(fTestOnly), str(bkgPlotsOnly))

#setup files 
ext          = 'fullNewTest2016'
#ext          = 'fullNewTest2017'
print 'ext = %s'%ext

baseFilePath  = '/vols/cms/es811/FinalFits/ws_%s/'%ext
fileNames     = []
for root,dirs,files in walk(baseFilePath):
  for fileName in files: 
    if not fileName.startswith('output_'): continue
    if not fileName.endswith('.root'):     continue
    fileNames.append(fileName)
fullFileNames = '' 
for fileName in fileNames: fullFileNames += baseFilePath+fileName+','
fullFileNames = fullFileNames[:-1]
#print 'fileNames = %s'%fullFileNames

#define processes and categories
procs         = ''
for fileName in fileNames: 
  if 'M125' not in fileName: continue
  procs += fileName.split('pythia8_')[1].split('.root')[0]
  procs += ','
procs = procs[:-1]
cats  = 'RECO_0J_Tag0,RECO_0J_Tag1,RECO_1J_PTH_0_60_Tag0,RECO_1J_PTH_0_60_Tag1,RECO_1J_PTH_60_120_Tag0,RECO_1J_PTH_60_120_Tag1,RECO_1J_PTH_120_200_Tag0,RECO_1J_PTH_120_200_Tag1,RECO_1J_PTH_GT200,'
cats += 'RECO_GE2J_PTH_0_60_Tag0,RECO_GE2J_PTH_0_60_Tag1,RECO_GE2J_PTH_60_120_Tag0,RECO_GE2J_PTH_60_120_Tag1,RECO_GE2J_PTH_120_200_Tag0,RECO_GE2J_PTH_120_200_Tag1,RECO_GE2J_PTH_GT200_Tag0,RECO_GE2J_PTH_GT200_Tag1,'
cats += 'RECO_VBFTOPO_JET3VETO_Tag0,RECO_VBFTOPO_JET3VETO_Tag1,RECO_VBFTOPO_JET3_Tag0,RECO_VBFTOPO_JET3_Tag1,RECO_VBFTOPO_REST'
print 'with processes: %s'%procs
print 'and categories: %s'%cats

#misc config
lumi          = '35.9'
if '2017' in ext: lumi = '41.3'
batch         = 'IC'
queue         = 'hep.q'
print 'lumi %s'%lumi
print 'batch %s'%batch
print 'queue %s'%queue

#input files
dataFile      = baseFilePath+'allData.root'
sigFile       = '$PWD/../Signal/outdir_%s/CMS-HGG_sigfit_%s.root'%(ext,ext)

theCommand = ''
theCommand += './runBackgroundScripts.sh -i '+dataFile+' -p '+procs+' -f '+cats+' --ext '+ext+' --intLumi '+lumi+' --batch '+batch+' --sigFile '+sigFile+' --isData '
if   fTestOnly:    theCommand += '--fTestOnly '
elif bkgPlotsOnly: theCommand += '--bkgPlotsOnly '
if unblind and not fTestOnly: theCommand += '--unblind '
if justPrint: print theCommand
else: system(theCommand)
