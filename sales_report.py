"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
# bob -> 10
# salespeople = ["eric", "bob", "grace", "tina", "tina"]
# melons_sold = [5, 12, 3, 5, 6]


# index = salespeople.index("bob")
# print index
# melons_sold[index] += 2

# print melons_sold[index]

# melons_sold[index] += 4
# print melons_sold[index]

# melons_sold[index-1] +=1
# print melons_sold[index-1]
salespeople = []
melons_sold = []

f = open("sales-report.txt") #opens function opens text file pass file name as a string and save it to varible f 

for line in f: # iterate thru the file returns each line in the file with white space between the lines 
    # print line 
    line = line.rstrip() #strips out the extra white space between the lines and returns a long string with | between words 

    entries = line.split("|") # splits the long string at the | returns a list of strings split at the | instead of one long string
    # print entries 
    salesperson = entries[0] # grabs the 1st element at index 0 in the list which is the salesperson's name and will iterate thru the list at zero index 
    melons = int(entries[2])#grabs number of melons from index 2 of the list type casts it from a string to an integer and save it to variable melons 

    # checks to see if salesperson already has a tally of sales
    # #If so, add. Else, add salesperson and tally to list.

    if salesperson in salespeople: # This is going to evaluate as false the first time because the list is empty
        #it will go to the else statement and append salesperson and the melons 
        position = salespeople.index(salesperson) # gets the index by index function of the salesperson [0] saves to variable position
        melons_sold[position] = melons_sold[position] + melons #grab that position of melons sold at that index and increment by numnber of melons and save to that variable melons_sold[position]
    else:
        salespeople.append(salesperson) # This is going to evaluate as false the first time because the list is empty
        #it will go to the else statement and append salesperson and the melons
        melons_sold.append(melons)


for i in range(len(salespeople)): # iterates thru our salesperson list by index 
     print "{} sold {} melons".format(salespeople[i], melons_sold[i]) #grabs that name element at that index and element melons sold at that index 
    #print s {} salespeople[i] melons_sold[i] {} string format  with sold melons 