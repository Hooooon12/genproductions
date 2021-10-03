import os

basedir = os.getcwd() + "/"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut5"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut5"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut10"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut10"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut15"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut15"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut20"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_ptcut20"
basename = "HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO"
basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Schannel_V0p1_NLO"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_V0p1_NLO"
#basename = "HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_NNPDF30"
#basename_tmp = "skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_NNPDF30"

ptcut = '0.0' if not basename[-1].isdigit() else filter(str.isdigit, basename)
#masses = [40, 300, 800]
#masses = [15, 20, 30, 40, 50, 60, 65, 70, 75, 85, 90, 95, 100, 125, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
masses = [100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
channels = ["EMu", "EE", "MuMu", "MuE"]
mixing_EMu = {'ven1' : 1.000000e-02, 'vmun1' : 1.000000e-02}
mixing_MuE = {'ven1' : 1.000000e-02, 'vmun1' : 1.000000e-02}
mixing_EE = {'ven1' : 1.000000e-02, 'vmun1' : 0.000000e+00}
mixing_MuMu = {'ven1' : 0.000000e+00, 'vmun1' : 1.000000e-02}
#mixing_EMu = {'ven1' : 1.000000e-01, 'vmun1' : 1.000000e-01}
#mixing_MuE = {'ven1' : 1.000000e-01, 'vmun1' : 1.000000e-01}
#mixing_EE = {'ven1' : 1.000000e-01, 'vmun1' : 0.000000e+00}
#mixing_MuMu = {'ven1' : 0.000000e+00, 'vmun1' : 1.000000e-01}

if 'Schannel' in basename:
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_templateNLO_customizecards.dat", "r") as f1:
    customizecards = f1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_templateNLO_proc_card.dat", "r") as g1:
    proc_card = g1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_templateNLO_extramodels.dat", "r") as h1:
    extramodels = h1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_templateNLO_run_card.dat", "r") as i1:
    run_card = i1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_templateNLO_madspin_card.dat", "r") as j1:
    madspin_card = j1.read()

elif 'Tchannel' in basename:
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_templateNLO_customizecards.dat", "r") as f1:
    customizecards = f1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_templateNLO_proc_card.dat", "r") as g1:
    proc_card = g1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_templateNLO_extramodels.dat", "r") as h1:
    extramodels = h1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_templateNLO_run_card.dat", "r") as i1:
    run_card = i1.read()
  with open("skeletons_NLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_templateNLO_madspin_card.dat", "r") as j1:
    madspin_card = j1.read()


for mass in masses:

  for channel in channels:
    
    output = "output " + basename + "_" + channel + "_M" + str(mass) + " --nojpeg"

    os.mkdir(basedir + basename + "_{0}_M{1}".format(channel, mass))

    if mass < 80: 

      if 'Schannel' in basename:
        process = ["generate p p > e n1 [QCD]", "generate p p > mu n1 [QCD]", "generate p p > e n1 [QCD]", "generate p p > mu n1 [QCD]"]
      if 'Tchannel' in basename:
        process = ["generate p a > n1 e j [QCD]\nadd process a p > n1 e j [QCD]", "generate p a > n1 mu j [QCD]\nadd process a p > n1 mu j [QCD]", "generate p a > n1 e j [QCD]\nadd process a p > n1 e j [QCD]", "generate p a > n1 mu j [QCD]\nadd process a p > n1 mu j [QCD]"]
      
      decay = ["set spinmode none\n\ndecay n1 > mu j j", "set spinmode none\n\ndecay n1 > e j j", "set spinmode none\n\ndecay n1 > e j j", "set spinmode none\n\ndecay n1 > mu j j"]

      if channel == "EMu":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f2:
          f2.write(customizecards.format(mass=mass, ven1=mixing_EMu['ven1'], vmun1=mixing_EMu['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g2:
          g2.write(proc_card.format(process=process[0], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h2:
          h2.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i2:
          i2.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j2:
          j2.write(madspin_card.format(decay=decay[0]))

      if channel == "MuE":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f3:
          f3.write(customizecards.format(mass=mass, ven1=mixing_MuE['ven1'], vmun1=mixing_MuE['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g3:
          g3.write(proc_card.format(process=process[1], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h3:
          h3.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i3:
          i3.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j3:
          j3.write(madspin_card.format(decay=decay[1]))

      elif channel == "EE":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f4:
          f4.write(customizecards.format(mass=mass, ven1=mixing_EE['ven1'], vmun1=mixing_EE['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g4:
          g4.write(proc_card.format(process=process[2], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h4:
          h4.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i4:
          i4.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j4:
          j4.write(madspin_card.format(decay=decay[2]))

      elif channel == "MuMu":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f5:
          f5.write(customizecards.format(mass=mass, ven1=mixing_MuMu['ven1'], vmun1=mixing_MuMu['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g5:
          g5.write(proc_card.format(process=process[3], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h5:
          h5.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i5:
          i5.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j5:
          j5.write(madspin_card.format(decay=decay[3]))



      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_customizecards.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_proc_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_extramodels.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_run_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_madspin_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))



    elif mass >= 80:
      
      if 'Schannel' in basename:
        process = ["generate p p > e n1 [QCD]", "generate p p > mu n1 [QCD]", "generate p p > e n1 [QCD]", "generate p p > mu n1 [QCD]"]
      if 'Tchannel' in basename:
        process = ["generate p a > n1 e j [QCD]\nadd process a p > n1 e j [QCD]", "generate p a > n1 mu j [QCD]\nadd process a p > n1 mu j [QCD]", "generate p a > n1 e j [QCD]\nadd process a p > n1 e j [QCD]", "generate p a > n1 mu j [QCD]\nadd process a p > n1 mu j [QCD]"]
      decay = ["decay n1 > w mu, w > j j", "decay n1 > w e, w > j j", "decay n1 > w e, w > j j", "decay n1 > w mu, w > j j"]

      if channel == "EMu":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f2:
          f2.write(customizecards.format(mass=mass, ven1=mixing_EMu['ven1'], vmun1=mixing_EMu['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g2:
          g2.write(proc_card.format(process=process[0], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h2:
          h2.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i2:
          i2.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j2:
          j2.write(madspin_card.format(decay=decay[0]))

      if channel == "MuE":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f3:
          f3.write(customizecards.format(mass=mass, ven1=mixing_MuE['ven1'], vmun1=mixing_MuE['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g3:
          g3.write(proc_card.format(process=process[1], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h3:
          h3.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i3:
          i3.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j3:
          j3.write(madspin_card.format(decay=decay[1]))

      elif channel == "EE":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f4:
          f4.write(customizecards.format(mass=mass, ven1=mixing_EE['ven1'], vmun1=mixing_EE['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g4:
          g4.write(proc_card.format(process=process[2], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h4:
          h4.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i4:
          i4.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j4:
          j4.write(madspin_card.format(decay=decay[2]))

      elif channel == "MuMu":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f5:
          f5.write(customizecards.format(mass=mass, ven1=mixing_MuMu['ven1'], vmun1=mixing_MuMu['vmun1']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g5:
          g5.write(proc_card.format(process=process[3], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h5:
          h5.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i5:
          i5.write(run_card.format(ptcut=ptcut))

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j5:
          j5.write(madspin_card.format(decay=decay[3]))



      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_customizecards.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_proc_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_extramodels.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_run_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_madspin_card.dat ".format(channel, mass) + basedir + basename + "_{0}_M{1}".format(channel, mass))


