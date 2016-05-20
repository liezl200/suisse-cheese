import csv
with open('companydata2.txt', 'rU') as csvfile:
  reader = csv.reader(csvfile, delimiter='\t', quotechar='|', \
    dialect=csv.excel_tab)

  row_ct = 0 # row counter in csv
  id_ct = 1 # id counter for SQL code

  for row in reader:

    # Form the CREATE TABLE statement using the first two usable rows
    if row_ct == 9:
      types = row[1:]
    if row_ct == 10:
      col_names = row[1:]
      print "CREATE TABLE companies ("
      for col_num in range (0, len(col_names)):
        print col_names[col_num].replace('"', ' ') + " " + \
          types[col_num].replace('"', ' ') + ","
        pass
      print "\n\n"

    # Form the INSERT INTO statements using the following rows
    if row_ct > 11 and row_ct <= 4041:
      company_data = row[1:]

      # Skip malformed data
      found_bad_data = False
      for col_num in range(0, len(company_data)):
        if company_data[col_num] == "NA" and ((col_num > 2 and col_num < 23) \
          or (col_num > 30)):
          found_bad_data = True
      if found_bad_data:
        continue # skip row

      # Generate "INSERT INTO" SQL statements for each company
      print 'INSERT INTO companies VALUES ("' + str(i) + '", '
      for col_num in range (0, len(col_names)):
          print '"' + company_data[col_num].replace('"', "") + '"',
          if col_num < len(col_names) - 1:
            print', ',
      print ");"
      print "\n\n"
      id_ct += 1 # increment SQL id counter
    row_ct += 1 # increment row counter

