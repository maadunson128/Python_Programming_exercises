#Program: Adding interest rates to a many accounts

def interestAdd(account, rate)-> None:
    #accpunt = [1, 2, 3, 4] #it wont change the outer variable balance
    for i in range(len(account)):
        account[i] = account[i] * (1+ rate)#reassigning will reflect on the balance variable.
        


    
def account_info()->None:
    #List containning account balances.
    balance:list[float] = [1000, 503, 200, 2002]
    rate:float = 0.06
    
    interestAdd(balance, rate)
    print(f"Account balances: {balance}")


account_info()
    


'''

Note:
In python , if we pass immutable objects, it act as 'pass by value' and if we change
the value of the parameter inside the function , it wont change.

If we pass mutable objects, it will act as 'pass by reference' and if we modify it inside the function,
it will reflect on the variable outside the function also.
If we try to reassign it, iot won't reflect any changes in the variable outside the function.
'''
    
