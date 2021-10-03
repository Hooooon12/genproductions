import os

masses = ["600","800","1000","1200","1400","1600","1800","2000","2200","2400","2600","2800","3000","3200","3400","3600","3800","4000","4200","4400","4600","4800","5000"]

for mass in masses:
  os.system("./MakeZprimeGridpack.sh "+"ZprimetoNN_EEJJJJ_Zprime{0}_N150_WR5000_NLO".format(mass))
