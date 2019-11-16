import os
import re
import sys
from sys import argv
from pathlib import Path

if len(argv)<2:
    print("No path given")
    sys.exit(1)
    
path = argv[1]
new_path = str(Path(path).parent)+"/new_"+os.path.basename(path)

if not os.path.exists(new_path):
    os.mkdir(new_path)
    
for dirr in os.listdir(path):
    cur_path  = path+"/"+dirr
    
    for file in os.listdir(cur_path):
        count = 1
        with open(cur_path+"/"+file,'r', encoding='utf-8') as f:
            doc_pattern = re.compile(r'<doc.*?>(.*?)<\/doc>', re.S)
            tag_pattern = re.compile(r'<.*?>.*?<\/.*?>')
            for txt in doc_pattern.findall(f.read()):
                if not os.path.exists(new_path+"/new_"+dirr):
                    os.mkdir(new_path+"/new_"+dirr)
                new_f = open(new_path+"/new_"+dirr+"/"+file+"_"+str(count)+".txt", 'w', encoding='utf-8')
                txt1 = re.sub(r'\n{2,}', '\n', txt)
                txt2 = re.sub(r'()', '', txt1)
                new_f.write(re.sub(tag_pattern, '', txt2))
                new_f.close()
                count += 1