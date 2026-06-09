import gdsfactory as gf

# We don't need to draw it from scratch; we call the built-in ring_single component.
# gap = distance between the straight wire and the ring (0.2 microns)
# radius = the size of the ring (10 microns)
c = gf.components.ring_single(gap=0.2, radius=10, width=0.5)

# Save the layout physically to your folder
c.write_gds("ring_resonator.gds")

# Try to show it in the live viewer
try:
    c.show()
except Exception:
    print("Saved! Open 'ring_resonator.gds' manually in KLayout.")