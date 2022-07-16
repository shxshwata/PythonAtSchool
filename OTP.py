# Write a program to genrate an OTP

import random
digits='0123456789'
otp=''
for i in range(4):
    d=random.choice(digits)
    otp+=d
print('OTP generated ',otp)

    
    
    
