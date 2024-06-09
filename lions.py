import sys
import pandas as pd
import numpy as np

path=sys.argv[1]
df = pd.read_csv(path,header=None,sep='\t')
#print(df)

#for row in df.rows():

#print(df.columns)
#print(df.index) 
#print(df.values)
start_peak = df.values[0][1]
name_TF = df.values[0][3].split('.')[0]
len_TF = df.values[0][10].split(',')[1]
start_TF = df.values[0][11].split(',')[1]
pval = [df.values[0][13]]
pos = [start_TF]
lens = [len_TF]
name = [name_TF]

tmp = [ df.values[0][0],
                str(df.values[0][1]),
                str(df.values[0][2]),
                '.'.join(name), 
                ".",
                str(df.values[0][5]),
                str(df.values[0][6]),
                str(df.values[0][7]),
                "255,0,0",
                str(2+len(pos)),
                "1,"+",".join(lens)+",1",
                 "0,"+",".join(pos)+","+str( df.values[0][2] - df.values[0][1] - 1 ),
                ".",
                str(sum(pval))]

#print("\t".join(tmp))

for i in range(1,len(df.values)):
        if df.values[i][1] != start_peak:
                print('\t'.join(tmp))
                start_peak = df.values[i][1]
        else:
                chr = df.values[i][0] 
                end_peak = df.values[i][2] 
