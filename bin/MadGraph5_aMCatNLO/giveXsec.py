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

ls = commands.getoutput('ls')
files = ls.split('\n')
logfiles = [[],[],[],[]]
channels = ['MuMu','EMu','EE','MuE']

for File in files:
	#if '.log' in File:
	if '.log' in File and 'Majorana' in File and not 'V0p1' in File:
		if 'MuMu' in File:
			logfiles[0].append(File)
		if 'EMu' in File:
			logfiles[1].append(File)
		if 'EE' in File:
			logfiles[2].append(File)
		if 'MuE' in File:
			logfiles[3].append(File)

for i in range(4):
	logfiles[i].sort(key = lambda f : int(filter(str.isdigit, f)))
	with open("NLO_Xsec{0}.txt".format(channels[i]),'w') as txt: 
		txt.write("Mass\tXsec(pb) for {0}\n".format(channels[i]))
		for logfile in logfiles[i]:
				with open(logfile, 'r') as f:
					lines = f.readlines()
				for line in lines:
					#if 'Cross-section' in line:
					if 'section: ' in line and not 'section:  ' in line: 
						txt.write(filter(str.isdigit,logfile)+'\t'+Xsec(line)+'\n')

#for i in range(len(logfiles)):
#	logfiles[i].sort(key = lambda f : int(filter(str.isdigit, f)))
#	for logfile in logfiles[i]:
#		with open(logfile, 'r') as f:
#			lines = f.readlines()
#		for line in lines:
#			#if 'Cross-section' in line:
#			if 'section: ' in line and not 'section:  ' in line: 
#				print logfile, line[:-1]
