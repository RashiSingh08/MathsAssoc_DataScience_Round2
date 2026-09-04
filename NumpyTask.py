import re
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "equations.txt"

num_vars = 100
A = np.zeros((num_vars, num_vars))
B = np.zeros(num_vars)

# Function to recognize implicit multiplication and variables
# This was the hardest part and where I had to use AI to code. I knew we have to break these at = 
# But, how to extract the coefficients and variables from the left-hand side of the equation was tricky. 
# AI used regex to find patterns like "-16x1" and extract both the coefficient and the variable index.
# I will know how to do this soon, now that I have seen it once.

def parse_equation(equation_str, row_idx):
    if '=' not in equation_str:
        return
    lhs, rhs = equation_str.split('=')
    
    B[row_idx] = float(rhs.strip())
    
    pattern = r"([+-]?\s*\d*)x(\d+)"
    matches = re.findall(pattern, lhs)
    
    for coeff_str, var_idx_str in matches:
        var_idx = int(var_idx_str) - 1 
        coeff_str = coeff_str.replace(" ", "")

# Dependent coding. I gave detailed instructions as I knew what to do.
# But, I knew I needed help with the syntax to extract these.
        # Handle cases where coefficient is just "-" or "+" or empty (implied 1)
        if coeff_str in ["", "+"]:
            coeff = 1.0
        elif coeff_str == "-":
            coeff = -1.0
        else:
            coeff = float(coeff_str)
            
        A[row_idx, var_idx] = coeff


with open(file_path, 'r') as f:
    equations = f.readlines()
    for idx, line in enumerate(equations):
        if line.strip():
            clean_line = line.replace("[source: 1]", "").strip()
            parse_equation(clean_line, idx)

# Here is where I start coding independently again. 
# I know how to do the matrix inversion and multiplication.
try:
    A_inv = np.linalg.inv(A)
    
    X = np.dot(A_inv, B)
    
    for i, val in enumerate(X):
        print(f"x{i+1} = {val:.4f}")
        
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted. Please check the equations.")