import sys
import os
sys.path.append((os.path.join(os.path.dirname(__file__), '..')))
from main import factorial
def test_case():
    assert factorial(3) == 6