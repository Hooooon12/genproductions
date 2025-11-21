import commands

def Xsec(x):
  items = x.split()
  for item in items:
    try:
      x = float(item)
      break
    except ValueError:
      pass
  return str(x)

def findBR(process,mass,channel): #put mass, channel
  print 'finding BR for:',process,mass,channel
  if float(mass) < 80: #for the low mass
    param_card = '/data8/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/Schannel_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_{0}_M{1}/HeavyMajoranaNeutrino_SSDiLepton_Schannel_NLO_{2}_M{3}_gridpack/work/gridpack/process/Cards/param_card.dat'.format(channel, mass, channel, mass)
    with open(param_card,'r') as param_card:
      Lines = param_card.readlines()
    for Line in Lines[:]: #you must make a 'copy' of the iterated list to modify it
      Line = Line.split()
      if not 'BR' in Line: del Lines[0]
      else : break
    BR = 0
    if channel == 'EE' or channel == 'MuMu':
      for n in range(4):
        BRs = Lines[n+1].split()
        #print BRs[0]
        BR += float(BRs[0])
        print 'total BR:',BR

    if channel == 'EMu':
      if float(mass) < 70:
        for n in [1,2,5,6]: 
          BRs = Lines[n].split()
          #print BRs[0]
          BR += float(BRs[0])
          print 'total BR:',BR
      else:
        for n in [1,2,7,8]: 
          BRs = Lines[n].split()
          #print BRs[0]
          BR += float(BRs[0])
          print 'total BR:',BR

    if channel == 'MuE':
      if float(mass) < 70:
        for n in [3,4,7,8]:
          BRs = Lines[n].split()
          #print BRs[0]
          BR += float(BRs[0])
          print 'total BR:',BR
      else:
        for n in [3,4,5,6]:
          BRs = Lines[n].split()
          #print BRs[0]
          BR += float(BRs[0])
          print 'total BR:',BR
    ######################### The BR order is different depending on mass range... You don't worry if using EE(MuMu) only. Emu, MuE may be problamatic
  else:
    logfile = '/data2/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/{0}_NLO_DF_M{1}.log'.format(process,mass)
    with open(logfile,'r') as logfile:
      Lines = logfile.readlines()
    for Line in Lines[:]:
      Line = Line.split()
      if not 'BR' in Line: del Lines[0]
      else : break

    BR = float(Lines[1].split()[1])*(2./3.)
    print 'total BR for',process,mass,':',BR

  return BR


ls = commands.getoutput('ls')
files = ls.split('\n')
logfiles = {'DYTypeI':[],'VBFTypeI':[]}

masses = ["M85","M90","M95","M100","M125","M150","M200","M250","M300","M350","M400","M450","M500","M600","M700","M800","M900","M1000","M1100","M1200","M1300","M1500","M1700","M2000","M2500","M3000","M5000","M7500","M10000","M15000","M20000","M25000","M30000","Weinberg"]
processes = ['DYTypeI','VBFTypeI']
channels = ['EE']

for File in files:
  for proc, mass in [(proc, mass) for proc in processes for mass in masses]:
    if proc+"_NLO_DF_"+mass+".log" in File:
      if 'DYTypeI' in File:
        logfiles['DYTypeI'].append(File)
      if 'VBFTypeI' in File:
        logfiles['VBFTypeI'].append(File)

for proc in processes:
  for ch in channels: #you'd better not to use 'for channel in channels~' because of the overlap of the definitions
    logfiles[proc].sort(key = lambda f : int(filter(str.isdigit, f)))

    with open("{0}_NLO_Xsec{1}_BRmultiplied.txt".format(proc,ch),'w') as txt: 
      txt.write("Mass\tXsec(pb) for {0} (BR applied)\n".format(ch))

      for logfile in logfiles[proc]:
          with open(logfile, 'r') as f:
            lines = f.readlines()
          for line in lines:
            if 'section: ' in line and not 'section:  ' in line:
              this_mass = filter(str.isdigit,logfile)
              txt.write(this_mass+'\t'+str(float(Xsec(line))*findBR(proc,this_mass,ch))+'\n')

    with open("{0}_NLO_Xsec{1}_BRmultiplied_ForSKFlat.txt".format(proc,ch),'w') as txt: 
      txt.write("Mass\tXsec(pb) for {0} (BR applied, V=1, *8)\n".format(ch))

      for logfile in logfiles[proc]:
          with open(logfile, 'r') as f:
            lines = f.readlines()
          for line in lines:
            if 'section: ' in line and not 'section:  ' in line:
              this_mass = filter(str.isdigit,logfile)
              txt.write(this_mass+'\t'+str(float(Xsec(line))*findBR(proc,this_mass,ch)*10000.*8)+'\n')
