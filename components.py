# CLASSES AND METHODS
class Person():
	def __init__(self, name, bio, age):

		self.name = name
		self.bio = bio
		self.age = age
		self.status = "member"

class Club():
	def __init__(self, name, description):
		
		self.name = name
		self.description = description
		self.members = []

	def assign_president(self, person):
		
		person.status = "president"
		self.members.append(person)

	def recruit_member(self, person):

		self.person = person
		self.members.append(person)

	def print_member_list(self):
		print()    
		print("Members :")
		for m in self.members:
			if m.status == "president":
				print("- %s (%s years old ,President) - %s"%(m.name , m.age , m.bio))
			else:
				print("- %s (%s years old) - %s"%(m.name , m.age , m.bio))

