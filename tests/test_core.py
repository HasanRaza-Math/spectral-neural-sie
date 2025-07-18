from src.core import SpectralSolver

def test_solver_initialization():
    """Test if the solver initializes correctly"""
    solver = SpectralSolver()
    assert solver.model is not None

def test_model_structure():
    """Verify basic model architecture"""
    solver = SpectralSolver()
    assert len(solver.model) == 3  # Should have 3 layers
