EXT="stage1_1_2016"
#EXT="stage1_1_2017"
#EXT="stage1_1_2018"
OUTDIR="outdir_${EXT}"

if [ ! -d "Signal/$OUTDIR" ]; then
  echo "Signal/$OUTDIR doesn't exist, maybe your EXT is wrong? Exiting..."
  exit 1
fi

cd Plots/FinalResults/Inputs/$EXT
ls ../../../../Signal/$OUTDIR/CMS-HGG_*sigfit*oot  > tmp.txt
while read p;
do
q=$(basename $p)
cp $p ${q/$EXT/mva} 
echo " cp $p ${q/$EXT/mva} "
done < tmp.txt
echo "cp ../../../../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}.root CMS-HGG_mva_13TeV_sigfit.root"
cp ../../../../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}.root CMS-HGG_mva_13TeV_sigfit.root
echo "cp ../../../../Background/CMS-HGG_multipdf_${EXT}${FAKE}.root CMS-HGG_mva_13TeV_multipdf${FAKE}.root"
cp ../../../../Background/CMS-HGG_multipdf_${EXT}${FAKE}.root CMS-HGG_mva_13TeV_multipdf${FAKE}.root
echo "cp ../../../../Datacard/Datacard_13TeV_$EXT.txt CMS-HGG_mva_13TeV_datacard.txt"
cp ../../../../Datacard/Datacard_13TeV_$EXT.txt CMS-HGG_mva_13TeV_datacard.txt
