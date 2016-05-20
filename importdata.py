import csv
with open('companydata2.txt', 'rU') as csvfile:
  reader = csv.reader(csvfile, delimiter='\t', quotechar='|', dialect=csv.excel_tab)
  c = 0 # row counter in csv
  i = 1 # id counter for SQL code

  for row in reader:
    # print column names
    if c == 9:
      types = row[1:]
    if c == 10:
      col_names = row[1:]
      print "CREATE TABLE companies ("
      for col_num in range (0, len(col_names)):
        print col_names[col_num].replace('"', ' ') + " " + types[col_num].replace('"', ' ') + ","
        pass
      print "\n\n"
    if c == 10:
      print "\n\n"
    if c > 11 and c <= 4041:
      company_data = row[1:]
      found_bad_data = False
      for col_num in range(0, len(company_data)):
        if company_data[col_num] == "NA" and ((col_num > 2 and col_num < 23) or (col_num > 30)):
          found_bad_data = True
      if found_bad_data:
        continue # skip row
      print 'INSERT INTO companies VALUES ("' + str(i) + '", '
      for col_num in range (0, len(col_names)):
          print '"' + company_data[col_num].replace('"', "") + '"',
          if col_num < len(col_names) - 1:
            print', ',
      print ");"
      print "\n\n"
      i += 1

    c += 1

