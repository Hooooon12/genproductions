#!/bin/bash

PROCESSNAME=$1
CHANNEL=$2
MASS=$3
FULLNAME=${1}TypeI_NLO_${2}_M${3}
#CARDPATH=/data2/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/cards/production/13TeV/HeavyNeutrino_Dilepton_NLO/DYTypeI_NLO/${1}
CARDPATH=/data2/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/cards/HeavyNeutrino_Dilepton_NLO/${1}TypeI_NLO/${FULLNAME}
#CARDPATH=/data2/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/cards/HeavyNeutrino_Dilepton_NLO/VBFTypeI_NLO/${1} #JH : XXX change here

echo "PROCESSNAME=$FULLNAME"
echo "CARDPATH=$CARDPATH"

if [ ! -e $CARDPATH ]
then
    echo "No $CARDPATH... Exiting..."
    exit 1
fi

SCRIPT=MG_MakeGridpack_${FULLNAME}.sh
echo "#!/bin/bash" > $SCRIPT
#echo time env -i 'HOME=$HOME' bash -l -c \"source /cvmfs/cms.cern.ch/cmsset_default.sh\; ./gridpack_generation.sh $PROCESSNAME cards/production/13TeV/HeavyNeutrino_Dilepton_NLO/DYTypeI_NLO/$PROCESSNAME\" >>$SCRIPT
echo time env -i 'HOME=$HOME' bash -l -c \"source /cvmfs/cms.cern.ch/cmsset_default.sh\; ./gridpack_generation.sh $FULLNAME cards/HeavyNeutrino_Dilepton_NLO/${1}TypeI_NLO/$FULLNAME\" >>$SCRIPT
#echo time env -i 'HOME=$HOME' bash -l -c \"source /cvmfs/cms.cern.ch/cmsset_default.sh\; ./gridpack_generation.sh $PROCESSNAME cards/HeavyNeutrino_Dilepton_NLO/VBFTypeI_NLO/$PROCESSNAME\" >>$SCRIPT #JH XXX : change here
chmod +x $SCRIPT

nohup ./MG_MakeGridpack_${FULLNAME}.sh &
