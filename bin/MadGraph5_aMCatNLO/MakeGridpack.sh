#!/bin/bash

PROCESSNAME=$1
CARDPATH=/data2/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/cards/production/13TeV/HeavyNeutrino_Dilepton_NLO/DYTypeI_NLO/${1}

echo "PROCESSNAME=$PROCESSNAME"
echo "CARDPATH=$CARDPATH"

if [ ! -e $CARDPATH ]
then
    echo "No $CARDPATH... Exiting..."
    exit 1
fi

SCRIPT=MG_MakeGridpack_${PROCESSNAME}.sh
echo "#!/bin/bash" > $SCRIPT
echo time env -i 'HOME=$HOME' bash -l -c \"source /cvmfs/cms.cern.ch/cmsset_default.sh\; ./gridpack_generation.sh $PROCESSNAME cards/production/13TeV/HeavyNeutrino_Dilepton_NLO/DYTypeI_NLO/$PROCESSNAME\" >>$SCRIPT
chmod +x $SCRIPT

nohup ./MG_MakeGridpack_${PROCESSNAME}.sh &
