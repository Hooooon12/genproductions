import commands

def findBR(mass,channel): #put mass, channel
  print 'finding BR for:',mass,channel
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
  
  elif 80 < float(mass) <= 90 : #before Z decay
    logfile = '/data8/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/Schannel_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_{0}_M{1}.log'.format(channel, mass)
    with open(logfile,'r') as logfile:
      Lines = logfile.readlines()
    for Line in Lines[:]:
      Line = Line.split()
      if not 'BR' in Line: del Lines[0]
      else : break

    if channel == 'EE' or channel == 'MuMu':
      BR = 4*float(Lines[1].split()[1])*float(Lines[7].split()[1])
      print 'total BR:',BR

    if channel == 'EMu' or channel == 'MuE':
      BR = 4*float(Lines[1].split()[1])*float(Lines[9].split()[1]) 
      print 'total BR:',BR

  elif 90 < float(mass) <= 125 : #before Higgs decay
    logfile = '/data8/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/Schannel_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_{0}_M{1}.log'.format(channel, mass)
    with open(logfile,'r') as logfile:
      Lines = logfile.readlines()
    for Line in Lines[:]:
      Line = Line.split()
      if not 'BR' in Line: del Lines[0]
      else : break

    if channel == 'EE' or channel == 'MuMu':
      BR = 4*float(Lines[1].split()[1])*float(Lines[9].split()[1])
      print 'total BR:',BR

    if channel == 'EMu' or channel == 'MuE':
      BR = 4*float(Lines[1].split()[1])*float(Lines[13].split()[1]) 
      print 'total BR:',BR

  elif 125 < float(mass) : #for the high mass
    logfile = '/data8/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/Schannel_NLO/HeavyMajoranaNeutrinoToDiLepton_Schannel_NLO_{0}_M{1}.log'.format(channel, mass) #Schannel
    #logfile = '/data8/Users/jihkim/genproductions/bin/MadGraph5_aMCatNLO/HeavyMajoranaNeutrinoToDiLepton_Tchannel_NLO_{0}_M{1}.log'.format(channel, mass) #Tchannel
    with open(logfile,'r') as logfile:
      Lines = logfile.readlines()
    for Line in Lines[:]:
      Line = Line.split()
      if not 'BR' in Line: del Lines[0]
      else : break

    if channel == 'EE' or channel == 'MuMu':
      BR = 4*float(Lines[1].split()[1])*float(Lines[11].split()[1])
      print 'total BR:',BR

    if channel == 'EMu' or channel == 'MuE':
      BR = 4*float(Lines[1].split()[1])*float(Lines[17].split()[1]) 
      print 'total BR:',BR

  return BR

ls = commands.getoutput('ls')
files = ls.split('\n')
Xsecfiles = [[],[],[],[]]

for File in files:
  if 'Xsec' in File and 'NLO' in File and not 'Tch' in File and not 'BR' in File and not 'py' in File: #not S(T)ch when calculating T(S)channel xsec
    if 'MuMu' in File:
      Xsecfiles[0].append(File)
    if 'EMu' in File:
      Xsecfiles[1].append(File)
    if 'EE' in File:
      Xsecfiles[2].append(File)
    if 'MuE' in File:
      Xsecfiles[3].append(File)

channels = ['MuMu','EMu','EE','MuE']

for i in range(4): #you'd better not to use 'for channel in channels~' because of the overlap of the definitions
  with open("NLO_Xsec{0}_BRmultiplied.txt".format(channels[i]),'w') as txt: 
    txt.write("Mass\tXsec(pb) for {0} (BR applied)\n".format(channels[i]))
    for Xsecfile in Xsecfiles[i]:
        with open(Xsecfile, 'r') as f:
          lines = f.readlines()
        for line in lines:
          mass_Xsec = line.split('\t')
          try: float(mass_Xsec[0])
          except ValueError: pass
          else: txt.write(mass_Xsec[0]+'\t'+str(float(mass_Xsec[1])*findBR(mass_Xsec[0],channels[i]))+'\n')


