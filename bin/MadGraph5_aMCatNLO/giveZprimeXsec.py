import commands as cmd

def Xsec(x):
  items = x.split()
  for item in items:
    try:
      x = float(item)
      break
    except ValueError:
      pass
  return str(x)

ls = cmd.getoutput('ls | grep N150_WR5000 | grep log')
files = ls.split('\n')

files.sort(key = lambda f : int(filter(str.isdigit, f)))
with open("Zprime_Xsec.txt",'w') as txt: 
  txt.write("ZMass\tNmass\tXsec(pb)\n")
  for File in files:
    with open(File, 'r') as f:
      lines = f.readlines()
    for line in lines:
      if 'section: ' in line and not 'section:  ' in line: 
        txt.write(filter(str.isdigit,File.split('_')[2])+'\t'+filter(str.isdigit,File.split('_')[3])+'\t'+Xsec(line)+'\n')
