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
            print("Backtracking...")
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

