with open("decode.txt","w")as d:
 with open("readme.txt","r")as f:d.write(decode(f.read()))