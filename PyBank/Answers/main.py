import csv
import os

# opening the csv file and calling it csv_file in code the passing it through the reader and abeling it as a list called data


with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        a = csv_reader.line_num
        b = str(a-1)
    print('''\nTotal number of Months : ''' + b)


# opens a CSV and calls it csv_file in code then passes it through the reader
with open('budget_data.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    header = next(csv_reader)
    total = sum(int(row[1])for row in csv.reader(csv_file))
    

 # this block takes the csv_reader and converts to a list then strips the profit loss data out and crates a new list,new_list [].  
with open("budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    data = list(csv_reader)
    new_list = []
   
    for e in data:
        plVal = e[1]
        new_list.append(plVal)


# in this block the program a new list, avg1_list, is created with the profit/ loss changes from month to month for averaging. 
with open("budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    avg1_list=[]
# once the delta from month to month is captured in this new list, avg1_list, the max and min changes can be determined and assigned to variables.
    for i in range(1,len(new_list)):
        avg1_list.append((int(new_list[i])-int(new_list[i-1])))
        b = avg1_list
        b = sum((avg1_list)) /len(avg1_list)
        c = max(avg1_list)
        d = min(avg1_list)

# the program will create a new list of just the dates so it can zipit to the profit loss difference list
    date_list = []
   
    for e in data:
        dtVal = e[0]
        date_list.append(dtVal)

# this is where the program creates a new "final list" with the months and the profit loss difference in order to determine the month where we experienced the largest and smallest swings
    PL_list = []
    for  i, [x, y] in enumerate(zip(avg1_list, date_list)):
        Final_list =  [i,x,y]
        Fl_list=list(Final_list)
        PL_list.append(Fl_list)
   
# here the program takes the final composite list and prints out the row where we experienced the largest and smallest changes    
    for i, e in enumerate(PL_list):
            if e[1] == c:
                
                MaxEl = e[2] 

    for i, e in enumerate(PL_list):
            if e[1] == d:
                
                MinEl = e[2] 


print('''The net Profit/Loss over the period is: ''' + '''$''' + str(float(total)))
print("The average of the profit loss changes for the period are: " + "$" + str(round(b,2)))
print("The greatest increase in profits was :" + "$" + str(c) + " for the month of " + MaxEl)
print("The greatest decrease in profits was :" + "$" + str(d) + " for the month of " + MinEl)

str1 = str('''The net Profit/Loss over the period is: ''' + '''$''' + str(float(total)))
str2 = str("The average of the profit loss changes for the period are: " + "$" + str(round(b,2)))
str3 = str("The greatest increase in profits was :" + "$" + str(c) + " for the month of " + MaxEl)
str4 = str("The greatest decrease in profits was :" + "$" + str(d) + " for the month of " + MinEl)


with open("Final_Answer.txt", "w") as file:
    file.write('The final answer is :' + '\n' + str1 +'\n' + str2 +'\n'+ str3 +'\n'+ str4) 

 