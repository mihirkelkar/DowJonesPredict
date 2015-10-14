#In this file, I will rad in the final json, take out data that does not make much sense and
#add dummy variables for logistic regression. 

import json
import datetime
import time

final_data = list()

def read_data():
  global final_data
  with open('final.json', 'r') as outfile:
    data = json.load(outfile)
  for ii in data:
    if len(data[ii].keys()) == 6:
      temp_list = list()
      temp_list.append(time.mktime(datetime.datetime.strptime(ii, "%Y-%m-%d").timetuple()))
      temp_list.append(data[ii]['dow'])
      temp_list.append(data[ii]['nikkie'])
      temp_list.append(data[ii]['sci'])
      temp_list.append(data[ii]['eur'])
      temp_list.append(data[ii]['yuan'])
      temp_list.append(data[ii]['gold'])
      if data[ii]['dow'] > 0:
        temp_list.append(1)
      else:
        temp_list.append(0)
      final_data.append(temp_list)  
      #print final_data

def write_data():
  global final_data
  clean = open('../clean-data/data.csv', 'w')
  clean.write("timestamp,dow,nikkie,sci,eur,yuan,gold,target\n")
  for ii in final_data:
    print ii
    clean.write(",".join([str(jj) for jj in ii]))
    clean.write("\n")
  clean.close()
  
read_data()
write_data()
