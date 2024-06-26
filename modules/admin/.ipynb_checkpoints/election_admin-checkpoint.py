max_retry = 3
def verify_cred():
    user_name = input('enter your username : ')
    pswd = int(input('enter your login password : '))
    for i in range(max_retry):
        if user_name == 'tejas' and pswd == 123:
            print(f'Hey {user_name} you are ADMIN....')
        else:
            print('Please enter the valid credentials')
    return False
        