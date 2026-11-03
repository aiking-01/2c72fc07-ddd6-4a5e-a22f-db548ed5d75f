with open('schools.csv')as f:
  code = list(csv.reader(f))
  for i in code[2:]:
    if i[0][0]=='F':
      print(*i[5:7])
