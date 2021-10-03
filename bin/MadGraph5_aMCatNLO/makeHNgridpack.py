import os

#masses = ["85","90","95","100","125","150","200","250","300","400","600","700","800","900","1100","1200","1300","1700","2000"]
#masses = ["600","700","800","900","1000","1100","1200","1300","1500","1700","2000"]
masses = ["300"]
#channels = ["SF"]
channels = ["DF"]

for channel in channels:
  for mass in masses:
    os.system("./MakeGridpack.sh "+"DYTypeI_NLO_{0}_M{1}".format(channel, mass))
    #os.system("./MakeGridpack.sh "+"VBFTypeI_NLO_{0}_M{1}".format(channel, mass))
