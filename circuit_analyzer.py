"""
Circuit Analyzer - A Simple DC Circuit Analysis Tool
=====================================================
Analyzes DC circuits using Ohm's Law, calculates series and parallel
resistance, voltage, current, and power for basic circuit configurations.

Author: Zion Oladosu
Purpose: Demonstrating Python programming skills and understanding of
         fundamental electrical engineering concepts.
"""

import math

class Resistor:
    """Represents a single resistor component."""

    def __init__(self, resistance, label=None):
        """
        Initialize a Resistor.

        Args:
            resistance (float): Resistance value in Ohms (must be positive).
            label (str, optional): A label for the resistor (e.g., 'R1').
        """
        if resistance <= 0:
            raise ValueError("Resistance must be a positive number.")
        self.resistance = resistance
        self.label = label if label else f"R({resistance}Ω)"

    def __repr__(self):
        return f"{self.label} = {self.resistance} Ω"

class CircuitAnalyzer:
    """Analyzes basic DC circuits using fundamental electrical laws."""

    @staticmethod
    def ohms_law(voltage=None, current=None, resistance=None):
        """
        Apply Ohm's Law (V = I × R) to find the missing value.

        Provide exactly two of the three parameters.

        Args:
            voltage (float, optional): Voltage in Volts (V).
            current (float, optional): Current in Amps (A).
            resistance (float, optional): Resistance in Ohms (Ω).

        Returns:
            dict: All three values (voltage, current, resistance).
        """
        provided = sum(x is not None for x in [voltage, current, resistance])
        if provided != 2:
            raise ValueError("Provide exactly two of: voltage, current, resistance.")

        if voltage is None:
            voltage = current * resistance
        elif current is None:
            if resistance == 0:
                raise ValueError("Resistance cannot be zero when solving for current.")
            current = voltage / resistance
        elif resistance is None:
            if current == 0:
                raise ValueError("Current cannot be zero when solving for resistance.")
            resistance = voltage / current

        return {
            "voltage": round(voltage, 4),
            "current": round(current, 4),
            "resistance": round(resistance, 4)
        }

    @staticmethod
    def series_resistance(resistors):
        """
        Calculate total resistance for resistors connected in series.

        In series: R_total = R1 + R2 + R3 + ...

        Args:
            resistors (list): List of Resistor objects or resistance values (floats).

        Returns:
            float: Total resistance in Ohms.
        """
        if not resistors:
            raise ValueError("Must provide at least one resistor.")

        total = 0
        for r in resistors:
            value = r.resistance if isinstance(r, Resistor) else r
            if value <= 0:
                raise ValueError("All resistance values must be positive.")
            total += value

        return round(total, 4)

    @staticmethod
    def parallel_resistance(resistors):
        """
        Calculate total resistance for resistors connected in parallel.

        In parallel: 1/R_total = 1/R1 + 1/R2 + 1/R3 + ...

        Args:
            resistors (list): List of Resistor objects or resistance values (floats).

        Returns:
            float: Total resistance in Ohms.
        """
        if not resistors:
            raise ValueError("Must provide at least one resistor.")

        inverse_sum = 0
        for r in resistors:
            value = r.resistance if isinstance(r, Resistor) else r
            if value <= 0:
                raise ValueError("All resistance values must be positive.")
            inverse_sum += 1.0 / value

        return round(1.0 / inverse_sum, 4)

    @staticmethod
    def calculate_power(voltage=None, current=None, resistance=None):
        """
        Calculate electrical power using available values.

        Power formulas:
            P = V × I
            P = I² × R
            P = V² / R

        Args:
            voltage (float, optional): Voltage in Volts.
            current (float, optional): Current in Amps.
            resistance (float, optional): Resistance in Ohms.

        Returns:
            float: Power in Watts.
        """
        if voltage is not None and current is not None:
            power = voltage * current
        elif current is not None and resistance is not None:
            power = (current ** 2) * resistance
        elif voltage is not None and resistance is not None:
            if resistance == 0:
                raise ValueError("Resistance cannot be zero.")
            power = (voltage ** 2) / resistance
        else:
            raise ValueError("Provide at least two of: voltage, current, resistance.")

        return round(power, 4)

    @staticmethod
    def voltage_divider(v_source, r1, r2):
        """
        Calculate output voltage of a voltage divider circuit.

        V_out = V_source × (R2 / (R1 + R2))

        Args:
            v_source (float): Source voltage in Volts.
            r1 (float): First resistor value in Ohms.
            r2 (float): Second resistor value in Ohms.

        Returns:
            float: Output voltage in Volts.
        """
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Resistance values must be positive.")
        if v_source < 0:
            raise ValueError("Source voltage must be non-negative.")

        v_out = v_source * (r2 / (r1 + r2))
        return round(v_out, 4)

    @staticmethod
    def current_divider(i_total, r1, r2):
        """
        Calculate current through R1 in a two-resistor parallel circuit.

        I_R1 = I_total × (R2 / (R1 + R2))

        Args:
            i_total (float): Total current entering the parallel combination (A).
            r1 (float): Resistor through which current is calculated (Ω).
            r2 (float): The other resistor in parallel (Ω).

        Returns:
            float: Current through R1 in Amps.
        """
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Resistance values must be positive.")

        i_r1 = i_total * (r2 / (r1 + r2))
        return round(i_r1, 4)

def display_banner():
    """Display the program banner."""
    print("=" * 60)
    print(" DC CIRCUIT ANALYZER")
    print(" Electrical & Computer Engineering Tool")
    print("=" * 60)
    print()

def display_menu():
    """Display the main menu options."""
    print("Select an analysis to perform:")
    print("-" * 40)
    print(" 1. Ohm's Law Calculator (V = IR)")
    print(" 2. Series Resistance")
    print(" 3. Parallel Resistance")
    print(" 4. Power Calculator")
    print(" 5. Voltage Divider")
    print(" 6. Current Divider")
    print(" 7. Full Circuit Analysis")
    print(" 8. Exit")
    print("-" * 40)

def get_float_input(prompt):
    """Safely get a float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(" Please enter a valid number.")

def get_positive_float(prompt):
    """Get a positive float input from the user."""
    while True:
        value = get_float_input(prompt)
        if value > 0:
            return value
        print(" Value must be positive.")

def get_resistor_list():
    """Get a list of resistor values from the user."""
    while True:
        try:
            n = int(input(" How many resistors? "))
            if n < 1:
                print(" Need at least 1 resistor.")
                continue
            break
        except ValueError:
            print(" Please enter a whole number.")

    resistors = []
    for i in range(n):
        value = get_positive_float(f" Enter R{i+1} value (Ω): ")
        resistors.append(Resistor(value, f"R{i+1}"))
    return resistors

def run_ohms_law():
    """Interactive Ohm's Law calculation."""
    print("\n Ohm's Law: V = I × R")
    print(" Enter the two known values (press Enter to skip unknown):\n")

    v_input = input(" Voltage (V) [press Enter if unknown]: ").strip()
    i_input = input(" Current (A) [press Enter if unknown]: ").strip()
    r_input = input(" Resistance (Ω) [press Enter if unknown]: ").strip()

    voltage = float(v_input) if v_input else None
    current = float(i_input) if i_input else None
    resistance = float(r_input) if r_input else None

    analyzer = CircuitAnalyzer()
    result = analyzer.ohms_law(voltage=voltage, current=current, resistance=resistance)

    print("\n Results:")
    print(f" Voltage = {result['voltage']} V")
    print(f" Current = {result['current']} A")
    print(f" Resistance = {result['resistance']} Ω")

def run_series():
    """Interactive series resistance calculation."""
    print("\n Series Circuit: R_total = R1 + R2 + R3 + ...")
    resistors = get_resistor_list()

    analyzer = CircuitAnalyzer()
    total = analyzer.series_resistance(resistors)

    print(f"\n Total Series Resistance = {total} Ω")
    print(f" Components: {' + '.join(str(r.resistance) for r in resistors)} = {total} Ω")

def run_parallel():
    """Interactive parallel resistance calculation."""
    print("\n Parallel Circuit: 1/R_total = 1/R1 + 1/R2 + 1/R3 + ...")
    resistors = get_resistor_list()

    analyzer = CircuitAnalyzer()
    total = analyzer.parallel_resistance(resistors)

    print(f"\n Total Parallel Resistance = {total} Ω")
    print(f" Components: {' ∥ '.join(str(r.resistance) for r in resistors)} = {total} Ω")

def run_power():
    """Interactive power calculation."""
    print("\n Power Calculator (P = VI = I²R = V²/R)")
    print(" Enter two known values (press Enter to skip unknown):\n")

    v_input = input(" Voltage (V) [press Enter if unknown]: ").strip()
    i_input = input(" Current (A) [press Enter if unknown]: ").strip()
    r_input = input(" Resistance (Ω) [press Enter if unknown]: ").strip()

    voltage = float(v_input) if v_input else None
    current = float(i_input) if i_input else None
    resistance = float(r_input) if r_input else None

    analyzer = CircuitAnalyzer()
    power = analyzer.calculate_power(voltage=voltage, current=current, resistance=resistance)

    print(f"\n Power = {power} W ({power * 1000} mW)")

def run_voltage_divider():
    """Interactive voltage divider calculation."""
    print("\n Voltage Divider: V_out = V_source × (R2 / (R1 + R2))")
    v_source = get_positive_float(" Source Voltage (V): ")
    r1 = get_positive_float(" R1 (Ω): ")
    r2 = get_positive_float(" R2 (Ω): ")

    analyzer = CircuitAnalyzer()
    v_out = analyzer.voltage_divider(v_source, r1, r2)

    print(f"\n Output Voltage (V_out) = {v_out} V")
    print(f" Ratio: {round(r2/(r1+r2) * 100, 2)}% of source voltage")

def run_current_divider():
    """Interactive current divider calculation."""
    print("\n Current Divider: I_R1 = I_total × (R2 / (R1 + R2))")
    i_total = get_positive_float(" Total Current (A): ")
    r1 = get_positive_float(" R1 - target resistor (Ω): ")
    r2 = get_positive_float(" R2 - other resistor (Ω): ")

    analyzer = CircuitAnalyzer()
    i_r1 = analyzer.current_divider(i_total, r1, r2)
    i_r2 = round(i_total - i_r1, 4)

    print(f"\n Current through R1 = {i_r1} A")
    print(f" Current through R2 = {i_r2} A")

def run_full_analysis():
    """Perform a complete circuit analysis."""
    print("\n Full Circuit Analysis")
    print(" " + "-" * 40)

    v_source = get_positive_float(" Source Voltage (V): ")

    print("\n Circuit configuration:")
    print(" 1. All resistors in Series")
    print(" 2. All resistors in Parallel")
    choice = input(" Select (1 or 2): ").strip()

    resistors = get_resistor_list()
    analyzer = CircuitAnalyzer()

    if choice == "1":
        config = "Series"
        r_total = analyzer.series_resistance(resistors)
    elif choice == "2":
        config = "Parallel"
        r_total = analyzer.parallel_resistance(resistors)
    else:
        print(" Invalid choice.")
        return

    i_total = round(v_source / r_total, 4)
    p_total = analyzer.calculate_power(voltage=v_source, current=i_total)

    print("\n " + "=" * 45)
    print(f" FULL CIRCUIT ANALYSIS RESULTS")
    print(" " + "=" * 45)
    print(f" Configuration : {config}")
    print(f" Source Voltage : {v_source} V")
    print(f" Total Resistance : {r_total} Ω")
    print(f" Total Current : {i_total} A ({round(i_total*1000, 2)} mA)")
    print(f" Total Power : {p_total} W ({round(p_total*1000, 2)} mW)")
    print(" " + "-" * 45)

    # Individual resistor analysis
    print(f"\n Individual Component Analysis:")
    for r in resistors:
        if choice == "1":
            # In series: same current, different voltages
            v_r = round(i_total * r.resistance, 4)
            p_r = round(i_total * v_r, 4)
            print(f" {r.label}: V = {v_r} V, I = {i_total} A, P = {p_r} W")
        else:
            # In parallel: same voltage, different currents
            i_r = round(v_source / r.resistance, 4)
            p_r = round(v_source * i_r, 4)
            print(f" {r.label}: V = {v_source} V, I = {i_r} A, P = {p_r} W")

    print(" " + "=" * 45)

def main():
    """Main program loop."""
    display_banner()

    while True:
        display_menu()
        choice = input("\n Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                run_ohms_law()
            elif choice == "2":
                run_series()
            elif choice == "3":
                run_parallel()
            elif choice == "4":
                run_power()
            elif choice == "5":
                run_voltage_divider()
            elif choice == "6":
                run_current_divider()
            elif choice == "7":
                run_full_analysis()
            elif choice == "8":
                print("\n Thank you for using Circuit Analyzer! Goodbye.\n")
                break
            else:
                print("\n Invalid choice. Please select 1-8.")
        except ValueError as e:
            print(f"\n Error: {e}")
        except Exception as e:
            print(f"\n Unexpected error: {e}")

        print()

if __name__ == "__main__":
    main()