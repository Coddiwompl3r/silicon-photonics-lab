# Silicon Photonics Lab & EPDA Portfolio

## Overview
This repository documents my independent exploration into the physical layer of AI compute, specifically focusing on Silicon Photonics and Co-Packaged Optics (CPO). As the energy and latency constraints of traditional copper interconnects become a bottleneck for scaling AGI, I am building a practical understanding of how data is routed and computed using light.

I am using **Python**, **gdsfactory** (an open-source Electronic Photonic Design Automation library), and **KLayout** to programmatically generate GDSII layouts for foundational optical hardware components, active modulators, and fully testable circuits.

## Current Layouts & Components

### 1. Fundamental Primitives & Logic
* **`hello_photonics.py`**: A baseline 10-micron straight optical waveguide. The fundamental highway for moving photons across a chip.
* **`ring_resonator.gds`**: A single ring resonator (10µm radius, 0.2µm gap). Designed to act as an optical filter, trapping and routing specific wavelengths of light via evanescent coupling.
* **`mzi_logic_gate.py`**: A Mach-Zehnder Interferometer (MZI). The core structure for optical logic and modulation, utilizing parallel waveguides to create constructive and destructive wave interference.

### 2. Active Components & Electro-Optic Modulation
* **`directional_coupler.py`**: A directional coupler (25µm coupling length, 0.2µm gap). The fundamental physical structure for precisely splitting and combining light via evanescent field transfer.
* **`thermo_optic_heater.py`**: A straight waveguide integrated with a metal heating element and electrical routing pads. Demonstrates thermo-optic phase shifting to actively control the refractive index of the silicon.

### 3. Integration & Testing Infrastructure
* **`integrated_circuit.py`**: An automated routing layout physically connecting a ring resonator to an MZI, demonstrating hierarchical port mapping and component integration.
* **`full_circuit_with_io.py`**: A fully testable circuit integrating grating couplers spaced at an industry-standard 127µm, enabling direct fiber array input/output testing for the routed MZI/ring system.

### 4. Commercial Scaling
* **`wdm_awg.py`**: An Arrayed Waveguide Grating (AWG). The foundational structure for Wavelength Division Multiplexing (WDM), designed to multiplex/demultiplex multiple wavelength channels to massively scale data throughput.

### 5. FDTD Physics Verification
* **`fdtd_coupler.py`**: A Finite-Difference Time-Domain (FDTD) simulation script utilizing the MIT Meep engine to extract S-parameters from the directional coupler. 
![S-Parameter Extraction](sparameter_simulation.png)
*Demonstrates physical verification of evanescent field coupling across the waveguide gap.*
* **`parameter_sweep.py`**: An automated optimization loop that iteratively simulates multiple coupler geometries. Successfully swept coupling lengths to identify the exact 17.7µm physical requirement for a perfect -3.01 dB (50/50) power split at 1550nm.
![Parameter Sweep Results](coupler_sweep_results.png)

## About the Author
I am an incoming Optics and Photonics Engineering student at the University of Central Florida (Expected Fall 2027) based in Fort Myers. My background consists of independent hardware operations, specifically managing self-hosted ASIC networks and localized computing nodes. I am actively teaching myself layout automation and photonics physics to prepare for undergraduate research opportunities in optical compute and heterogeneous integration.

**Tech Stack:** Python, GDSFactory, KLayout, Git.
