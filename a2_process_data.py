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
#print("the variable contents: ")
#print(contents)
#print("the variable contents[0]")
#print(contents[0])
#print("the variable contents[0][0]")
#print(contents[0][0])
#print("the type of the variable contents using the type() function: ")
#print(type(contents))
#print("the type of the variable contents[0]: ")
#print(type(contents[0]))
#print("the type of the variable contents[0][0]: ")
#print(type(contents[0][0]))
#print("the variable contents[5][6]")
#print(contents[5][6])
#print("the type of the variable contents[5][6]: ")
#print(type(contents[0][0]))
#print("population of Turkey in 2000: ")
#totalPopulation =0
#for i in range(1,82):
#	totalPopulation=totalPopulation+int(contents[i][1])
#print(totalPopulation)
#print("average population of cities in Turkey in 2001: ")
#totalPopulation =0
#for i in range(1,82):
#	totalPopulation=totalPopulation+int(contents[i][2])
#averageIn2001=totalPopulation/81
#print(round(averageIn2001,0))
#conc=contents[1][0]+contents[2][0]
#print(conc)
#print(contents["hello"])
#conc=contents[1][0]+contents[1][1]
#print(conc)
#print(contents[1][0]*3)
#print(type(conc),type(contents[1][0]*3),type(averageIn2001))
#help(conc)
#help(averageIn2001)
html = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>population of Turkey from 2000 to 2010</title>
        <style>
            body{
            font-size: 15px;
            }
            table, th, td {
                border: 1px solid black;
                
            }
            th, td {
                padding: 5px;
            }
            td{
            text-align: right;
            }
            .grey{
            background-color: #dddddd;
            }
        </style>
    </head>
    <body>
        <table>
            %s
        </table>
    </body>
</html>
"""

include=""
th="<th>%s</th>"
td="<td>%s</td>"
i=0
for row in contents:
    include+="<tr>\n"
    a=0
    color=0
    for cell in contents[i]:

        if(i==0 or a==0):
            co="<th class=\"%s\">"
            if(color%2==0):
                include+=co%"grey"
            else:
                include+=co%"g"
            include+=cell
            include+="</th>\n"
            color+=1
        else:
            co="<td class=\"%s\">"
            if(color%2==0):
                include+=co%"grey"
            else:
                include+=co%"g"
            include+=cell
            include+="</td>\n"
            color+=1
        a+=1
    i+=1
    include+="</tr>\n"


print(html%include)
