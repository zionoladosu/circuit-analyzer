"""
Sample Circuit Analyses
========================
Demonstrates the Circuit Analyzer with practical examples.
Run with: python3 examples/sample_circuits.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from circuit_analyzer import CircuitAnalyzer, Resistor

def example_1_led_circuit():
    """Example: Calculating resistor needed for an LED circuit."""
    print("=" * 55)
    print(" Example 1: LED Current-Limiting Resistor")
    print("=" * 55)
    print()
    print(" Scenario: You want to power a red LED with a 9V battery.")
    print(" The LED has a forward voltage of 2V and needs 20mA.")
    print(" What resistor do you need?")
    print()

    v_supply = 9.0 # 9V battery
    v_led = 2.0 # LED forward voltage
    i_desired = 0.020 # 20mA

    # Voltage across resistor = V_supply - V_LED
    v_resistor = v_supply - v_led

    # Use Ohm's Law to find resistance
    result = CircuitAnalyzer.ohms_law(voltage=v_resistor, current=i_desired)

    print(f" Supply Voltage : {v_supply} V")
    print(f" LED Forward Voltage: {v_led} V")
    print(f" Voltage across R : {v_resistor} V")
    print(f" Desired Current : {i_desired*1000} mA")
    print(f" Required Resistor: {result['resistance']} Ω")
    print(f" (Use a standard 350Ω or 360Ω resistor)")

    # Calculate power dissipated by resistor
    power = CircuitAnalyzer.calculate_power(voltage=v_resistor, current=i_desired)
    print(f" Power dissipated : {power*1000} mW")
    print()

def example_2_series_parallel():
    """Example: Mixed calculation with series and parallel."""
    print("=" * 55)
    print(" Example 2: Series vs. Parallel Comparison")
    print("=" * 55)
    print()
    print(" Three resistors: 220Ω, 470Ω, 1000Ω")
    print(" Connected to a 12V source.")
    print()

    r_values = [220, 470, 1000]
    resistors = [Resistor(r, f"R{i+1}") for i, r in enumerate(r_values)]
    analyzer = CircuitAnalyzer()

    # Series
    r_series = analyzer.series_resistance(resistors)
    i_series = round(12 / r_series, 4)
    p_series = analyzer.calculate_power(voltage=12, resistance=r_series)

    print(" SERIES Configuration:")
    print(f" R_total = {r_values[0]} + {r_values[1]} + {r_values[2]} = {r_series} Ω")
    print(f" I_total = 12V / {r_series}Ω = {i_series} A ({round(i_series*1000, 2)} mA)")
    print(f" P_total = {p_series} W")
    print()

    # Parallel
    r_parallel = analyzer.parallel_resistance(resistors)
    i_parallel = round(12 / r_parallel, 4)
    p_parallel = analyzer.calculate_power(voltage=12, resistance=r_parallel)

    print(" PARALLEL Configuration:")
    print(f" R_total = {r_values[0]} ∥ {r_values[1]} ∥ {r_values[2]} = {r_parallel} Ω")
    print(f" I_total = 12V / {r_parallel}Ω = {i_parallel} A ({round(i_parallel*1000, 2)} mA)")
    print(f" P_total = {p_parallel} W")
    print()

    print(f" Comparison:")
    print(f" Series draws {round(i_series*1000, 2)} mA — Parallel draws {round(i_parallel*1000, 2)} mA")
    print(f" Parallel draws {round(i_parallel/i_series, 1)}x more current!")
    print()

def example_3_voltage_divider():
    """Example: Designing a voltage divider for a sensor."""
    print("=" * 55)
    print(" Example 3: Voltage Divider for a 3.3V Sensor")
    print("=" * 55)
    print()
    print(" Scenario: You have a 5V Arduino output but need 3.3V")
    print(" for a sensor input. Design a voltage divider.")
    print()

    v_source = 5.0
    # Using R1 = 1.7kΩ, R2 = 3.3kΩ gives approximately 3.3V
    r1 = 1700
    r2 = 3300

    v_out = CircuitAnalyzer.voltage_divider(v_source, r1, r2)

    print(f" V_source = {v_source} V")
    print(f" R1 = {r1} Ω (1.7 kΩ)")
    print(f" R2 = {r2} Ω (3.3 kΩ)")
    print(f" V_out = {v_source} × ({r2} / ({r1} + {r2})) = {v_out} V")
    print()
    print(f" This gives us {v_out}V — {' Safe' if v_out <= 3.3 else ' Too high'} for the 3.3V sensor!")
    print()

if __name__ == "__main__":
    print()
    example_1_led_circuit()
    example_2_series_parallel()
    example_3_voltage_divider()
    print("=" * 55)
    print(" All examples completed successfully!")
    print("=" * 55)
