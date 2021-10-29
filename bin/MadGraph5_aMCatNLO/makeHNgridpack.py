import os

#masses = ["85","90","95","100","125","150","200","250","300","400","600","700","800","900","1100","1200","1300","1700","2000"]
#masses = ["600","1000","1200","750","2000","3000","5000"]
#masses = ["10000","15000","20000"]
#masses = ["750", "5000"]
masses = ["15000"]
channels = ["SF_top"]
#channels = ["SF_V0p1"]
#channels = ["DF"]
#channels = ["SF","DF","MuMu"]
#channels = ["SF","DF"]
#channels = ["MuMu"]
#processes = ["DY","VBF","SSWW"]
processes = ["SSWW"]

for process in processes:
  for channel in channels:
    for mass in masses:
      os.system("./MakeGridpack.sh "+process+" "+channel+" "+mass)
