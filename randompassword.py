import random
import string
pass_len=int(input())
Charvalue= string.ascii_letters+ string.digits+ string.punctuation

Password=" "
for i in range(pass_len):
  Password += random.choice(Charvalue)

print("your random password is",Password)
  
