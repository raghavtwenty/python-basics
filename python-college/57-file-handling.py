'''
Simulate a bank account supporting opening/closing, withdrawals, and deposits of money. 
Watch out for concurrent transactions!
                        author @raghav
Date Created : 10 March 2022 | Last Updated : 11 March 2022
                        MINI  PROJECT
'''


# Importing required libraries
import ast


''' 
--------------RUN FOR THE FIRST TIME
# Code for file creation 
# transactions file
Initial_Dict = dict()
with open('transactions.txt','w') as t_file:
    t_file.write(str(Initial_Dict))

# user details
with open('account_details.txt','w') as ad_file:
    ad_file.write(str(Initial_Dict))
--------------END
'''


# Creating user defined functions

# ad = account details
# td = transactions details

# read account details file
def read_ad():
    with open('account_details.txt','r') as raf:
        reader = raf.read() # read as str
        dic = ast.literal_eval(reader) #convert to dictionary 
        return dic

# write account details file
def write_ad(dic):
    with open('account_details.txt','w') as waf:
                waf.write(str(dic)) # write into the same file

# read transactions details fil
def read_td():
    with open('transactions.txt','r') as rtd:
        raf_reader = rtd.read() # read as str
        raf_dic = ast.literal_eval(raf_reader) #convert to dictionary 
        return raf_dic

# write transactions details file
def write_td(dic):
    with open('transactions.txt','w') as wtd:
                wtd.write(str(dic)) # write into the same file

#----- END of all read and write -----


# account creation
def account_creation():
    name = str(input('Enter your name : '))
    user_name = str(input('Enter your username : '))
    passcode = str(input('Enter your new passcode : '))
    ph = int(input('Enter your phone number : '))

    # account details file
    # read the contents of the account details file and new user
    dic = read_ad()

    if not user_name in dic.keys():    #Check if account exists
        dic[user_name] = [passcode,name,ph] #append new account data
        write_ad(dic)

        # Create transaction account with 0 balance
        trans_dic = read_td()
        trans_dic[user_name] = [0]
        write_td(trans_dic)

        print("\nAccount Created Sucessfully")
    else:
        print('\nAccount already exists')


# login 
def login():

    global pc
    global un

    un = str(input('Enter your username : '))
    pc = str(input('Enter your new passcode : '))

    dic = read_ad()
    if un in dic.keys():
        if pc == dic.get(un)[0]:
            print('\nAccess Granted\n')

        else :
            print('\nIncorrect passcode\n')
            pc = un = False
        
    else: 
        print('\nAccount doesnt exist.')
        pc = un = False


# transactions
def trans(un):
    print('\nTransaction History\n')
    tr_read = read_td()
    dum = tr_read.get(un)
    for i in dum:
        print(i)

    print(f'\nNet Balance : {sum(dum)}\n')


# deposit money
def deposit(un):
    d_read = read_td()
    depo = int(input('Enter The deposit amount : '))
    if depo > 0:
        depo_trans = d_read.get(un)
        depo_trans.append(depo)
        d_read[un] = depo_trans

        write_td(d_read)
        print('\nAmount added to your main balance.\n')

    else:
        print('\nDeposit amount must be greater than 0.\n')


# withdraw
def withdraw(un):
    w_read = read_td()
    withdraw_det = w_read.get(un)

    withdr_amt = int(input('Enter The withdraw amount : '))
   
    if withdr_amt< sum(withdraw_det):
        withdraw_det.append(int(-withdr_amt))
        w_read[un] = withdraw_det
        write_td(w_read)
        print('\nAmount withdrawed from your main balance.\n')

    else:
        print('\nDeposit amount must be less than net balance.\n')
    

#close account
def close_account(un,pc):

    pwd = str(input('Enter your account passcode : '))
    if pwd == pc :
        # delete account in account details file
        dic = read_ad()
        dic.pop(un)
        write_ad(dic)
        print('\nAccount details had been cleared.')

        # delete transaction history
        trans_dic = read_td()
        trans_dic.pop(un)
        write_td(trans_dic)
        print('\nAccount permanently deleted.\n')
    else :
        print('\nAccess denied.')


# MAIN
print('\nMINI PROJECT : Bank account simulation.\n')
flag = 0
while (flag != 7):
    print('''
MENU
1 - Create new account
2 - login
3 - View transactions history
4 - Deposit money
5 - Withdraw money
6 - Close account
7 - Quit''')

    flag = int(input('\nEnter your choice : '))

    if flag == 1:
        account_creation()

    elif flag == 2:
        login()

    elif flag == 3:
        try:
            trans(un)
        except NameError:
            print('\nPlease login.\n')
        
    elif flag == 4:
        try:
            deposit(un)
        except NameError:
            print('\nPlease login.\n')
    
    elif flag == 5:
        try:
            withdraw(un)
        except NameError:
            print('\nPlease login.\n')

    elif flag == 6:
        try:
            close_account(un,pc)
        except NameError:
            print('\nPlease login.\n')

    else:
        flag == 0