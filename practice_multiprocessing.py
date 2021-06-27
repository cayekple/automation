import multiprocessing
import subprocess
import os

dest = ''
def sync_file(file):
  subprocess.call(['rsync','-avz', file, dest])

for root, dirs, files from os.walk(directory):
  pool = multiprocessing.Pool(multiprocessing.cpu_count())
  pool.map(sync_file, dirs)


#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
from os import walk 
src= "/home/user/data/"
dest="/home/user/data/backup/"
def backupData(dir):    
  print("dir = "+ src+dir +" dest = " + dest+dir)    
  subprocess.call(["rsync", "-arq", src+dir, dest+dir]) 
dirList = []
for (root, dirs, files) in walk(src):    
  dirList.extend(dirs)    
  break;
  print (dirList)
  p= Pool(len(dirList))
  p.map(backupData, dirList)