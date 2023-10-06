import math

n = 365
k = 2

# for debugging
#totalNumerator = n

def getProbabilityOfOverlappingBirthdays_viaRecursion(numberOfPeople):

	def getProbabilityOfAllDistinctBirthdays(numberOfPeople):
		if numberOfPeople <= 1:
			return 1
		else:
			numerator = n - numberOfPeople + 1
			newMultiplier = numerator/n

			# for debugging
			#print(numerator)
			#global totalNumerator
			#totalNumerator *= numerator

			return newMultiplier * getProbabilityOfAllDistinctBirthdays(numberOfPeople-1)
	
	# for debugging - this method skips the calculation of n/n so starting the totalNumerator at n
	#global totalNumerator	
	#totalNumerator = n

	return 1 - getProbabilityOfAllDistinctBirthdays(numberOfPeople) #, totalNumerator



def getProbabilityOfOverlappingBirthdays_viaBigNumbers(numberOfPeople):
	# n choose k
	numberOfPossibleNonFavorableCollections = math.comb(n, numberOfPeople)
	#print(f"# of non-favorable birthday collections: {numberOfPossibleNonFavorableCollections}")

	# takes the number of collections and multiply it to yield the number of sequences
	nonFavorableOutcomes = numberOfPossibleNonFavorableCollections * math.factorial(numberOfPeople)
	#print(f"# of non-favorable birthday sequences:   {nonFavorableOutcomes}")
	
	# total possible sequences of birthdays (exponent)
	totalPossibleSequencesOfBirthdays = n**numberOfPeople
	#print(f"# of total possible birthday sequences:  {totalPossibleSequencesOfBirthdays}")
	
	probabilityOfAllDistinct = nonFavorableOutcomes/totalPossibleSequencesOfBirthdays
	#print(f"Probability of all distinct birthdays:   {probabilityOfAllDistinct}")
	
	probabilityOfOverlap = 1 - probabilityOfAllDistinct
	return probabilityOfOverlap



if __name__ == '__main__':
	while k <= 23:
		print(f"FOR {k} PEOPLE")
		probability = getProbabilityOfOverlappingBirthdays_viaBigNumbers(k)
		percentage = round(probability * 100, 2)
		print(f"Chance of overlapping birthdays: {percentage}%. (via Big Number method)")
		
		probability = getProbabilityOfOverlappingBirthdays_viaRecursion(k)
		percentage = round(probability * 100, 2)
		#print(f"# of non-favorable birthday sequences:   {totalDistinctBirthdaySequences}")
		print(f"Chance of overlapping birthdays: {percentage}%. (via Recursive method)")
		print()

		k+=1
	input()

