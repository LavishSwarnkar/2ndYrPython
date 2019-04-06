import re
p1 = r"['\"]{3}[\w\s]*['\"]{3}"
p2 = r"\s*#{1}[\w\s]*\s+"
f1 = open("files\\in.py", mode="r")
f2 = open("files\\out.py", mode="w")
script = f1.read()
script = re.sub(p1, "", script)
script = re.sub(p2, "", script)
f2.write(script)
f1.close()
f2.close()
print("in.py copied to out.py without comments!")