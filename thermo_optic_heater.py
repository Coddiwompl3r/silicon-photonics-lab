import gdsfactory as gf

# Call a straight waveguide that has a metal heating element and electrical routing pads built in.
c = gf.components.straight_heater_metal(length=50)

c.write_gds("thermo_optic_heater.gds")

try:
    c.show()
except Exception:
    print("Heater saved! Open 'thermo_optic_heater.gds' in KLayout.")