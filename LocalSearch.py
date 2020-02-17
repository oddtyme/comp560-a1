# import randrange for random assignment
from random import randrange

# Class that holds all functions relevant to local search
class LocalSearch:
	# main function where action takes place
	def main(self, adj_list, colors):
		print("Randomly assigning colors...")
		state_color_dict = self.randomAssignment(adj_list.keys(), colors)		

		# print random assignments for test purposes
		for state in state_color_dict:
			print("Randomly assigned " + state_color_dict[state] + " to " + state)
		
		# get initial cost
		cost = self.cost(adj_list, state_color_dict)

		# print initial cost for testing purposes
		print("INITIAL COST: " + str(self.cost(adj_list, state_color_dict)))

		while cost > 0:
			

	# function that randomly assigns all states a color
	def randomAssignment(self, state_list, colors):
		state_color_dict = {}
		
		for state in state_list:
			state_color_dict[state] = colors[randrange(4)]

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
