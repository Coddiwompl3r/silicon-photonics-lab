import gdsfactory as gf

# Generate an MZI. 
# length_x controls the horizontal length of the arms (50 microns).
# length_y controls the vertical separation distance (10 microns).
c = gf.components.mzi(length_x=50, length_y=10)

# Save it to your portfolio folder
c.write_gds("mzi_logic_gate.gds")

try:
    c.show()
except Exception:
    print("MZI logic gate saved! Open 'mzi_logic_gate.gds' manually in KLayout.")