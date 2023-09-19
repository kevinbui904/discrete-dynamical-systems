# Functions that allow us to easily create and analyze 
# compartmental models.

def my_list_function(x):
    """This is a sample function that returns a list of numbers from 0 to x."""
    my_list = []
    for i in range(x+1):
        my_list.append(i)
    return my_list

class CompartmentalModel:
    def __init__(self, start_states = None, compartments = None, time_units = "days"):
        """compartments is a list of functions that each take in 
        the current state and current time step and return how 
        much the states change due to that compartment."""

        # self.starting_value = starting
        # This will contain a list of functions that look like:
        # eat(states={deer: 100, plant: 3000}, timestep=1) -> {deer: 10, plant: -100}
        self.compartments = compartments

        # Eventually store all of the states in a list, so that if we 
        # later want to compute more, we don't have to re-compute the early states
        
        #This will containing a dictionary with keys and array values
        #{deer: [100, 200, 100]}, plant:[3000, 2000, 1000]}
        self.states = start_states
        
        self.max_timestep_computed = 0
        self.time_units = time_units

    def get_states(self):
        """Return a list of all of the states that have been computed so far."""
        return self.states
    
    def get_time_units(self):
        """Return the time units that this model is using."""
        return self.time_units
    
    def print_states(self):
        """Print out all of the states that have been computed so far in a nice format."""
        population_names = self.states.keys()
        names_string = "\t".join(population_names)

        # print the header
        print(f"{self.time_units} {names_string}")

        # print the values
        for i in range(self.max_timestep_computed + 1):
            # print the timestep
            print(f"{i}", end="\t")
            for name in population_names:
                # print the value of each population
                print(f"{round(self.states[name][i], 2)}", end="\t")
            # print a new line
            print()


    def simulate(self, timesteps):
        """Simulate the model for the given number of timesteps."""
        for i in range(self.max_timestep_computed + 1, timesteps + 1):
            keys = self.states.keys()
            cur_state = {}
            new_state = {}
            # Grab the last computed states for each key in the dict
            for key in keys:
                cur_state[key] = self.states[key][-1]
                new_state[key] = self.states[key][-1]

            # Compute the new state

            # Use each compartment function to get a new piece of the state
            # Compute a new state for each time_step, update only at the end
            for compartment in self.compartments:
                changes_dict = compartment(cur_state, i)
                for key in keys:
                    new_state[key] += changes_dict[key]

            # Add the new state to the list of states
            for key in keys:
                self.states[key].append(new_state[key])
        
        # Update the max timestep computed tracker
        self.max_timestep_computed = timesteps



    