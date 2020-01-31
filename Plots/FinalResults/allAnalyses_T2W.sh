text2workspace.py allAnalyses.txt -o allAnalyses.root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 higgsMassRange=122,128 \
--PO "map=.*/ggH_0J_PTH_0_10_hgg:r_ggH_0J_low[1,0,4]" \
--PO "map=.*/ggH_0J_PTH_GT10_hgg:r_ggH_0J_high[1,0,2]" \
--PO "map=.*/ggH_1J_PTH_0_60_hgg:r_ggH_1J_low[1,0,4]" \
--PO "map=.*/ggH_1J_PTH_60_120_hgg:r_ggH_1J_med[1,0,4]" \
--PO "map=.*/ggH_1J_PTH_120_200_hgg:r_ggH_1J_high[1,0,4]" \
--PO "map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60_hgg:r_ggH_2J_low[1,0,4]" \
--PO "map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120_hgg:r_ggH_2J_med[1,0,4]" \
--PO "map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200_hgg:r_ggH_2J_high[1,0,4]" \
--PO "map=.*/ggH_PTH_GT200_hgg:r_ggH_BSM[1,0,4]" \
--PO "map=.*/ggH_GE2J_MJJ_350_700_.*_hgg:r_ggH_VBFlike[1,0,6]" \
--PO "map=.*/ggH_GE2J_MJJ_GT700_.*_hgg:r_ggH_VBFlike[1,0,6]" \
--PO "map=.*/qqH_GE2J_.*_PTH_0_200_PTHJJ_0_25_hgg:r_qqH_2Jlike[1,0,4]" \
--PO "map=.*/qqH_GE2J_.*_PTH_0_200_PTHJJ_GT25_hgg:r_qqH_3Jlike[1,0,4]" \
--PO "map=.*/qqH_GE2J_.*_PTH_GT200_hgg:r_qqH_BSM[1,0,4]" \
--PO "map=.*/WH_had_GE2J_.*_PTH_0_200_PTHJJ_0_25_hgg:r_qqH_2Jlike[1,0,4]" \
--PO "map=.*/WH_had_GE2J_.*_PTH_0_200_PTHJJ_GT25_hgg:r_qqH_3Jlike[1,0,4]" \
--PO "map=.*/WH_had_GE2J_.*_PTH_GT200_hgg:r_qqH_BSM[1,0,4]" \
--PO "map=.*/ZH_had_GE2J_.*_PTH_0_200_PTHJJ_0_25_hgg:r_qqH_2Jlike[1,0,4]" \
--PO "map=.*/ZH_had_GE2J_.*_PTH_0_200_PTHJJ_GT25_hgg:r_qqH_3Jlike[1,0,4]" \
--PO "map=.*/ZH_had_GE2J_.*_PTH_GT200_hgg:r_qqH_BSM[1,0,4]" \
--PO "map=.*/qqH_GE2J_MJJ_60_120_hgg:r_qqH_VHhad[1,0,6]" \
--PO "map=.*/WH_had_GE2J_MJJ_60_120_hgg:r_qqH_VHhad[1,0,6]" \
--PO "map=.*/ZH_had_GE2J_MJJ_60_120_hgg:r_qqH_VHhad[1,0,6]" \
--PO "map=.*/WH_lep.*hgg:r_WH_lep[1,0,6]" \
--PO "map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]" \
--PO "map=.*/ttH.*hgg:r_ttH[1,0,4]" \
--PO "map=.*/tHq.*hgg:r_tH[1,0,10]" \
--PO "map=.*/tHW.*hgg:r_tH[1,0,10]"
