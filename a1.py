# Make python file executable
#/usr/bin/env python

# class that holds functions relevant to backtracking search (might be moved to new file later)
class BacktrackingSearch:
	# function that initiates the backtrack on all distinct graphs
	def main(self, adj_list, colors):
		# output dict linking each state with color
		state_color_dict = {}
	
		# for each distinct root node, run backtrack search with utility function
		for state in adj_list:
			if state not in state_color_dict:
				state_color_dict = self.bt_utility(adj_list, state, colors, state_color_dict)
	

		# output results
		print("-------------------------BACKTRACK RESULTS---------------------------")
		for state in state_color_dict:
			print("State: " + state + ", Color: " + state_color_dict[state])


	# utility function used to do the actual work of backtracking
	def bt_utility(self, adj_list, state, colors, state_color_dict):
		# determine available colors

		# start with all colors (create copy of all colors first)
		available_colors = list(colors)
	
		# then remove colors present in adjacent states
		for adj_state in adj_list[state]:
			if adj_state in state_color_dict:
				if state_color_dict[adj_state] in available_colors:
					available_colors.remove(state_color_dict[adj_state])

		# if no colors remaining, return false
		if not available_colors:
			print("Bracktracking...")
			return False
		# otherwise, 
		else:
			# try first color in list of available colors. Use pointer to keep track of current position
			pointer = 0
			print("Assigning " + available_colors[pointer] + " to " + state)
			state_color_dict[state] = available_colors[pointer]
			
			for adj_state in adj_list[state]:
				# check if node is visited already
				if adj_state not in state_color_dict:
					# while search fails at next level, try different color here
					while not self.bt_utility(adj_list, adj_state, colors, state_color_dict):
						# if no more colors available here, unvisit state and return false
						pointer = pointer + 1
						if pointer is len(available_colors):
							print("Removing " + state_color_dict[state] + " from " + state)
							del state_color_dict[state]
							print("Backtracking...")
							return False
						else:
							print("Assigning " + available_colors[pointer] + " to " + state)
							state_color_dict[state] = available_colors[pointer]
					
			# all has gone well: return solution
			return state_color_dict



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



# TODO: Implement Backtracking Search
print("Running Backtracking Search...")
BTS = BacktrackingSearch()
BTS.main(adj_list, colors)
