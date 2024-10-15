import os

#masses = ["85","90","95","100","125","150","200","250","300","400","600","700","800","900","1100","1200","1300","1700","2000"]
#masses = ["600","1000","1200","750","2000","3000","5000"]
#masses = ["10000","15000","20000"]
#masses = ["1250", "1750", "7500"]
#masses = ["25000", "30000"]
#masses = ["800"]
#masses = ["500","600","700","800","900","1000","1100","1200","1300","1700","2000","2500","3000","10000","15000","20000"]
#masses = ["500","600","700","800","900","1000","1100","1200"]
#masses = ["1300","1700","2000","2500"]
#masses = ["3000","10000","15000","20000"]
masses = ["40000","50000","60000","70000","80000","90000","100000"]
#channels = ["SF_top"]
#channels = ["SF_V0p1"]
#channels = ["DF"]
#channels = ["SF","DF","MuMu"]
channels = ["SF","DF"]
#channels = ["EE"]
#channels = ["MuMu"]
#channels = ["MupMup","MumMum"]
#processes = ["DY","VBF","SSWW"]
processes = ["SSWW"]
#processes = ["VBF"]

for process in processes:
  for channel in channels:
    for mass in masses:
      os.system("./MakeGridpack.sh "+process+" "+channel+" "+mass)
