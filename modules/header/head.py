
def header(mesg = None):
    width = 170
    commission_name = 'Maharashtra Legislative Assembly Election 2024'
    conducted = 'Conducted by State Election Commission'
    head = '-' * width
    print(f'{head} \n {commission_name.center(width)} \n {conducted.center(width)} ')
    if mesg:
        print(mesg.center(width))
    print(head)

