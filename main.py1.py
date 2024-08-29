import Accounts
import ATM

Account1 = Accounts.Accounts(account_number = 123456,account_firstname= "Royce",
                             account_lastname= "chua",current_balance = 1000,
                             address = " silver street quezon city", 
                             email = "roycechua123@gmai.com")
print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)



print()



Account2 = Accounts.Accounts(account_number= 654321,account_firstname= "John",
                             account_lastname= "doe",current_balance = 2000,
                             address = " Golden Street Quezon City", 
                             email = "johndoe@yahoo.com")

print('Account2')
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)