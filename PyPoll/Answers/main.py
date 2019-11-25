import csv
import os
import math


with open('election_data.csv', 'r') as csv_file:
    vote_reader = csv.reader(csv_file)

#counts number of lines to return a total voter turnout number    
    for row in vote_reader:
        a = vote_reader.line_num
    
        b = str(a-1)

        c=int(a-1)

    print('''\nTotal number of Votes : ''' + b)

with open('election_data.csv', 'r') as csv_file:
    vote_reader = csv.reader(csv_file)
    header = next(vote_reader)
    voteList = list(vote_reader)

# creates a separate list with just the candidates involved by filtering out the non-unique occurences of candidate names   
    vote_list = []
   
    for e in voteList:
        voteVal = e[2]
        vote_list.append(voteVal)

    cleanList = list(dict.fromkeys(vote_list)) 
    cand_list = list(cleanList) 
    print("The candidates are: " +str(cand_list) +'\n')

    for i in range(0, len(cand_list)): 
#counts each candidates number of votes   
        count1 = vote_list.count(cand_list[0])
        count2 = vote_list.count(cand_list[1])
        count3 = vote_list.count(cand_list[2])
        count4 = vote_list.count(cand_list[3])

#calc percent of the vote obtained by candidate then creates a list of winning percents to combine with candidate list
        voteNum1 = count1/c*100
        voteNum2 = count2/c*100
        voteNum3 = count3/c*100
        voteNum4 = count4/c*100

    winner_list = [voteNum1,voteNum2, voteNum3, voteNum4]
    

    Winning_list = list(zip(cand_list, winner_list))
    
for i, e in enumerate(Winning_list):
            if e[1] == max(winner_list):
                
                Winner = e[0] 



print(str(cand_list[0]) + ' : Total Vote Count: '+ str(count1) + ' : Percent Vote: ' + str(int(voteNum1))+'%\n')
print(str(cand_list[1]) + ' : Total Vote Count: '+ str(count2) + ' : Percent Vote: ' + str(int(voteNum2))+'%\n')
print(str(cand_list[2]) + ' : Total Vote Count: '+ str(count3) + ' : Percent Vote: ' + str(int(voteNum3))+'%\n')
print(str(cand_list[3]) + ' : Total Vote Count: '+ str(count4) + ' : Percent Vote: ' + str(int(voteNum4))+'%\n')
print('THE WINNER IS  ' + Winner + '!!!!!!!!!!(Spock Voice)')

str1 = str(str(cand_list[0]) + ' : Total Vote Count: '+ str(count1) + ' : Percent Vote: ' + str(int(voteNum1))+'%\n')
str2 = str(str(cand_list[1]) + ' : Total Vote Count: '+ str(count2) + ' : Percent Vote: ' + str(int(voteNum2))+'%\n')
str3 = str(str(cand_list[2]) + ' : Total Vote Count: '+ str(count3) + ' : Percent Vote: ' + str(int(voteNum3))+'%\n')
str4 = str(str(cand_list[3]) + ' : Total Vote Count: '+ str(count4) + ' : Percent Vote: ' + str(int(voteNum4))+'%\n')
str5 = str('THE WINNER IS  ' + Winner + '!!!!!!!!!!(Spock Voice)')


with open("Poll_Answer.txt", "w") as file:
    file.write('The final answer is :' + '\n' + str1 +'\n' + str2 +'\n'+ str3 +'\n'+ str4+'\n'+ str5 ) 