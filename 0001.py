#the idea: use random to judge use which kind random. Just two loops
import random

List = []
while len(set(List))<200 :		#in case of repeat
	string = ""	
	for j in range(10):
		rand = random.randint(1,3)
		if rand ==1:
			x = str(random.randint(0,9))
			string = string + x
		if rand==2:
			y = chr(random.randint(65,90))
			string =string +y
		if rand==3:
			z = chr(random.randint(97,122))
			string =string + z
	List.append(string)
	print(string)