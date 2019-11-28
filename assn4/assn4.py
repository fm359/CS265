#!/usr/bin/env python3
# assn4 - Cash Register
#
# Farhan Muhammad
# 06/07/2018

import sys;

# Sub Commands #######################################################################################################

def init(initialAmount, bills) :

# initialize register - create/reset cash register with initial 
# amount, denominations, and data file to store its contents

# cmd input example: ./assn4 init 15 = 10 1 0 0

	if (len(initialAmount) != 1 or len(bills) != 4) :		  # input denominations format check
		sys.exit(1)

	try: 
		initialAmount = int(initialAmount[0])			  # convert input to arrays of integers
		for i in range(len(bills)) :
			bills[i] = int(bills[i])
	except:
		sys.exit(1)

	billsAmount = 1*bills[0] + 5*bills[1] + 10*bills[2] + 20*bills[3] # calculated total from denominations

	if (initialAmount != billsAmount) :	# check if lhs amount = total of rhs denominations
		 sys.exit(2)

	recordFile = open("record.txt", "w+")	# create/reset register and data file
	totalPurchases = 0			# running total of purchases

	# stored data example: 0 : 15 = 10 1 0 0
	recordFile.write("%s : %s =" % (totalPurchases, initialAmount))
	for i in range(len(bills)) :
		recordFile.write(" %s" % bills[i])
	recordFile.write("\n")
	recordFile.close()
	sys.exit(0)

def purchase(purchaseAmount, billsGiven) :

# purchase item - accept cash for purchase and return change, update data file with running total
# income from sales, total amount of cash in the register, and denomination breakdown

# cmd input example: ./assn4 purchase 38 = 0 0 0 2

	if (len(purchaseAmount) != 1 or len(billsGiven) != 4) :
                sys.exit(1)

	try:
		purchaseAmount = int(purchaseAmount[0])
		for i in range(len(billsGiven)) :
			billsGiven[i] = int(billsGiven[i])
	except:
		sys.exit(1)

	isFile("record.txt")					# isFile() defined below
	recordFile = open("record.txt", "r")
	currentRegister = recordFile.read().rstrip("\n").split(" ")
	recordFile.close()

	currentTotal = int(currentRegister[2])			# current amount of cash in the register
	amountGiven = 1*billsGiven[0] + 5*billsGiven[1] + 10*billsGiven[2] + 20*billsGiven[3]
	if (purchaseAmount > amountGiven) :
		sys.exit(2)
	changeAmount = amountGiven - purchaseAmount
	if (currentTotal < changeAmount) :			# check if there is sufficient denominations
		sys.exit(3)					# in the register for the change

	currentBills = []					# breakdown of denominations in the register
	for i in range(4) :
		currentBills.append(int(currentRegister[i+4]))
	changeBills = calcChange(changeAmount, currentBills)    # calcChange() defined below

	for i in range(4) :					# add received denominations and update
		if (billsGiven[i] > 0) :			# total amount in the register
                        currentBills[i] += billsGiven[i]
	currentTotal = 1*currentBills[0] + 5*currentBills[1] + 10*currentBills[2] + 20*currentBills[3]

	totalPurchases = int(currentRegister[0])		# update running total of purchases
	totalPurchases += purchaseAmount			#
	recordFile = open("record.txt", "w")			# update data file
	recordFile.write("%s : %s =" % (totalPurchases, currentTotal))
	for i in range(len(currentBills)) :
		recordFile.write(" %s" % currentBills[i])
	recordFile.write("\n")
	recordFile.close()
	print (changeBills[0], changeBills[1], changeBills[2], changeBills[3]) # display change denominations
	sys.exit(0)

def change(change, request) :

# return change - provide change for requested denominations

# cmd input example: ./assn4 change 0 1 0 0 = 5 0 0 0
#		     ./assn4 change 0 1 = 5 (can ommit trailing 0's)

	try:
		for i in range(len(change)) :
			change[i] = int(change[i])
		for i in range(len(request)) :
			request[i] = int(request[i])
	except:
		sys.exit(1)

	change = formattedChange(change)		# formattedChange() defined below
	request = formattedChange(request)		#
	changeAmount = 1*change[0] + 5*change[1] + 10*change[2] + 20*change[3]
	requestAmount = 1*request[0] + 5*request[1] + 10*request[2] + 20*request[3]
	if (changeAmount != requestAmount) :
		sys.exit(2)

	isFile("record.txt")
	recordFile = open("record.txt", "r")
	currentDrawer = recordFile.read().rstrip("\n").split(" ")
	recordFile.close()

	currentBills = []
	for i in range(4) :
		currentBills.append(int(currentDrawer[i+4]))
		currentBills[i] -= request[i]
		if (currentBills[i] < 0) :			# check for sufficient funds
			sys.exit(3)
		currentBills[i] += change[i]
		currentDrawer[i+4] = str(currentBills[i])

	currentDrawer = (" ").join(currentDrawer)
	recordFile = open("record.txt", "w")
	recordFile.write("%s" % currentDrawer)
	recordFile.write("\n")
	recordFile.close()
	print (request[0], request[1], request[2], request[3])	# display requested denominations

	sys.exit(0)

def report() :

# report register - display contents of data file

# cmd input example: ./assn4 report

	isFile("record.txt")
	recordFile = open("record.txt", "r")
	currentDrawer = recordFile.read().rstrip("\n")
	print (currentDrawer)
	recordFile.close()

	sys.exit(0)

# Additional Methods #################################################################################################

def calcChange(changeAmount, currentBills) :

# calculate change - breakdown change owed into denominations such that
# larger denominations are considered first

	changeBills = [0, 0, 0, 0]
	while (changeAmount >= 20 and currentBills[3] > 0) :
		changeAmount -= 20
		currentBills[3] -= 1
		changeBills[3] += 1

	while (changeAmount >= 10 and currentBills[2] > 0) :
		changeAmount -= 10
		currentBills[2] -= 1
		changeBills[2] += 1

	while (changeAmount >= 5 and currentBills[1] > 0) :
		changeAmount -= 5
		currentBills[1] -= 1
		changeBills[1] += 1

	while (changeAmount >= 1 and currentBills[0] > 0) :
		changeAmount -= 1
		currentBills[0] -= 1
		changeBills[0] += 1

	if (changeAmount > 0) :			# check for sufficient funds
		sys.exit(3)

	return changeBills

def isFile(recordfile) :

# check if data file exists

	try:
                f = open(recordfile)
                f.close()
	except:
                sys.exit(4)

def formattedChange(bills) :

# format array for change subcommand - if input arrays for change are abridged

	adjustedBills = [0, 0, 0, 0]
	for i in range(len(bills)) :
		adjustedBills[i] = bills[i]
	return adjustedBills

# Main ###############################################################################################################

def main(argv = sys.argv) :

	argc = len(argv)
	if (argc == 1) :
		sys.exit(1)
	subcommand = argv[1]

	if (subcommand != "report") :
		try:
			arguments = (" ").join(argv).split(" = ")	# split cmd input arguments at " = "
			lhs = arguments[0].split(" ")
			lhs = lhs[2:]
			rhs = arguments[1].split(" ")
		except:
			sys.exit(1)

	elif (subcommand == "report") :
		if (argc > 2) :
			sys.exit(1)
		else :
			report()

	if (subcommand == "init") :
		initialAmount = lhs
		initialBills = rhs
		init(initialAmount, initialBills)

	elif (subcommand == "purchase") :
		purchaseAmount = lhs
		givenBills = rhs
		purchase(purchaseAmount, givenBills)

	elif (subcommand == "change") :
		givenChange = lhs
		requestedChange = rhs
		change(givenChange, requestedChange)

	else :
		sys.exit(1)

if __name__ == "__main__" :
        main()
