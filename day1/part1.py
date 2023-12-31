import re
file = open("../input.txt", "r")
totalValue = 0

while True:
	content=file.readline()
	if not content:
		break
	numbers = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", content)
	for index, number in enumerate(numbers):
		if (number == "one"):
			numbers[index] = '1'
		if (number == "two"):
			numbers[index] = '2'
		if (number == "three"):
			numbers[index] = '3'
		if (number == "four"):
			numbers[index] = '4'
		if (number == "five"):
			numbers[index] = '5'
		if (number == "six"):
			numbers[index] = '6'
		if (number == "seven"):
			numbers[index] = '7'
		if (number == "eight"):
			numbers[index] = '8'
		if (number == "nine"):
			numbers[index] = '9'
	firstNumber = numbers[0]
	lastNumber = numbers[-1]
	combinedNumber = int(firstNumber + lastNumber)
	totalValue += combinedNumber
print(totalValue)
file.close()
