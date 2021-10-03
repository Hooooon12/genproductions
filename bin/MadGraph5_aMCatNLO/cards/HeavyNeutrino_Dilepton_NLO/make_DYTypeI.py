import os

basedir = os.getcwd() + "/"
basename = "DYTypeI_NLO"
basename_tmp = "skeletons_DYTypeI_NLO/DYTypeI_NLO"

os.system("mkdir -p " + basedir + basename)

#masses = [70, 75, 85, 90, 95, 100, 125, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700, 2000]
#channels = ["EMu", "EE", "MuMu", "MuE"]
#masses = [85, 90, 95, 100, 125, 150, 200, 250, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700, 2000]
masses = [2200, 2500, 2700, 3000]
channels = ["SF","DF"]
#channels = ["DF"]

mixing_SF = {'ven1' : 0.01, 'ven2' : 0., 'vmun1' : 0., 'vmun2' : 0.01}
mixing_DF = {'ven1' : 0.01, 'ven2' : 0., 'vmun1' : 0.01, 'vmun2' : 0.}

with open("skeletons_DYTypeI_NLO/DYTypeI_templateNLO_customizecards.dat", "r") as f1:
  customizecards = f1.read()
with open("skeletons_DYTypeI_NLO/DYTypeI_templateNLO_proc_card.dat", "r") as g1:
  proc_card = g1.read()
with open("skeletons_DYTypeI_NLO/DYTypeI_templateNLO_extramodels.dat", "r") as h1:
  extramodels = h1.read()
with open("skeletons_DYTypeI_NLO/DYTypeI_templateNLO_run_card.dat", "r") as i1:
  run_card = i1.read()
with open("skeletons_DYTypeI_NLO/DYTypeI_templateNLO_madspin_card.dat", "r") as j1:
  madspin_card = j1.read()


for mass in masses:

  for channel in channels:
    
    output = "output " + basename + "_" + channel + "_M" + str(mass) + " --nojpeg"

    os.mkdir(basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))

    if mass < 80: 

      process = ["generate p p > l n1 [QCD]", "generate p p > e n1 [QCD]\nadd process p p > mu n2 [QCD]"]
      decay = ["set spinmode none\n\ndecay n1 > l j j", "set spinmode none\n\ndecay n1 > e j j\ndecay n2 > mu j j"]

      if channel == "DF":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f2:
          f2.write(customizecards.format(mass=mass, ven1=mixing_DF['ven1'], ven2=mixing_DF['ven2'], vmun1=mixing_DF['vmun1'], vmun2=mixing_DF['vmun2']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g2:
          g2.write(proc_card.format(process=process[0], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h2:
          h2.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i2:
          i2.write(run_card)

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j2:
          j2.write(madspin_card.format(decay=decay[0]))

      if channel == "SF":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f3:
          f3.write(customizecards.format(mass=mass, ven1=mixing_SF['ven1'], ven2=mixing_SF['ven2'], vmun1=mixing_SF['vmun1'], vmun2=mixing_SF['vmun2']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g3:
          g3.write(proc_card.format(process=process[1], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h3:
          h3.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i3:
          i3.write(run_card)

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j3:
          j3.write(madspin_card.format(decay=decay[1]))


      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_customizecards.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_proc_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_extramodels.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_run_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_madspin_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))



    elif mass > 80:
      
      process = ["generate p p > l n1 [QCD]", "generate p p > e n1 [QCD]\nadd process p p > mu n2 [QCD]"]
      decay = ["decay n1 > w l, w > j j", "decay n1 > w e, w > j j\ndecay n2 > w mu, w > j j"]

      if channel == "DF":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f2:
          f2.write(customizecards.format(mass=mass, ven1=mixing_DF['ven1'], ven2=mixing_DF['ven2'], vmun1=mixing_DF['vmun1'], vmun2=mixing_DF['vmun2']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g2:
          g2.write(proc_card.format(process=process[0], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h2:
          h2.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i2:
          i2.write(run_card)

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j2:
          j2.write(madspin_card.format(decay=decay[0]))

      if channel == "SF":

        with open(basename_tmp + "_{0}_M{1}_customizecards.dat".format(channel, mass), "w") as f3:
          f3.write(customizecards.format(mass=mass, ven1=mixing_SF['ven1'], ven2=mixing_SF['ven2'], vmun1=mixing_SF['vmun1'], vmun2=mixing_SF['vmun2']))

        with open(basename_tmp + "_{0}_M{1}_proc_card.dat".format(channel, mass), "w") as g3:
          g3.write(proc_card.format(process=process[1], output=output))

        with open(basename_tmp + "_{0}_M{1}_extramodels.dat".format(channel, mass), "w") as h3:
          h3.write(extramodels)

        with open(basename_tmp + "_{0}_M{1}_run_card.dat".format(channel, mass), "w") as i3:
          i3.write(run_card)

        with open(basename_tmp + "_{0}_M{1}_madspin_card.dat".format(channel, mass), "w") as j3:
          j3.write(madspin_card.format(decay=decay[1]))


      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_customizecards.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_proc_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_extramodels.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_run_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))
      os.system("mv " + basedir + basename_tmp + "_{0}_M{1}_madspin_card.dat ".format(channel, mass) + basedir + basename + "/" + basename + "_{0}_M{1}".format(channel, mass))


