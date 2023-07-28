uname = 'Admin'
pwd  = "admin123"
attemp=0
while True:
    attemp+=1
    print(f'Attempt{attemp} of 3')
    username=input('enter the username:')
    password=input('enter the password:')
    if attemp==3:
        print('to many attemptsas')
        break
    if username!=uname:
        print("Invalid Username")
    if password!=pwd:
        print('invalid password')
    if username==uname and password==pwd:
        print('Login Successful')
        break