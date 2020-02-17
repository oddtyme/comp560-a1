# Class that holds all functions relevant to local search
class LocalSearch:
	# function that takes in current solution and evaluates cost
	def cost(self, adj_list, state_color_dict):
		# cost is intially 0

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
