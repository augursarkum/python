ro = open("balance.txt","r")
balance = ro.read(99999)
ro.close()
balance = int(balance)
print("Welcome to ATM App")
while(True):
  print("1. Check Balance")
  print("2. Withdraw Amount")
  print("3. Deposit Amount")
  print("4. Exit")
  option = int(input("Enter the options: "))
  if(option == 1):
    print("The balance is ", balance)
  elif(option == 2):
    withdraw = int(input("Enter the amount to withdraw: "))
    ro = open("balance.txt","w")
    ro.write(str(balance - withdraw))
    ro.close()
    balance = balance - withdraw
    print("The balance is: ",balance)
  elif(option == 3):
    deposit = int(input("Enter the amount to deposit: "))
    ro = open("balance.txt","w")
    ro.write(str(balance + deposit))
    ro.close()
    balance = balance + deposit
    print("The balance is: ",balance)

  elif(option == 4):
    quit()
  else:
    print("invalid option")
  print("------------------------------")

