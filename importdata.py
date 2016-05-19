import csv
with open('companydata2.csv', 'rU') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|', dialect=csv.excel_tab)
  c = 0 # row counter in csv
  i = 1 # id counter for SQL code
  # column names on row 10 (c = 9)
  # labels on row 11 (c = 10)
  for row in reader:
    # print column names
    if c == 9:
      print ', '.join(row)
      print "\n\n"
    if c == 10:
      print ', '.join(row)
      print "\n\n"
    if c > 11 and c <= 4040:
      print len(row)
      print ', '.join(row)
      print "\n\n"
      i += 1

    c += 1

