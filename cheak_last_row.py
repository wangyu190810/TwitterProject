# This program checks the last follower we have processed from the current tweet-collecting session.
# It then returns the index of the first follower we need to process for the next tweet-collecting session.
# Use the output from this program to update get_likes.py after each tweet-collecting session.

import csv

# update file name with the last output file for each session
read_file = open('Patrick_liked_tweets_122456.210828.csv', 'r', newline='', encoding='utf-8')
list_file = list(csv.reader((line.replace('\0', '') for line in read_file), delimiter=","))

# this is the last follower we have processed from the current session.
last_follower = list_file[-1][0]

# Check the index of the last follower from the input file
input_file = list(csv.reader(open('C:/Users/wangt/Desktop/PythonProjects/Twitter_Project/Patrick_likes.csv')))
row_count = sum(1 for row in input_file)
for i in range(1, row_count):
    if input_file[i][0] == last_follower:
        update_index = i + 1
        print(update_index)

# update line 1848 of get_likes.py with update_index
# That is, the line "users = [path_data[n][0].replace("/","") for n in range(1,row_count)]"
# should be changed to "users = [path_data[n][0].replace("/","") for n in range(update_index,row_count)]"

if __name__ == "__main__":
    pass






