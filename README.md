Integrate-and-Fire Model
Code an integrate-and-fire model, given by the following equation: 

τv dv/dt =−v + RI,

where the time constant τv = 10ms and the resistance R= 1. When the neuron crosses a threshold
vth = 10, the neuron emits a spike and is reset to 0.

Use the Euler method to simulate the neuron model, with a time step of 1ms. For the Euler
method, we can re-write the integrate-and-fire model as: 
τv (v(t+1)−v(t))/∆t =−v(t) + RI(t), where ∆t is the time step. We therefore have: v(t + 1) = v(t) + ∆t
τv (−v(t) + RI(t)).

Simulate the neuron for 100ms for different constant currents I= 9, I= 11, I= 15. Plot the
voltage across time for the different currents. Comment.
