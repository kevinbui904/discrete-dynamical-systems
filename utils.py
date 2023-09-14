# Functions that allow us to easily create and analyze 
# compartmental models.

def my_list_function(x):
    """This is a sample function that returns a list of numbers from 0 to x."""
    my_list = []
    for i in range(x+1):
        my_list.append(i)
    return my_list

class CompartmentalModel:
    def __init__(self, starting_value, compartments = None):
        """compartments is a list of functions that each take in 
        the current state and current time step and return how 
        much the state changes due to that compartment."""

        self.starting_value = starting_value
        self.compartments = compartments

        # Eventually store all of the states in a list, so that if we 
        # later want to compute more, we don't have to re-compute the early states
        self.states = [starting_value]
        self.max_timestep_computed = 0

    def get_states(self):
        """Return a list of all of the states that have been computed so far."""
        return self.states

    def simulate(self, timesteps):
        """Simulate the model for the given number of timesteps."""
        for i in range(self.max_timestep_computed + 1, timesteps + 1):
            # Compute the new state
            new_state = self.states[-1]
            # Use each compartment function to get a new piece of the state
            for compartment in self.compartments:
                cur_state = new_state
                new_state += compartment(cur_state, i)
            self.states.append(new_state)
        
        # Update the max timestep computed tracker
        self.max_timestep_computed = timesteps



    