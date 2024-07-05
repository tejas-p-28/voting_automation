from modules.u_input import u_input
def first_screen():
    choice = ['Admin','Voter','Exit']
    for i,j in enumerate(choice,1):
        print(f'{i}. {j}')
    return u_input.user_input('enter your choice : ',3)