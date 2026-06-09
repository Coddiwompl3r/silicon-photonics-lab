import gdsfactory as gf
import gplugins.gmeep as gm
import gplugins.common.utils.plot as plot_utils
import matplotlib.pyplot as plt

# Explicitly activate the generic Process Design Kit (PDK)
gf.gpdk.PDK.activate()

# Load the Directional Coupler 
c = gf.components.coupler(length=15, gap=0.2)

print("Initializing MIT Meep FDTD engine...")
print("Extracting S-Parameters. Your CPU will spike. Stand by...")

# Run the simulation to extract the mathematical transmission data
sp = gm.write_sparameters_meep(
    component=c,
    resolution=20,
    run=True
)

# Plot the exact decibel loss and transmission curves
plot_utils.plot_sparameters(sp)
plt.show()