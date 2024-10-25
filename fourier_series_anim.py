import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the function
def f(x):
    return 2*np.sin(x) - x**2

# Set up the interval
a = 0  # Starting point
b = 2  # End point for better visibility
T = b - a  # Period of the function

# Number of Fourier series terms to include
num_terms = 50

# Calculate a0 coefficient
a0 = (1 / T) * quad(f, a, b)[0]

# Function to calculate Fourier coefficients
def fourier_coefficients(n):
    an = (2 / T) * quad(lambda x: f(x) * np.cos(2 * np.pi * n * (x - a) / T), a, b)[0]
    bn = (2 / T) * quad(lambda x: f(x) * np.sin(2 * np.pi * n * (x - a) / T), a, b)[0]
    return an, bn

# Set up the x values for plotting
x_vals = np.linspace(a, b, 5000)

# Initialize arrays for each Fourier component
y_dc = np.full_like(x_vals, a0 / 2)   # Start with DC term (constant)
y_sine = np.zeros_like(x_vals)        # Placeholder for sine term
y_cosine = np.zeros_like(x_vals)      # Placeholder for cosine term
y_fourier = np.full_like(x_vals, a0 / 2)  # Start with Fourier series using DC term

# Prepare subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Fourier Series Approximation of a Function")

# Plot the original function for reference
axs[1, 1].plot(x_vals, f(x_vals), label="Original function", color='black', linestyle='--', linewidth=2)

# Main loop to calculate and plot each Fourier term
for n in range(1, num_terms + 1):
    # Calculate Fourier coefficients
    an, bn = fourier_coefficients(n)
    
    # Calculate current sine and cosine terms
    y_sine = bn * np.sin(2 * np.pi * n * (x_vals - a) / T)
    y_cosine = an * np.cos(2 * np.pi * n * (x_vals - a) / T)
    
    # Update cumulative Fourier series approximation
    y_fourier += y_sine + y_cosine
    
    # Clear previous lines in each subplot
    for ax in axs.flat:
        ax.cla()
    
    # DC Term plot
    axs[0, 0].plot(x_vals, y_dc, color='yellow', linewidth=2)
    axs[0, 0].set_ylim(-5, 5)
    axs[0, 0].set_title("DC Term")
    
    # Sine term plot
    axs[0, 1].plot(x_vals, y_sine, color='cyan', linewidth=2)
    axs[0, 1].set_ylim(-5, 5)
    axs[0, 1].set_title(f"Current Sine Term (n={n})")
    
    # Cosine term plot
    axs[1, 0].plot(x_vals, y_cosine, color='magenta', linewidth=2)
    axs[1, 0].set_ylim(-5, 5)
    axs[1, 0].set_title(f"Current Cosine Term (n={n})")
    
    # Fourier series approximation plot
    axs[1, 1].plot(x_vals, f(x_vals), label="Original function", color='black', linestyle='--', linewidth=2)
    axs[1, 1].plot(x_vals, y_fourier, color='red', label=f'Fourier Series Approximation ({n} terms)')
    axs[1, 1].set_ylim(-5, 5)
    axs[1, 1].legend(loc="upper right")
    axs[1, 1].set_title("Fourier Series Approximation")
    
    # Adjust plot layout and pause to visualize each step
    plt.pause(1)

plt.show()

