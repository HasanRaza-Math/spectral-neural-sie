import torch

class SpectralSolver:
    """Hybrid neural-spectral solver"""
    def __init__(self):
        self.model = self._build_model()
    
    def _build_model(self):
        return torch.nn.Sequential(
            torch.nn.Linear(1, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, 1)
        )
