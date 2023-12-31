import re
file = open("../input.txt", "r")
totalValue = 0

while True:
	# do stuff here
	content=file.readline()
	if not content:
		break
	numbers = re.findall(r"\d", content)
	firstNumber = numbers[0]
	lastNumber = numbers[-1]
	combinedNumber = int(str(firstNumber) + str(lastNumber))
	totalValue += combinedNumber
print(totalValue)
file.close()
