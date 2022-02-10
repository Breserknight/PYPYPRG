import shutil
import os
import zipfile
import re

result = []

pattern = r'\d{3}-\d{3}-\d{4}'

dirt = os.getcwd()+'\\extracted_content\\Five\\AEITMYIRQLP.txt'

f = open(dirt, 'r')
if re.search("ursus tortorcura", f.read()):
    result.append(re.search("ursus tortorcura", f.read()))
print(result)