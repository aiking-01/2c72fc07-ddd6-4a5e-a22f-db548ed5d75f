with open('schools.csv')as f:
 for i in list(csv.reader(f))[2:]:
  if i[0][0]=='F':print(*i[5:7])