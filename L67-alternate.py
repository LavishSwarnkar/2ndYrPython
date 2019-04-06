import re
p1 = r"^['\"]{3}\w*"
p2 = r"\w*['\"]{3}$"
p3 = r"^#{1}\w*"
f1 = open("in.py", mode="r")
f2 = open("out.py", mode="w")
script=""
multiline=False
lines = f1.readlines()
print(lines)
for line in lines:
    if re.match(p1, line):
        multiline = True
    elif multiline:
        continue
    elif re.match(p2, line):
        multiline = False
    elif re.match(p3, line):
        continue
    else:
        script += line
f2.write(script)
f1.close()
f2.close()
print("in.py copied to out.py without comments!")
