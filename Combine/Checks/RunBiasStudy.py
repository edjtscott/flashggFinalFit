#!/usr/bin/env python
from biasUtils import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d","--datacard",default="Datacard.root")
parser.add_option("-w","--workspace",default="w")
parser.add_option("-t","--toys",action="store_true", default=False)
parser.add_option("-n","--nToys",default=1000,type="int")
parser.add_option("-f","--fits",action="store_true", default=False)
parser.add_option("-p","--plots",action="store_true", default=False)
parser.add_option("-e","--expectSignal",default=1.,type="float")
parser.add_option("--rMin",default=-5,type="float") ##-- rmin for fitting 
parser.add_option("--rMax",default=20.,type="float") ##-- rmax for fitting 
parser.add_option("-m","--mH",default=125.,type="float")
parser.add_option("-c","--combineOptions",default="")
parser.add_option("-s","--seed",default=-1,type="int")
parser.add_option("--dryRun",action="store_true", default=False)
parser.add_option("--poi",default="r")
parser.add_option("--split",default=500,type="int")
parser.add_option("--selectFunction",default=None)

##-- Plotting
parser.add_option("--gaussianFit",action="store_true", default=False) 
parser.add_option("--plot_xbins",default=80,type="int")
parser.add_option("--plot_xmin",default=-4,type="float") ##-- xmin for pull plotting and distribution fitting 
parser.add_option("--plot_xmax",default=4,type="float") ##-- xmax for pull plotting and distribution fitting
parser.add_option("--outputDirectory",default="",type="str") ##-- Output directory for BiasPlots directory. Default to current working directory 

(opts,args) = parser.parse_args()
print
if opts.nToys>opts.split and not opts.nToys%opts.split==0: raise RuntimeError('The number of toys %g needs to be smaller than or divisible by the split number %g'%(opts.nToys, opts.split))

import ROOT as r
r.gROOT.SetBatch(True)
r.gStyle.SetOptStat(2211)

ws = r.TFile(opts.datacard).Get(opts.workspace)

pdfs = rooArgSetToList(ws.allPdfs())
multipdfName = None
for pdf in pdfs:
    if pdf.InheritsFrom("RooMultiPdf"):
        if multipdfName is not None: raiseMultiError() 
        multipdfName = pdf.GetName()
        print 'Conduct bias study for multipdf called %s'%multipdfName
multipdf = ws.pdf(multipdfName)
print

varlist = rooArgSetToList(ws.allCats())
indexName = None
for var in varlist:
    if var.GetName().startswith('pdfindex'):
        if indexName is not None: raiseMultiError()
        indexName = var.GetName()
        print 'Found index called %s'%indexName
print

from collections import OrderedDict as od
indexNameMap = od()
for ipdf in range(multipdf.getNumPdfs()):
    if opts.selectFunction is not None:
        if not multipdf.getPdf(ipdf).GetName().count(opts.selectFunction): continue
    indexNameMap[ipdf] = multipdf.getPdf(ipdf).GetName()

##-- Generate toys 
if opts.toys:
    if not os.path.isdir('BiasToys'): os.system('mkdir -p BiasToys')
    toyCmdBase = 'combine -m %.4f -d %s -M GenerateOnly --expectSignal %.4f --rMin %.4f --rMax %.4f -s %g --saveToys %s '%(opts.mH, opts.datacard, opts.expectSignal, opts.rMin, opts.rMax, opts.seed, opts.combineOptions)
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                toyCmd = toyCmdBase + ' -t %g -n _%s_split%g --setParameters %s=%g --freezeParameters %s'%(opts.split, name, isplit, indexName, ipdf, indexName)
                run(toyCmd, dry=opts.dryRun)
                os.system('mv higgsCombine_%s* %s'%(name, toyName(name,split=isplit)))
        else: 
            toyCmd = toyCmdBase + ' -t %g -n _%s --setParameters %s=%g --freezeParameters %s'%(opts.nToys, name, indexName, ipdf, indexName)
            run(toyCmd, dry=opts.dryRun)
            os.system('mv higgsCombine_%s* %s'%(name, toyName(name)))
print

if opts.fits:
    if not os.path.isdir('BiasFits'): os.system('mkdir -p BiasFits')
    fitCmdBase = 'combine -m %.4f -d %s -M MultiDimFit -P %s --algo singles %s --rMin %.4f --rMax %.4f '%(opts.mH, opts.datacard, opts.poi, opts.combineOptions, opts.rMin, opts.rMax)
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                fitCmd = fitCmdBase + ' -t %g -n _%s_split%g --toysFile=%s'%(opts.split, name, isplit, toyName(name,split=isplit))
                run(fitCmd, dry=opts.dryRun)
                os.system('mv higgsCombine_%s* %s'%(name, fitName(name,split=isplit)))
            run('hadd %s BiasFits/*%s*split*.root'%(fitName(name),name), dry=opts.dryRun)
        else:
            fitCmd = fitCmdBase + ' -t %g -n _%s --toysFile=%s'%(opts.nToys, name, toyName(name))
            run(fitCmd, dry=opts.dryRun)
            os.system('mv higgsCombine_%s* %s'%(name, fitName(name)))

if opts.plots:
    if not os.path.isdir('BiasPlots'): os.system('mkdir -p BiasPlots')
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        tfile = r.TFile(fitName(name))
        # skips = ["bern", "exp", "pow"]
        # skips = ["bern"]
        skips = [] 
        dontPlot = 0
        for skip in skips:
            if skip in fitName(name):
                dontPlot = 1 
        if(dontPlot == 1): 
            print("SKIPPING by hand")
            continue 
        tree = tfile.Get('limit')
        print("tree:",tree)
        pullHist = r.TH1F('pullsForTruth_%s'%name, 'Pull distribution using the envelope to fit %s'%(name), opts.plot_xbins, opts.plot_xmin, opts.plot_xmax)
        pullHist.GetXaxis().SetTitle('Pull')
        pullHist.GetYaxis().SetTitle('Entries')
        for itoy in range(opts.nToys):
            tree.GetEntry(3*itoy)
            if not getattr(tree,'quantileExpected')==-1: 
                raiseFailError(itoy,True) 
                continue
            bf = getattr(tree, 'r')
            tree.GetEntry(3*itoy+1)
            # if not abs(getattr(tree,'quantileExpected')--0.32)<0.001: ##-- Is there a reason this is "--" ? If not, what is the purpose of this condition? Wouldn't this remove any small best fit values? 
            #     raiseFailError(itoy,True) 
            #     continue
            lo = getattr(tree, 'r')
            tree.GetEntry(3*itoy+2)
            # if not abs(getattr(tree,'quantileExpected')--0.32)<0.001: 
            if not abs(getattr(tree,'quantileExpected')-0.32)<0.001: 
                raiseFailError(itoy,True) 
                continue
            hi = getattr(tree, 'r')
            diff = bf - opts.expectSignal
            unc = 0.5 * (hi-lo)
            if unc > 0.: 
                pullHist.Fill(float(diff/unc))
        canv = r.TCanvas()
        pullHist.Draw()
        if opts.gaussianFit:
           print("Doing gaussian fit")
           r.gStyle.SetOptFit(111)

           ##-- User function 
           initial_mu, initial_sig = 0., 2.
        #    f1 = r.TF1("f1", "gaus", initial_mu, initial_sig)
           f1 = r.TF1("f1", "gaus")
           f1.SetParameter(0, 0.) ##-- constant 
           f1.SetParameter(1, initial_mu) ##-- average 
           f1.SetParameter(2, initial_sig) ##-- sig 
           pullHist.Fit("f1")
        #    pullHist.Fit("f1", "R")
           
           ##-- Default Gaussian
        #    pullHist.Fit('gaus')
        canv.SaveAs('%s%s.pdf'%(opts.outputDirectory, plotName(name)))
        canv.SaveAs('%s%s.png'%(opts.outputDirectory, plotName(name)))
