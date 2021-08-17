import numpy as np
from sim.sim1d import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['CONSTANT_SPEED'] = True

class KalmanFilterToy:
    def __init__(self):
        # Class parameters
        self.v = 0       # Velocity
        self.prev_x = 0  # Prev. car position
        self.prev_t = 0  # Prev. time

    # Predict function     
    def predict(self,t):
       # Predicted value of x position
       # t: actual time 
        prediction = self.prev_x + (self.v * (t - self.prev_t))
        return prediction

    # Measure update function
    def measure_and_update(self,x,t):
        # Actual velocity: delta_x / delta_t  
        measured_v = (x - self.prev_x) / (t - self.prev_t)
        # Update velocity
        self.v = self.v + 0.5 * (measured_v - self.v)
        # Update position
        self.prev_x = x
        # Update time
        self.prev_t = t 

        return


sim_run(options,KalmanFilterToy)
