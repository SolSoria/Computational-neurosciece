import numpy as np
import matplotlib.pyplot as plt

tau_v = 10  # Time constant in ms
R = 1       # Resistance
v_th = 10   # Threshold voltage
dt = 1      # Time step in ms
T = 100     # Total simulation time in ms
time_steps = np.arange(0, T+dt, dt) 

def integrate_and_fire(I):
    v = 0 
    voltages = []  # Store voltage values
    spikes = []  # Store spike times
    for t in time_steps:
        #Euler Ecuation 
        v = v + (dt/tau_v) * (-v + R*I) 
        
        if v >= v_th:  # If voltage crosses threshold
            spikes.append(t)  # Record spike time
            v = 0  # Reset voltage after spike
        
        voltages.append(v)
    
    return np.array(voltages), spikes

# for different constante currents
currents = [9, 11, 15]
voltage_results = {}

plt.figure(figsize=(10, 5))
for I in currents:
    v, spikes = integrate_and_fire(I)
    voltage_results[I] = v
    plt.plot(time_steps, v, label=f'I = {I} μA')

plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (V)')
plt.title('Integrate-and-Fire Neuron Model')
plt.legend()
plt.grid()
plt.show()