'''
Q56. airline information system want to maintain the information of passengers 
traveling by their airways. Following is the information that is to be maintained for 
the passengers.                             
Name of passenger
Age of passenger
flight no.
departure time
source
destination
Design a class to accept and display information for the airlines.
						author @raghav
Date Created : 16 Feb 2022 | Last Updated : 20 Feb 2022
'''

# User defined class
class passengers:

	def __init__(self, name, age, f_no, dep_time, source, dest):
		self.name = name
		self.age = age
		self.f_no = f_no
		self.dep_time = dep_time
		self.source = source 
		self.dest = dest

	def show(self):
		print(f'''
Name : {self.name}
Age : {self.age}
Flight Number : {self.f_no}
Departure Time : {self.dep_time}
Source : {self.source}
Destination : {self.dest}
''') 


# Main 
print('Class : Airline ')
p1 = passengers('Raghav', 12, 8765, 1830, 'CBE', 'MUM')
p2 = passengers('Hello', 1, 765, 1630, 'MUM', 'CBE')

p2.show()
p1.show()






