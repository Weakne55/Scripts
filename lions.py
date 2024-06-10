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

# Start values from 1st line
start_peak = df.values[0][1]
name_TF = df.values[0][3].split('.')[0]
len_TF = df.values[0][10].split(',')[1]
start_TF = df.values[0][11].split(',')[1]
p = df.values[0][13]

# Start arrays for peaks 
pval = [p]
pos = [start_TF]
lens = [len_TF]
name = [name_TF]

# template for lines draw
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

# lines processing
for i in range(1,len(df.values)):
        if df.values[i][1] != start_peak:
                print(' '.join(tmp)) # print last processed line if we got new start cordinate

                # update line values
                start_peak = df.values[i][1]
                name_TF = df.values[i][3].split('.')[0]
                len_TF = df.values[i][10].split(',')[1]
                start_TF = df.values[i][11].split(',')[1]
                p = df.values[i][13]
                
                # update line array
                pval = [p]
                pos = [start_TF]
                lens = [len_TF]
                name = [name_TF]
        
                # update line template
                tmp = [ df.values[i][0],
                        str(df.values[i][1]),
                        str(df.values[i][2]),
                        '.'.join(name), 
                        ".",
                        str(df.values[i][5]),
                        str(df.values[i][6]),
                        str(df.values[i][7]),
                        "255,0,0",
                        str(3),
                        "1,"+",".join(lens)+",1",
                         "0,"+",".join(pos)+","+str( df.values[i][2] - df.values[i][1] - 1 ),
                        ".",
                        str(sum(pval))]
                if i == len(df.values)-1:
                        print(" ".join(tmp))

        else:
                start_TF = df.values[i][11].split(',')[1]
                name_TF = df.values[i][3].split('.')[0]
                len_TF = df.values[i][10].split(',')[1]
                p = df.values[i][13]
                
                for j in range(len(pos)):
                        if start_TF < pos[j]:
                                pos.insert(j,start_TF)
                                lens.insert(j,len_TF)
                                name.insert(j,name_TF)
                                pval.insert(j,p)

                tmp = [ df.values[i][0],
                        str(df.values[i][1]),
                        str(df.values[i][2]),
                        '.'.join(name), 
                        ".",
                        ".",
                        "0",
                        "0",
                        "255,0,0",
                        str(2+len(pos)),
                        "1,"+",".join(lens)+",1",
                         "0,"+",".join(pos)+","+str( df.values[i][2] - df.values[i][1] - 1 ),
                        ".",
                        str(sum(pval))]
