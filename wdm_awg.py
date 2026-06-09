import gdsfactory as gf

# 1. We are going to call the built-in Arrayed Waveguide Grating (AWG) component.
# This is a massive, complex component used in commercial telecom and data centers.
awg_component = gf.components.awg()

# 2. Save the layout physically to your portfolio folder
awg_component.write_gds("wdm_awg.gds")

# 3. Try to show it in the live viewer
try:
    awg_component.show()
except Exception:
    print("AWG layout saved! Open 'wdm_awg.gds' manually in KLayout.")