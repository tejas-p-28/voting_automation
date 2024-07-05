
def user_input(ch,max_exp_input):
    max_retry = 3
    for i in range(max_retry):
        ch = int(input('enter your choice : '))
        if ch in range(max_exp_input+1):
            return ch
        else:
            print('ERROR : Invalid Input')
    print('ERROR : Maximum Retries Exceeded')