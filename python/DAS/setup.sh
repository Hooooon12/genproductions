#!/bin/bash
CURDIR=$PWD
export SCRAM_ARCH=slc7_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_0_2/src ] ; then 
 echo release CMSSW_10_0_2 already exists
else
scram p CMSSW CMSSW_10_0_2
fi
cd CMSSW_10_0_2/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
cp $CURDIR/DY0j_MLM_fragment.py Configuration/GenProduction/python/

scram b
cd ../../
seed=$(($(date +%s) % 100 + 1))


HadronizerPATH=Configuration/GenProduction/python/DY0j_MLM_fragment.py
OutputPATH=DAS_MG_EXERCISE.root
PythonName=DAS_MG_EXERCISE.py
NEVENT=5000



cmsDriver.py ${HadronizerPATH} --fileout file:${OutputPATH} --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 100X_upgrade2018_realistic_v10 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --geometry DB:Extended --era Run2_2018 --python_filename ${PythonName} --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n ${NEVENT} 
