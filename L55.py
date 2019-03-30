import re
str1 = "Today is 30-03-2019 or 30/03/2019 or 30/3/19"
p = r"\d{1,2}[-/]{1}\d{1,2}[-/]{1}\d{2,4}"
print("Dates found are:", re.findall(p, str1))
