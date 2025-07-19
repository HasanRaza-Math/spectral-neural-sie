import torch
from src.core import SpectralSolver
import matplotlib.pyplot as plt

def main():
    print("🔬 Spectral-Neural Solver Demo")
    
    # Initialize solver
    solver = SpectralSolver()
    print(f"Model architecture:\n{solver.model}")
    
    # Example: Plot dummy data (replace with your actual research code)
    x = torch.linspace(0, 1, 100)
    y = torch.sin(x * 2 * torch.pi)
    plt.plot(x.numpy(), y.numpy())
    plt.title("Spectral-Neural Solution")
    plt.savefig("figures/demo_output.png")  # Saves to figures/ folder

if __name__ == "__main__":
    main()
