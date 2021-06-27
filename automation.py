#! /usr/bin/env python3

import os
import requests

def list_files(directory):
  for file in os.listdir(directory):
    file_dict = {}
    with open(directory+file, 'r') as f:
      n = 0
      feedback = ['title','name','date','feedback']
      for line in f:
        file_dict[feedback[n]] = line.replace('\n','')
        n += 1
    save_feedback(file_dict)
    

def save_feedback(feedback):
  return requests.post('http://35.193.70.50/feedback', feedback)


list_files('/data/feedback/')
