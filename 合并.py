import pandas as pd
for inputfile in os.listdir(inputfile_dir):
    pd.read_csv(inputfile, header=None)
    pd.to_csv(outputfile, mode='a', index=False, header=False)