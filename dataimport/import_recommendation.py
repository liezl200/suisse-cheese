import csv
with open('output.txt', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|', \
    dialect=csv.excel_tab)
  for row in reader:
  	print 'UPDATE companies SET cadf_score="' + row[2] + \
  	'" ,recommendation="'+ row[3] + \
  	'" WHERE symbol= "' + row[0] + \
  	'" AND country= "' + row[1] +\
  	'" ;'