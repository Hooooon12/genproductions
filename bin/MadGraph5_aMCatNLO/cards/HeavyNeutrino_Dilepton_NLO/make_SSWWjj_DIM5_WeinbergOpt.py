import os

basedir = os.getcwd() + "/"
basename = "SSWWjj_DIM5_WeinbergOpt"

os.system("mkdir -p " + basedir + basename)

#channels = ["EE","EMu","ETau","MuMu","MuTau","TauTau"]
channels = ["ETau","MuTau","TauTau"]

wilsons = {}
wilsons['EE'] = 0
wilsons['EMu'] = 0
wilsons['ETau'] = 0
wilsons['MuMu'] = 0
wilsons['MuTau'] = 0
wilsons['TauTau'] = 0

with open("skeletons_SSWWjj_DIM5_WeinbergOpt/SSWWjj_DIM5_WeinbergOpt_templateNLO_customizecards.dat", "r") as f1:
  customizecards = f1.read()
with open("skeletons_SSWWjj_DIM5_WeinbergOpt/SSWWjj_DIM5_WeinbergOpt_templateNLO_proc_card.dat", "r") as g1:
  proc_card = g1.read()
with open("skeletons_SSWWjj_DIM5_WeinbergOpt/SSWWjj_DIM5_WeinbergOpt_templateNLO_extramodels.dat", "r") as h1:
  extramodels = h1.read()
with open("skeletons_SSWWjj_DIM5_WeinbergOpt/SSWWjj_DIM5_WeinbergOpt_templateNLO_run_card.dat", "r") as i1:
  run_card = i1.read()
with open("skeletons_SSWWjj_DIM5_WeinbergOpt/SSWWjj_DIM5_WeinbergOpt_templateNLO_FKS_params.dat", "r") as j1:
  FKS_params = j1.read()


process = {}
process['EE']     = "generate p p > e+ e+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > e- e- j j QED=4 QCD=0 $$ w+ w- [QCD]"
process['EMu']    = "generate p p > e+ mu+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > e- mu- j j QED=4 QCD=0 $$ w+ w- [QCD]"
process['ETau']   = "generate p p > e+ ta+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > e- ta- j j QED=4 QCD=0 $$ w+ w- [QCD]"
process['MuMu']   = "generate p p > mu+ mu+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > mu- mu- j j QED=4 QCD=0 $$ w+ w- [QCD]"
process['MuTau']  = "generate p p > mu+ ta+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > mu- ta- j j QED=4 QCD=0 $$ w+ w- [QCD]"
process['TauTau'] = "generate p p > ta+ ta+ j j QED=4 QCD=0 $$ w+ w- [QCD]\nadd process p p > ta- ta- j j QED=4 QCD=0 $$ w+ w- [QCD]"

for channel in channels:
  
  wilsons[channel] = 1

  output = "output " + basename + "_" + channel + " -nojpeg"

  os.system("mkdir -p " + basedir + basename + "/" + basename + "_{0}".format(channel))

  outdir = basedir+basename+"/"+basename+"_"+channel

  with open(outdir+"/"+basename+"_{0}_customizecards.dat".format(channel), "w") as f2:
    f2.write(customizecards.format(cee=wilsons['EE'],cem=wilsons['EMu'],cet=wilsons['ETau'],cmm=wilsons['MuMu'],cmt=wilsons['MuTau'],ctt=wilsons['TauTau']))
  with open(outdir+"/"+basename+"_{0}_proc_card.dat".format(channel), "w") as g2:
    g2.write(proc_card.format(process=process[channel], output=output))
  with open(outdir+"/"+basename+"_{0}_extramodels.dat".format(channel), "w") as h2:
    h2.write(extramodels)
  with open(outdir+"/"+basename+"_{0}_run_card.dat".format(channel), "w") as i2:
    i2.write(run_card)
  with open(outdir+"/"+basename+"_{0}_FKS_params.dat".format(channel), "w") as j2:
    j2.write(FKS_params)

  # reset
  wilsons[channel] = 0
