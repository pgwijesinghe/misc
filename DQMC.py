import numpy as np

# Define the model parameters
J = 1.0  # coupling constant
h = 0.0  # magnetic field
N = 16   # number of spins

# Initialize the simulation parameters
T = 1.0  # temperature
beta = 1.0 / T
n_steps = 1000
dt = 0.1

# Set up the initial configuration
s = np.ones(N)

# Define the Hamiltonian
def hamiltonian(s, J, h):
    return -J * np.sum(s[:-1] * s[1:]) - h * np.sum(s)

# Define the Monte Carlo step
def monte_carlo_step(s, beta, dt, J, h):
    # Propose a new configuration by flipping a random spin
    i = np.random.randint(0, N)
    s_new = s.copy()
    s_new[i] *= -1
    
    # Calculate the change in energy
    delta_E = hamiltonian(s_new, J, h) - hamiltonian(s, J, h)
    
    # Accept or reject the proposed configuration
    if np.random.rand() < np.exp(-beta * delta_E):
        s = s_new
        
    # Propose a new phonon configuration
    phi = np.random.normal(scale=np.sqrt(dt), size=N)
    s = s * np.exp(1j * phi)
    
    return s

# Run the DQMC simulation
E = 0.0
E2 = 0.0
for i in range(n_steps):
    s = monte_carlo_step(s, beta, dt, J, h)
    E_step = hamiltonian(s, J, h)
    E += E_step
    E2 += E_step**2
    
# Calculate the average energy and specific heat
E /= n_steps
E2 /= n_steps
C = (E2 - E**2) / (N * T**2)

print("Average energy: ", E)
print("Specific heat: ", C)
