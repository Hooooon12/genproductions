import commands as cmd

def Xsec(x,channel):
  items = x.split()
  for item in items:
    try:
      x = float(item)
      break
    except ValueError:
      pass
  if channel == "MuMu":
    return str(x/2.)
  elif channel == "EMu":
    return str(x*10000)

ls = cmd.getoutput('ls | grep SSWW | grep log')
files = ls.split('\n')
logfiles = [[],[]]
channels = ['MuMu','EMu']

for File in files:
  if '.log' in File and not 'V0p1' in File:
    if 'SF' in File:
      logfiles[0].append(File)
    if 'DF' in File:
      logfiles[1].append(File)

for i in range(2):
  logfiles[i].sort(key = lambda f : int(filter(str.isdigit, f)))
  with open("SSWWTypeI_NLO_Xsec_{0}.txt".format(channels[i]),'w') as txt:
    txt.write("Mass\tXsec(pb) for {0} (V==1)\n".format(channels[i]))
    for logfile in logfiles[i]:
        with open(logfile, 'r') as f:
          lines = f.readlines()
        for line in lines:
          if 'section: ' in line and not 'section:  ' in line:
            txt.write(filter(str.isdigit,logfile)+'\t'+Xsec(line,channels[i])+'\n')
