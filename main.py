#ONE MILLION!!
#ONE MILLION!!
#ONE MILLION!!
#ONE MILLION!!

import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(100000):
    password = password + random.choice(characters)

print(password)
