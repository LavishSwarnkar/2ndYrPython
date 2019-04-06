f1 = open("files\\in.txt", mode="r")
f2 = open("files\\out.txt", mode="w")
txt = f1.read()[::-1]
f2.write(txt)
f1.close()
f2.close()
print("in.txt copied to out.txt in reverse order!")
