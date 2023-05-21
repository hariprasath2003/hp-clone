user_name ="john smith"
password = 2023

m = input("enter a username")
n = int(input("enter a password"))
if user_name ==  m and  password == n:
    print("password is correct")
    print("login successfully")
elif  user_name != m and password != n:
    print("password is wrong")
    print("login failed")
else:
    print("better luck nxt time")
