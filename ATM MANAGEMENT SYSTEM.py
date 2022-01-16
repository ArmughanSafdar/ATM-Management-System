print("\n\n----------WELCOME TO ATM MANAGEMENT SYSTEM----------\n\n")

import getpass

users = ['user1', 'user2', 'user3']
pins = ['1234', '2345', '3456']
amounts = [3000, 3000, 3000]
count = 0

while True:
	user = input("Enter Username: ")
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print("Invalid Username!")

while count < 3:
	pin = str(getpass.getpass("\nEnter Your Password: "))
	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print("Invalid Password!")
				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print("Invalid Password!")
				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print("Invalid Password!")
				print()
	else:
		print("Password must consist of 4 digits:")
		count += 1
	
if count == 3:
	print("3 WRONG ATTEMPTS!\nYOUR CARD HAS BEEN LOCKED!\nEXITING")
	exit()

print("\nLogged In Successfully!\n")
print()

# Main menu

while True:
	response = input("Please Select from Following Options: \nPress B for Balance Inquiry\nPress W for Withdrawl\nPress A to Add Amount\nPress Q to Quit:\n ").lower()
	valid_responses = ['b', 'w', 'a', 'q']
	response = response.lower()
	if response == 'b':
		print("\nYour Balance is Rs.", amounts[n])
		
	elif response == 'w':
		cash_out = int(input("\nEnter amount you would like to withdraw:"))
		if cash_out%10 != 0:
			print("\nAmount must be the multiple of 10!")
		elif cash_out > amounts[n]:
			print("\nYou have Insufficient Balance!")
		else:
			amounts[n] = amounts[n] - cash_out
			print("\nYour New Balance is Rs.", amounts[n])
			
	elif response == 'a':
		print()
		cash_in = int(input("\nEnter amount you want to Add:"))
		print()
		if cash_in%10 != 0:
			print("\nAmount must be the multiple of 10!")
		else:
			amounts[n] = amounts[n] + cash_in
			print("\nYour New Balance is Rs.", amounts[n])
	
	elif response == 'q':
		exit()
	else:
		print("INVALID RESPONSE!")

