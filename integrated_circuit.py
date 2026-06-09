import gdsfactory as gf

# 1. Create a master blank canvas for the whole circuit
c = gf.Component("filtered_mzi_circuit")

# 2. Instantiate the components you already know
# The '<<' operator drops a reference of the component onto your canvas
ring = c << gf.components.ring_single(radius=10)
mzi = c << gf.components.mzi(length_x=50, length_y=10)

# 3. Placement
# By default, both components spawn at coordinates (0,0) right on top of each other.
# We need to physically move the MZI 50 microns to the right so they don't overlap.
mzi.movex(50)

# 4. Routing (The magic step)
# We tell the software to draw a waveguide from the Ring's output port ('o2') 
# to the MZI's input port ('o1'). 
route = gf.routing.get_route(ring.ports['o2'], mzi.ports['o1'])

# 5. Add the newly drawn route to the canvas
c.add(route.references)

# 6. Save the layout
c.write_gds("integrated_circuit.gds")

try:
    c.show()
except Exception:
    print("Circuit saved! Open 'integrated_circuit.gds' in KLayout.")