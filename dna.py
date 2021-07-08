
class InputError(Exception):
    pass
import pandas as pd
import sys
if len(sys.argv) != 3:
    try:
        raise InputError
    finally:
        print("Error. Please provide database and sequence")
database=str(sys.argv[1])
sequence=str(sys.argv[2])
dat=pd.read_csv(database)
with open(sequence,'r') as dna_file:
    dna_strand=dna_file.read()
checker=dat.columns.values.tolist()
checker.pop(0)
for i in checker:
    count   = 0
    pattern = i
    while pattern in dna_strand:
        count += 1
        pattern += i
    dat=dat[dat[i]==count]
if dat.empty :
    print("No match")
else:
    name=dat.iloc[0,0]
    print(str(name))
