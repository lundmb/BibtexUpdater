#!/usr/bin/env python

import sys
maxauthor=3
bibtexfile=sys.argv[1]
bibtexoutput=sys.argv[2]
g = open('myfile','w')
abbrevs=[]
with open("BibtexUpdate_Macros.dat") as Macros:
   for line in Macros:
      abbrevs.append(line[:-1].split(";"))


with open(bibtexfile) as f:
   for line in f:
      if line.startswith('author'):
         temp=line.split(" and ")
         #print temp, len(temp)
         if len(temp) <= maxauthor:
            pass
         else:
            #print line
            line=temp[0]
            for author in temp[1:maxauthor]:
               line=line+' and '+author
            line=line+' and others},\n'
            #print line
      if line.startswith('journal'):
         #print line
         for x in abbrevs:
            line=line.replace('{'+x[1]+'}','{\\'+x[0]+'}')
         print line
      g.write(line)

g.close()
