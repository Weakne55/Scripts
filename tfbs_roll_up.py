#python3 lions.py file.gappedPeak > output.gappedPeak
# lines should be sorted by first coordinate 

# Test data
# NC_007117.7 32092540 32094280 FOXD3.H12CORE.1.S.B . - 32093696 32093716 255,0,0 3 1,20,1 0,1156,1739 . 4.3283806192717105
# NC_007117.7 32092540 32094280 MITF.H12CORE.0.P.B . + 32093873 32093884 255,0,0 3 1,11,1 0,1333,1739 . 6.622659904607587
# NC_007117.7 43386520 43387930 FOXD3.H12CORE.1.S.B . - 43387168 43387188 255,0,0 3 1,20,1 0,648,1409 . 4.717298853387327
# NC_007117.7 43386520 43387930 MITF.H12CORE.0.P.B . - 43386847 43386858 255,0,0 3 1,11,1 0,327,1409 . 4.389671220464675
# NC_007117.7 43391600 43392580 FOXD3.H12CORE.1.S.B . - 43391949 43391969 255,0,0 3 1,20,1 0,349,979 . 4.855581129278044
# NC_007117.7 43450120 43450740 FOXD3.H12CORE.1.S.B . + 43450606 43450626 255,0,0 3 1,20,1 0,486,619 . 4.354296101502011

# Test output
# NC_007117.7 32092540 32094280 FOXD3.MITF . . 0 0 255,0,0 4 1,20,11,1 0,1156,1333,1739 . 10.951040523879298
# NC_007117.7 43386520 43387930 MITF.FOXD3 . . 0 0 255,0,0 4 1,11,20,1 0,327,648,1409 . 9.106970073852
# NC_007117.7 43391600 43392580 FOXD3 . - 43391949 43391969 255,0,0 3 1,20,1 0,349,979 . 4.855581129278044
# NC_007117.7 43450120 43450740 FOXD3 . + 43450606 43450626 255,0,0 3 1,20,1 0,486,619 . 4.354296101502011

# code must be optimized but i don`t have enough time :(

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
start_peak = int(df.values[0][1])
init_name_TF = df.values[0][3].split('.')[0]
init_len_TF = int(df.values[0][10].split(',')[1])
init_start_TF = int(df.values[0][11].split(',')[1])
init_p = float(df.values[0][13])

# Start arrays for peaks 
pval = [init_p]
pos = [init_start_TF]
lens = [init_len_TF]
name = [init_name_TF]

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
                "1,"+",".join(list(map(str,lens)))+",1",
                 "0,"+",".join(list(map(str,pos)))+","+str( df.values[0][2] - df.values[0][1] - 1 ),
                ".",
                str(sum(pval))]

# lines processing
for i in range(1,len(df.values)):
        if int(df.values[i][1]) != start_peak:
                print('\t'.join(tmp)) # print last processed line if we got new start cordinate

                # update line values
                start_peak = int(df.values[i][1])
                name_TF = df.values[i][3].split('.')[0]
                len_TF = int(df.values[i][10].split(',')[1])
                start_TF = int(df.values[i][11].split(',')[1])
                p = float(df.values[i][13])
                
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
                        "1,"+",".join(list(map(str,lens)))+",1",
                         "0,"+",".join(list(map(str,pos)))+","+str( df.values[i][2] - df.values[i][1] - 1 ),
                        ".",
                        str(sum(pval))]
                
        else:
                #print(df.values[i])
                start_TF = int(df.values[i][11].split(',')[1])
                name_TF = df.values[i][3].split('.')[0]
                len_TF = int(df.values[i][10].split(',')[1])
                p = float(df.values[i][13])

                #print(start_TF,name_TF,len_TF,p,sep='\t',end='\n')     
                #print(pos,lens,name,pval,sep='\n',end='\n')

                for j in range(len(pos)):
                        if start_TF < pos[j]:
                                pos.insert(j,start_TF)
                                lens.insert(j,len_TF)
                                name.insert(j,name_TF)
                                pval.insert(j,p)
                                break
                else:
                        pos.append(start_TF)
                        lens.append(len_TF)
                        name.append(name_TF)
                        pval.append(p)

                
                
                #print(pos,lens,name,pval,sep='\n',end='\n')

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
                        "1,"+",".join(list(map(str, lens)))+",1",
                         "0,"+",".join(list(map(str,pos)))+","+str( df.values[i][2] - df.values[i][1] - 1 ),
                        ".",
                        str(sum(pval))]

        if i == len(df.values)-1:
                print("\t".join(tmp))
