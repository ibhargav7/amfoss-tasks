import string
import codecs
a='667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268'
b=codecs.decode(a,"hex")
c=[]
for i in b:
   c.append(chr(ord(i)^10))
def shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i)-3)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)-3)%26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i)-3)%10])
    return n

print(shift(c))