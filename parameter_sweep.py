import gdsfactory as gf
import gplugins.gmeep as gm
import matplotlib.pyplot as plt
import numpy as np

# 1. Activate the PDK
gf.gpdk.PDK.activate()

# 2. Define the sweep parameters
# We will test lengths from 10 microns to 20 microns in steps of 2
lengths_to_test = [10, 12, 14, 16, 18, 20]
cross_port_power = []

print("Initiating FDTD Parameter Sweep...")
print("WARNING: This will sequentially simulate multiple layouts. Your CPU will max out.")
print("Go grab a coffee. Stand by...\n")

# 3. The Optimization Loop
for L in lengths_to_test:
    print(f"[+] Simulating Coupler: Length = {L} µm")
    
    # Generate the physical component
    c = gf.components.coupler(length=L, gap=0.2)

    # Run the FDTD extraction
    sp = gm.write_sparameters_meep(
        component=c,
        resolution=20,
        run=True
    )

    # 4. Data Extraction
    # The simulation returns a massive array of wavelengths. 
    # We only care about the standard telecom wavelength: 1.55 microns (1550nm).
    wavelengths = sp["wavelengths"]
    idx_1550 = (np.abs(wavelengths - 1.55)).argmin()

    # Extract the complex transmission data from Port 1 to Port 4 (The Cross Port)
    # The string 'o4@0,o1@0' means: Output Port 4 (Mode 0) from Input Port 1 (Mode 0)
    s41 = sp["o4@0,o1@0"][idx_1550]
    
    # Convert the raw transmission into Decibels (dB)
    power_db = 20 * np.log10(np.abs(s41))

    print(f"    -> Cross Port Power at 1550nm: {power_db:.2f} dB\n")
    cross_port_power.append(power_db)

# 5. Plot the Final Sweep Curve
plt.figure(figsize=(8, 5))
plt.plot(lengths_to_test, cross_port_power, marker='o', linewidth=2, color='blue')

# Draw a red target line at exactly -3.01 dB (The mathematical 50/50 split)
plt.axhline(-3.01, color='red', linestyle='--', label='Perfect 50/50 Target (-3.01 dB)')

plt.title("Directional Coupler Parameter Sweep (Wavelength = 1550nm)")
plt.xlabel("Coupling Length (µm)")
plt.ylabel("Cross Port Transmission (dB)")
plt.legend()
plt.grid(True)

# Save the graph automatically for your GitHub portfolio
plt.savefig("coupler_sweep_results.png")
plt.show()