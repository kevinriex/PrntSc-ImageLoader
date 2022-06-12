import random as rnd
import string
import os

base_url = "https://prnt.sc/"

x = 0

while x < 10:
    x = x + 1
    y = 0
    code = "".join(rnd.choice(string.ascii_lowercase + string.digits) for _ in range(6))
    print(base_url + code)

os.system("pause")
