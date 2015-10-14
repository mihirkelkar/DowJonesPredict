import json

write_data = {}

def read_dow_json(filename, index_name):
  global write_data
  with open(filename, 'r') as infile:
    data = json.load(infile)
  #columns = data['dataset']['column_names']
  data = data['dataset']['data']
  print len(data)
  for ii in data:
    try:
      write_data[ii[0]][index_name] = ii[4]
    except:
      write_data[ii[0]] = {}
      write_data[ii[0]][index_name] = ii[4]
  print index_name + " Written"


def read_currency(filename, index_name):
  global write_data
  with open(filename, 'r') as infile:
    data = json.load(infile)
  data = data['dataset']['data']
  for ii in data:
    try:
      write_data[ii[0]][index_name] = ii[1]
    except:
      write_data[ii[0]] = {}
      write_data[ii[0]][index_name] = ii[1]
  print index_name + "Currency written" 


def write_to_json(filename):
  global write_data
  
  with open(filename, 'w') as outfile:
    json.dump(write_data, outfile, indent = 4)
 
read_dow_json('dow_data.json', "dow")
read_dow_json('nikkie_225.json', 'nikkie')
read_dow_json('shanghai_composite.json', 'sci')
read_currency('dollar_vs_eur.json', 'eur')
read_currency('dollar_vs_yuan.json', 'yuan')
read_currency('gold.json', 'gold')
write_to_json('final.json')
