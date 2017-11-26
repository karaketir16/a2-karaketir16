#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################
print("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>India Temperature Analysis</title></head><body>")

print("<p>the variable contents: </p>")
print(contents)
print("<p>the variable contents[0]</p>")
print(contents[0])
print("<p>the variable contents[0][0]</p>")
print(contents[0][0])
print("<p>the type of the variable contents using the type() function: </p>")
print(type(contents))
print("<p>the type of the variable contents[0]: </p>")
print(type(contents[0]))
print("<p>the type of the variable contents[0][0]: </p>")
print(type(contents[0][0]))
print("<p>the variable contents[5][6]")
print(contents[5][6])
print("<p>the type of the variable contents[5][6]: </p>")
print(type(contents[0][0]))
print("<p>population of Turkey in 2000: </p>")
totalPopulation =0
for i in range(1,82):
	totalPopulation=totalPopulation+int(contents[i][1])
print(totalPopulation)
print("<p>average population of cities in Turkey in 2001: </p>")
totalPopulation =0
for i in range(1,82):
	totalPopulation=totalPopulation+int(contents[i][2])
averageIn2001=totalPopulation/81
print(round(averageIn2001,0))
conc=contents[1][0]+contents[2][0]
print(conc)
print("<p>print(contents[\"hello\"]): TypeError: list indices must be integers or slices, not str</p>")
conc=contents[1][0]+contents[1][1]
print(conc)
print(contents[1][0]*3)
print(type(conc),type(contents[1][0]*3),type(averageIn2001))
help(conc)
help(averageIn2001)

print("</body></html>")
