#Program : Balance update with interest

def interest_add(amount:float, rate:float)->float:
    new_balance:float = amount + amount * rate
    amount = new_balance
    return amount
    


    
def account_show()->None:

    #balance and rate of interest
    balance:float = 1000
    rate:float = 0.05

    balance = interest_add(balance, rate)
    print(f"New account balance: {balance}")


account_show()


'''
Note:
    Python passess parameters by value. It doesn't have access to the variable.
'''
