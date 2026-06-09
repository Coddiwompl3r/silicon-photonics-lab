import gdsfactory as gf

# Create a directional coupler. 
# length = how long they run parallel. gap = the distance between them.
c = gf.components.coupler(length=25, gap=0.2)

c.write_gds("directional_coupler.gds")

try:
    c.show()
except Exception:
    print("Coupler saved! Open 'directional_coupler.gds' in KLayout.")