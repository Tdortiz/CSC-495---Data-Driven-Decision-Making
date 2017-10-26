import os
import sys
#from pathlib import Path
import glob
import subprocess

script_dir = str(os.path.abspath(__file__ + "/../"))
medicare_path = os.path.join(script_dir, "csv/preprocessed")
print("medicare_path\t= " + str(medicare_path))
model_output = os.path.join(script_dir, 'hospitalRanking/temp-models/models.py')
print("model_output\t= " + str(model_output))


with open(model_output, 'a') as out:
    for csv_file in glob.glob( os.path.join(medicare_path, '*.csv') ):
        print(str(csv_file))
        out.write("#Imported from : " + str(csv_file) + "\n")
        subprocess.call(["python", "manage.py", "inspectcsv", str(csv_file)], stdout=out)
        out.write("\n\n") 
