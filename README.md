# DC Circuit Analyzer

A Python-based tool for analyzing simple DC (Direct Current) circuits using fundamental electrical engineering principles including Ohm's Law, Kirchhoff's Laws, and power calculations.

## About This Project

This project demonstrates my understanding of:
- **Electrical engineering fundamentals** (Ohm's Law, series/parallel circuits, power)
- **Python programming** (Object-Oriented Programming, functions, error handling)
- **Software engineering practices** (modular design, testing, documentation)

As an aspiring Electrical and Computer Engineering student, I built this tool to automate the circuit calculations I frequently perform by hand, showcasing how programming can solve real engineering problems.

## Features

| Feature | Description |
|---------|-------------|
| Ohm's Law Calculator | Solve for V, I, or R given any two values |
| Series Resistance | Calculate total resistance for series circuits |
| Parallel Resistance | Calculate total resistance for parallel circuits |
| Power Calculator | Calculate power using P=VI, P=I²R, or P=V²/R |
| Voltage Divider | Design and calculate voltage divider outputs |
| Current Divider | Calculate current distribution in parallel branches |
| Full Circuit Analysis | Complete analysis with per-component breakdown |

## How to Run

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

### Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/circuit-analyzer.git

# Navigate to the project directory
cd circuit-analyzer
```

### Running the Program

```bash
# Run the interactive analyzer
python circuit_analyzer.py
```

### Running Examples

```bash
# See practical examples with real-world scenarios
python examples/sample_circuits.py
```

### Running Tests

```bash
# Run the test suite to verify all calculations
python tests/test_circuit.py
```

## How It Works

### Core Concepts

**Ohm's Law:** The fundamental relationship between voltage (V), current (I), and resistance (R):
```
V = I × R
```

**Series Circuits:** Resistors in series add directly:
```
R_total = R1 + R2 + R3 + ...
```

**Parallel Circuits:** Resistors in parallel combine as reciprocals:
```
1/R_total = 1/R1 + 1/R2 + 1/R3 + ...
```

**Power:** Electrical power can be calculated three ways:
```
P = V × I P = I² × R P = V² / R
```

### Code Structure

```
circuit-analyzer/
circuit_analyzer.py # Main program with CircuitAnalyzer class
examples/
sample_circuits.py # Practical usage examples
tests/
test_circuit.py # Unit tests (13 tests)
requirements.txt # Dependencies (none required)
README.md # This file
```

## Sample Output

```
============================================================
       DC CIRCUIT ANALYZER
============================================================

Select an analysis to perform:
----------------------------------------
  1. Ohm's Law Calculator (V = IR)
  2. Series Resistance
  3. Parallel Resistance
  4. Power Calculator
  5. Voltage Divider
  6. Current Divider
  7. Full Circuit Analysis
  8. Exit
----------------------------------------

  Enter your choice (1-8): 1

  Ohm's Law: V = I × R
  Enter the two known values (press Enter to skip unknown):

  Voltage (V) [press Enter if unknown]: 12
  Current (A) [press Enter if unknown]:
  Resistance (Ω) [press Enter if unknown]: 4

     Results:
     Voltage = 12.0 V
     Current = 3.0 A
     Resistance = 4.0 Ω
```

## What I Learned

- How to translate electrical engineering formulas into clean Python code
- Object-Oriented Programming (classes, methods, encapsulation)
- Input validation and error handling for robust applications
- Writing comprehensive unit tests to verify calculations
- Organizing code into modular, maintainable components

## Future Improvements

- Add AC circuit analysis (impedance, reactance, phase angles)
- Implement Kirchhoff's Current and Voltage Laws for complex circuits
- Add a graphical interface using Tkinter or PyQt
- Support for capacitors and inductors
- Circuit diagram visualization

## References

- Ohm's Law: [Wikipedia](https://en.wikipedia.org/wiki/Ohm%27s_law)
- Series and Parallel Circuits: [All About Circuits](https://www.allaboutcircuits.com/)
- Python Documentation: [python.org](https://docs.python.org/3/)

## Author

**[Student Name]** — Aspiring Electrical & Computer Engineering Student

---

*Built with Python 3 | No external dependencies required*