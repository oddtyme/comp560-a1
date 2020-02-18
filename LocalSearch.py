# import random for arbitrary choices
import random

# import math for Simulated Annealing algorithm
import math

import time

# Class that holds all functions relevant to local search
class LocalSearch:
	# main function where action takes place
	def main(self, adj_list, colors):
		print("Randomly assigning colors...")
		state_color_dict = self.randomAssignment(adj_list.keys(), colors)		

		# print random assignments for test purposes
		for state in state_color_dict:
			print("Randomly assigned " + state_color_dict[state] + " to " + state)
		
		# print initial cost for testing purposes
		print("INITIAL COST: " + str(self.cost(adj_list, state_color_dict)))

		print("Searching...")

		while self.cost(adj_list, state_color_dict) > 0:
			# create potential new solution
			state_color_dict_prime = dict(state_color_dict)

			# choose random state 
			rand_state = random.choice(list(state_color_dict))
			

			# create copy of colors
			available_colors = list(colors)
			
			# remove original color from list of colors 
			available_colors.remove(state_color_dict[rand_state])

			# randomly choose a color from that list and assign it to randomly selected state
			rand_color = random.choice(available_colors)
			state_color_dict_prime[rand_state] = rand_color

			# compare solutions
			if self.cost(adj_list, state_color_dict_prime) < self.cost(adj_list, state_color_dict):
				print("Cooling...")
				print("Swtiched " + rand_state + " from " + state_color_dict[rand_state] + " to " + rand_color)
				state_color_dict = state_color_dict_prime
			else:
				# implement simulated annealing condition
				# calculate difference in temp of trade
				diff = self.cost(adj_list, state_color_dict_prime) - self.cost(adj_list, state_color_dict)

				# delta d negated
				negdiff = -1 * diff
				
				# exponential value calculated
				exponent = float(negdiff) / float(self.cost(adj_list, state_color_dict))
		
				# SA condition for accepting bad trades
				if math.exp(exponent) > random.uniform(0, 1):
					print("Warming...")
					print("Swtiched " + rand_state + " from " + state_color_dict[rand_state] + " to " + rand_color)
					state_color_dict = state_color_dict_prime
					

		print("----------------LOCAL SEARCH RESULTS-------------------")
		for state in state_color_dict:
			print("State: " + state + ", Color: " + state_color_dict[state])
		
	

	# function that randomly assigns all states a color
	def randomAssignment(self, state_list, colors):
		state_color_dict = {}
		
		for state in state_list:
			state_color_dict[state] = colors[random.randrange(4)]

		return state_color_dict

	
	# function that takes in current solution and evaluates cost
	def cost(self, adj_list, state_color_dict):
		# cost is intially 0
		cost = 0

		# check every edge for equal colors
		for state in adj_list.keys():
			for adj_state in adj_list[state]:
				# get colors of each state
				color1 = state_color_dict[state]
				color2 = state_color_dict[adj_state]
				
				# if colors are the same, cost of solution increases by .5
				# suboptimal solution will count each edge twice, therefore each flawed edge will end up counting as 1
				if color1 is color2:
					cost = cost + .5
		
		return cost
