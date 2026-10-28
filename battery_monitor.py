print("BATTERY MONITORING SYSTEM")
print("-------------------------")

voltage = float(input("Enter battery voltage (V): "))
current = float(input("Enter battery current (A): "))

power = voltage * current

print("\n--- Battery Report ---")
print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Power:", power, "W")

if voltage > 0 and current >= 0:
    print("Status: Readings entered successfully")
else:
    print("Status: Please check the readings")
