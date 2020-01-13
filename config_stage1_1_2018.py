# Config file: options for combine fitting

_year = '2018'

combineScriptCfg = {
  
  # Setup
  'mode':'datacard',
  #'inputWSDir':'/vols/cms/jl2117/hgg/ws/Jan20/stage1_1_%s'%_year, 
  'inputWSDir':'/vols/cms/es811/HggGeneral/WorkspaceTest/Pass1/%s/ws'%_year, 
  #Procs will be inferred automatically from filenames
  'cats':'RECO_0J_PTH_0_10_Tag0,RECO_VBFTOPO_JET3VETO_LOWMJJ,RECO_0J_PTH_0_10_Tag1,RECO_GE2J_PTH_0_60_Tag1,RECO_1J_PTH_0_60_Tag0,RECO_0J_PTH_GT10_Tag0,RECO_VBFTOPO_JET3VETO_HIGHMJJ,RECO_GE2J_PTH_60_120_Tag1,RECO_VBFTOPO_BSM,RECO_GE2J_PTH_120_200_Tag1,RECO_1J_PTH_0_60_Tag1,RECO_GE2J_PTH_60_120_Tag0,RECO_1J_PTH_60_120_Tag1,RECO_GE2J_PTH_0_60_Tag0,RECO_VBFTOPO_JET3_HIGHMJJ,RECO_1J_PTH_60_120_Tag0,RECO_GE2J_PTH_120_200_Tag0,RECO_1J_PTH_120_200_Tag1,RECO_1J_PTH_120_200_Tag0,RECO_PTH_GT200_Tag0,RECO_PTH_GT200_Tag1,RECO_VBFTOPO_VHHAD,RECO_VBFLIKEGGH,RECO_0J_PTH_GT10_Tag1,RECO_VBFTOPO_JET3_LOWMJJ',
  'ext':'stage1_1_%s'%_year,
  'year':'%s'%_year,
  'signalProcs':'all',

  # Add UE/PS systematics to datacard (only relevant if mode == datacard)
  'doUEPS':0,

  #Photon shape systematics  
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB',
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB',
  'scalesGlobal':'NonLinearity:UntaggedTag_0:2,Geant4',
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho',

  # Job submission options
  'batch':'IC',
  'queue':'hep.q',

  'printOnly':0 # For dry-run: print command only
  
}
