# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Fatima"
my_age = 29
my_bio = "Software Engineer"
myself = Person(my_name, my_bio, my_age)

def introduction():
	print("Hello, %s. Welcome to our portal." % my_name)


def options():
	print("--------------------------------")
	print("Would you like to:")
	print("1) create a new club.")
	print("Or:")
	print("2) Browse and join club.")
	print("Or:")
	print("3) View existing club.")
	print("Or:")
	print("4) Display members of club.")
	print("Or:")
	print("-1) Close Application")

def create_club(club_name, club_describtion):
	# your code goes here!
	return Club(club_name, club_describtion)

def view_clubs():
	print()
	for cl in clubs:
		print("\t\tNAME : %s"%(cl.name))
		print("\t\tDESCRIPTION : %s"%(cl.description))
		print("\t\tMEMBERS : %s"%(len(cl.members)))
		print()    
	print("--------------------------------")

def view_club_members(club):
	club.print_member_list()
	
def join_clubs():
	view_clubs()  
	user_club_join = input("Enter the name of the club you'd like to join :")
	flag = True
	while flag:
		for item in clubs:
			if(item.name == user_club_join):
				item.recruit_member(myself)
				print("%s just joined %s Club."%(my_name, user_club_join))
				print("--------------------------------")
				flag = False
				break
		else:
			print("Sorry, we havn't a club with this name ! Try again :")
			user_club_join = input("Enter the name of the club you'd like to join :")

				

def application():
	introduction()
	
	while True:
		options() 
		choice = input()
		if(choice == '1'):
			club_name = input("Pick a name for your awesome new club: ")
			print("What is your club about? ")
			club_describtion = input()
			myclub = create_club(club_name, club_describtion)
			myclub.assign_president(myself)
			age_sum = myself.age

			print("Enter the number of people you would like to recruit to your new club (-1 to stop): ")   
			print("--------------------------------")
			print("[1] Steve\n[2] Michelle \n[3] John \n[4] Ron \n[5] Maha \n[6] Fatma \n[7] Dude \n[8] Dudette \n[9] Forever Alone \n[10] confession Bear \n[11] Jack \n[12] Audrey \n[13] Asis \n[14] Caesar \n[15] Marcus Aurelius")

			while True:
				n = int(input())
				if n == -1:
					break
				elif n in range(1,16):
					myclub.recruit_member(population[n-1])
					age_sum += population[n-1].age
				else:
					print("Invalid choice ! Try again : ")

			clubs.append(myclub)
			print()
			print("Here's your club :")
			print("Club Name : %s"%(myclub.name))
			print("Club Discription : %s"%(myclub.description))
			myclub.print_member_list()

			average = age_sum / len(myclub.members)
			print("Average age in this club: %s"%(average))
			

		elif(choice == '2'):
			join_clubs()
			

		elif(choice == '3'):
			view_clubs()
			

		elif(choice == '4'):
			view_clubs()
			see_club = input("Enter the name of the clup whose members you'd like to see:")
			flag = True
			while flag:
				for item in clubs:
					if(item.name == see_club):
						view_club_members(item)
						flag = False
						break
				else:
					print("Sorry, we havn't a club with this name ! Try again :")
					see_club = input("Enter the name of the club you'd like to join :")					
			

		elif(choice == '-1'):
			break

		else:
			print("Wrong input ! ,Try again :")
			print()
			options()
			choice = input()
			


