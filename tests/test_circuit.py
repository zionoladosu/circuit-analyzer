"""
Unit Tests for Circuit Analyzer
================================
Tests all core functions to verify correctness of calculations.
Run with: python3 -m pytest tests/test_circuit.py -v
Or: python3 tests/test_circuit.py
"""

import sys
import os

# Add parent directory to path so we can import circuit_analyzer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from circuit_analyzer import CircuitAnalyzer, Resistor

def test_ohms_law_find_voltage():
    """Test: V = I × R → V = 2A × 5Ω = 10V"""
    result = CircuitAnalyzer.ohms_law(current=2, resistance=5)
    assert result["voltage"] == 10.0
    assert result["current"] == 2.0
    assert result["resistance"] == 5.0
    print(" Ohm's Law (find voltage): PASSED")

def test_ohms_law_find_current():
    """Test: I = V / R → I = 12V / 4Ω = 3A"""
    result = CircuitAnalyzer.ohms_law(voltage=12, resistance=4)
    assert result["current"] == 3.0
    print(" Ohm's Law (find current): PASSED")

def test_ohms_law_find_resistance():
    """Test: R = V / I → R = 9V / 3A = 3Ω"""
    result = CircuitAnalyzer.ohms_law(voltage=9, current=3)
    assert result["resistance"] == 3.0
    print(" Ohm's Law (find resistance): PASSED")

def test_series_resistance():
    """Test: R_total = 100 + 200 + 300 = 600Ω"""
    resistors = [Resistor(100), Resistor(200), Resistor(300)]
    total = CircuitAnalyzer.series_resistance(resistors)
    assert total == 600.0
    print(" Series Resistance: PASSED")

def test_series_resistance_with_floats():
    """Test series resistance with plain float values."""
    total = CircuitAnalyzer.series_resistance([10.5, 20.3, 30.2])
    assert total == 61.0
    print(" Series Resistance (floats): PASSED")

def test_parallel_resistance_two():
    """Test: Two 100Ω resistors in parallel = 50Ω"""
    resistors = [Resistor(100), Resistor(100)]
    total = CircuitAnalyzer.parallel_resistance(resistors)
    assert total == 50.0
    print(" Parallel Resistance (two equal): PASSED")

def test_parallel_resistance_three():
    """Test: 100Ω ∥ 200Ω ∥ 300Ω ≈ 54.5455Ω"""
    resistors = [Resistor(100), Resistor(200), Resistor(300)]
    total = CircuitAnalyzer.parallel_resistance(resistors)
    assert abs(total - 54.5455) < 0.001
    print(" Parallel Resistance (three): PASSED")

def test_power_from_voltage_current():
    """Test: P = V × I = 12V × 2A = 24W"""
    power = CircuitAnalyzer.calculate_power(voltage=12, current=2)
    assert power == 24.0
    print(" Power (V×I): PASSED")

def test_power_from_current_resistance():
    """Test: P = I² × R = 3² × 10 = 90W"""
    power = CircuitAnalyzer.calculate_power(current=3, resistance=10)
    assert power == 90.0
    print(" Power (I²R): PASSED")

def test_power_from_voltage_resistance():
    """Test: P = V² / R = 12² / 6 = 24W"""
    power = CircuitAnalyzer.calculate_power(voltage=12, resistance=6)
    assert power == 24.0
    print(" Power (V²/R): PASSED")

def test_voltage_divider():
    """Test: V_out = 10V × (2000 / (1000 + 2000)) = 6.6667V"""
    v_out = CircuitAnalyzer.voltage_divider(10, 1000, 2000)
    assert abs(v_out - 6.6667) < 0.001
    print(" Voltage Divider: PASSED")

def test_current_divider():
    """Test: I_R1 = 5A × (30 / (10 + 30)) = 3.75A"""
    i_r1 = CircuitAnalyzer.current_divider(5, 10, 30)
    assert i_r1 == 3.75
    print(" Current Divider: PASSED")

def test_resistor_invalid():
    """Test that invalid resistance raises ValueError."""
    try:
        Resistor(-5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print(" Invalid Resistor Validation: PASSED")

def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 50)
    print(" CIRCUIT ANALYZER - TEST SUITE")
    print("=" * 50 + "\n")

    test_ohms_law_find_voltage()
    test_ohms_law_find_current()
    test_ohms_law_find_resistance()
    test_series_resistance()
    test_series_resistance_with_floats()
    test_parallel_resistance_two()
    test_parallel_resistance_three()
    test_power_from_voltage_current()
    test_power_from_current_resistance()
    test_power_from_voltage_resistance()
    test_voltage_divider()
    test_current_divider()
    test_resistor_invalid()

    print("\n" + "=" * 50)
    print(" ALL 13 TESTS PASSED ")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    run_all_tests()
