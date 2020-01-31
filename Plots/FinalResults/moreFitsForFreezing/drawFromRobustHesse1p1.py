#!/usr/bin/env python

from shanePalette import set_color_palette
from usefulStyle import drawCMS, drawEnPu, setCanvas1p1, formatHisto
from collections import OrderedDict as od
import ROOT as r

r.gROOT.SetBatch(True)
r.gStyle.SetNumberContours(500)

lumi = 137

exts = od()

from pois import POIs

exts['stage1p1'] = POIs

def prettyProc( proc ):
  if proc.startswith('r_'): proc = proc.split('r_')[1]
  name = proc.split('_')[0]
  proc = '_'.join(proc.split('_')[1:])
  proc = proc.replace('GE2J','2J')
  proc = proc.replace('jlike','Jlike')
  proc = proc.replace('2Jlike','VBF-2J-like')
  proc = proc.replace('3Jlike','VBF-3J-like')
  proc = proc.replace('VBFlike','VBF-like')
  proc = proc.replace('VHhad','VH-like')
  proc = proc.replace('_',' ')
  name = name + ' ' + proc
  return name

for ext,pois in exts.iteritems():
  fileName = 'robustHesse_robustHesse.root'
  inFile = r.TFile(fileName,'READ')
  theMatrix = inFile.Get('h_correlation')
  theList   = inFile.Get('floatParsFinal')

  pars = od()
  for iPar,par in enumerate(theList):
    if iPar==len(theList)-1: break
    if not par.GetName().startswith('r_'): continue
    pars[par.GetName()] = iPar
  nPars = len(pars.keys())
  print 'Procesing the following %g parameters:'%nPars
  for par in pars.keys(): print par
  revPars = {i:name for name,i in pars.iteritems()}

  theHist = r.TH2F('corr_%s'%ext, '', nPars, -0.5, nPars-0.5, nPars, -0.5, nPars-0.5)
  theMap = {}

  for iBin,iPar in enumerate(pars.values()):
    for jBin,jPar in enumerate(pars.values()):
      proc = theMatrix.GetXaxis().GetBinLabel(iPar+1)
      #print 'Got proc %s, expecting proc %s'%(proc, revPars[iPar])
      theVal = theMatrix.GetBinContent(iPar+1,jPar+1)
      #print 'Value for correlation between %s and %s is %.3f'%(revPars[iPar],revPars[jPar],theVal)
      theMap[(revPars[iPar],revPars[jPar])] = theVal

  for iBin,iPar in enumerate(pois):
    for jBin,jPar in enumerate(pois):
      theHist.GetXaxis().SetBinLabel(iBin+1, prettyProc(iPar))
      theHist.GetYaxis().SetBinLabel(jBin+1, prettyProc(jPar))
      #print 'Filling correlation for %s and %s of %.3f'%(iPar, jPar, theMap[(iPar,jPar)])
      theHist.Fill(iBin, jBin, theMap[(iPar,jPar)])

  print 'Final correlation map used is:'
  print theMap

  set_color_palette('frenchFlag')
  r.gStyle.SetNumberContours(500)
  r.gStyle.SetPaintTextFormat('1.2f')

  canv = setCanvas1p1()
  formatHisto(theHist)
  theHist.GetXaxis().SetTickLength(0.)
  theHist.GetXaxis().SetLabelSize(0.05)
  theHist.GetYaxis().SetTickLength(0.)
  theHist.GetYaxis().SetLabelSize(0.05)
  theHist.GetZaxis().SetRangeUser(-1.,1.)
  theHist.GetZaxis().SetTickLength(0.)
  if ext.count('Minimal') or ext.count('1p1'): 
    theHist.GetXaxis().SetLabelSize(0.04)
    theHist.GetYaxis().SetLabelSize(0.04)

  theHist.Draw('colz,text')
  drawCMS(True)
  drawEnPu(lumi='%2.0f fb^{-1}'%lumi)
  canv.Print('Plots/Other/corrMatrix_%s.png'%ext)
  canv.Print('Plots/Other/corrMatrix_%s.pdf'%ext)
