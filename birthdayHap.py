
n = 365
k = 2

def getBirthdayOverlapProbability(numberOfPeople):

	def multiplyBirthdayMultipliers(numberOfPeople):
		if numberOfPeople <= 1:
			return 1
		else:
			numerator = n - numberOfPeople + 1
			newMultiplier = numerator/n
			#print(numerator)
			return newMultiplier * multiplyBirthdayMultipliers(numberOfPeople-1)
	
	return 1 - multiplyBirthdayMultipliers(numberOfPeople)


if __name__ == '__main__':
	while k < 24:
		probability = getBirthdayOverlapProbability(k)
		percentage = probability * 100
		print(f"Put {k} people in a room and the odds that there will be a common birthday is {probability}%.")
		k+=1

