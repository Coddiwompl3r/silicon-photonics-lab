import gdsfactory as gf

# 1. Recreate your custom circuit canvas
c = gf.Component("filtered_mzi_circuit")

# Drop in the Ring and MZI
ring = c << gf.components.ring_single(radius=10)
mzi = c << gf.components.mzi(length_x=50, length_y=10)

# Move the MZI and route them together
mzi.movex(50)
route = gf.routing.get_route(ring.ports['o2'], mzi.ports['o1'])
c.add(route.references)

# THE FIX: Expose the unconnected internal ports to the outer canvas.
# "o1" is standard for input, "o2" is standard for output.
c.add_port("o1", port=ring.ports['o1'])
c.add_port("o2", port=mzi.ports['o2'])

# 2. THE FINAL PIECE: Add Grating Couplers
# Now that the master canvas has official ports, the software knows exactly where to route.
circuit_with_io = gf.routing.add_fiber_array(c)

# 3. Save the completed layout
circuit_with_io.write_gds("full_circuit_with_io.gds")

try:
    circuit_with_io.show()
except Exception:
    print("Full I/O circuit saved! Open 'full_circuit_with_io.gds' in KLayout.")