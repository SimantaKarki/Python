import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "hellokarki@gmail.com"
pattern2 = re.compile(r"(")
a = pattern.search(string)
print(a)

# at least 8 character
# contain any numbers character,$%#@
# has to end with number