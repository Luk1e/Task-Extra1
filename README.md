# Quine Generator

This Python program demonstrates the concept of a **quine**, a program that generates its own source code. It outputs a JavaScript program, which when executed, outputs the original Python program. This process showcases self-replicating code logic across two programming languages.

## Usage Instructions

1. **Run the Python script** to generate the JavaScript code:

   ```powershell
   python solution.py | Out-File -Encoding utf8 solution.js
   ```

2. **Run the generated JavaScript file** to produce a Python file:

   ```powershell
   node solution.js | Out-File -Encoding utf8 solution2.py
   ```

3. **Compare the original Python file** (`solution.py`) and the generated Python file (`solution2.py`) to verify they are identical:
   ```powershell
   code -d solution.py solution2.py
   ```

## Explanation of the Code

1. **Python Output**: The Python program creates a string representation of its own logic and formats it into a JavaScript program.
2. **JavaScript Execution**: The generated JavaScript program outputs the original Python code using the same concept of string formatting.
3. **Comparison**: The final output Python file (`solution2.py`) is verified to match the original (`solution.py`), proving the correctness of the quine.
