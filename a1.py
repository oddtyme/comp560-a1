# Make python file executable
#/usr/bin/env python

# import backtracking search file
import BacktrackingSearch

# import local search file
import LocalSearch

import time

# import multiprocessing to time local search
import multiprocessing

# Open and read input file
f = open("input.txt", "r")
input_string = f.read()

# Use input to create adjacency list of state "nodes" and list of colors

# split lines in order to more easily handle input
input_string_split = input_string.splitlines()

# declare variable for difference "phases" of input read
# Phase 0: Color Read
# Phase 1: State Read
# Phase 2: Adjacent State Read
phase = 0

# declare list of colors and dict for adj list
colors = []
adj_list = {}

for line in input_string_split:
	# line is empty -> increment phase
	if not line:
		phase = phase + 1
	# phase 0 -> add each line to list of colors
	elif phase is 0:
		colors.append(line)
	# phase 1 -> add each state key to adj list with empty lists
	elif phase is 1:
		adj_list[line] = []
	# phase 2 -> for every state w/ adjacent states, add them to that state's respective adj_list
	elif phase is 2:
		# split line string based on white space
		adj_states = line.split()
		adj_list[adj_states[0]].append(adj_states[1])
		adj_list[adj_states[1]].append(adj_states[0])



print("Running Backtracking Search...")
BTS = BacktrackingSearch.BacktrackingSearch()
BTS.main(adj_list, colors)

print("------------------------------------------------")

print("Running Local Search...")
LS = LocalSearch.LocalSearch()

# multiprocessing will terminate search after 60 seconds
p = multiprocessing.Process(target=LS.main, args=(adj_list, colors, ))

p.start()

time.sleep(60)

if p.is_alive():
	print("Local search did not arrive at solution within time constraints")
	p.terminate()


