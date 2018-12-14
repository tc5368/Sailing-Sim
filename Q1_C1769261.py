
import csv
from numpy import random as r
import numpy as np

def series_score(t, discard=1):
	for i in range(discard):			#This causes the following line of code to be run as many times as needed to remove bad scores.
		dele = max(t[1])				 #This line of code will take the given tuple and remove the largest item in the list.
	return sum(t[1]) - dele					#This returns the value of the added up list.

def sort_series(t):
	return sorted(t, key=lambda x: (-series_score(x), x[1][0]), reverse = True)

def importing_csv_file(filename):		#This takes the filename of the csv file as input so it knows where to collect the data from.
	with open(filename+'.csv') as f:
		reader = csv.reader(f)			#Then it opens the file and begines to read the data from it.
		raw_data = [r for r in reader]
	return raw_data[1:]					#It then returns the raw data of the file minus the header.

def read_sailor_data():
	where_is_data = 'sailor_performances'								#This is where the name of the location where the infomation is stored.
	raw_data = importing_csv_file(where_is_data)
	sailors = {}
	for people in raw_data:										
		sailors.update({people[0]:(float(people[1]),float(people[2]))})	#This iterated through all the lines on the raw data from the csv file and then
	return(sailors)														#it simultaneously converts the data into the dictionary format.

def generate_performances(sailors):
	scores = {}
	for person in sailors:										#This code will iterate through the sailors and then 
		score = r.normal(sailors[person][0],sailors[person][1])	#using the numpy library random distribution method will
		scores.update({person : score})							# assign each of the sailors a score and then update a dictionary with these scores.
	return scores

def calculate_finishing_order(sailor_scores):
	win_order = []
	for people in (sorted(sailor_scores.items(), key = lambda x: x[1],reverse=True)):	#This line sorts the people in the sailor scores parameter and then also begins
		win_order.append(people[0])											#a loop with them which allows it to have the win order so to print the winers
	return win_order														#it can just run through the loop. Instead it adds them in order to a winning order array

def simulate_the_races(races=6):
	results = {}
	for sailor in read_sailor_data():												#This iterates through the sailors in the csv file
		results.update({sailor:[]})													#it initializes a new results dictionary for the silors in the csv file
	for i in range(races):															
		r = (calculate_finishing_order(generate_performances(read_sailor_data())))	#Then it runs a loop that for however many times the user want to run the races for
		for person in r:															#after it generates the perfromances and works out hte finishing order it will show the winners
			results[person].append(r.index(person)+1)
	return results, r


def main():
	results, standing = simulate_the_races(6)						#results is a list for each player showing where they placed in each race.
	for i in results:
		print(i,results[i])
	print('\nWinning Order: ',standing)	#Works out who won the most overall.

if __name__ == '__main__':
	main()					#runs on start.
	