# Silicon Photonics Lab & EPDA Portfolio

## Overview
This repository documents my independent exploration into the physical layer of AI compute, specifically focusing on Silicon Photonics and Co-Packaged Optics (CPO). As the energy and latency constraints of traditional copper interconnects become a bottleneck for scaling AGI, I am building a practical understanding of how data is routed and computed using light.

I am using **Python**, **gdsfactory** (an open-source Electronic Photonic Design Automation library), and **KLayout** to programmatically generate GDSII layouts for foundational optical hardware components.

## Current Layouts & Components
* **`hello_photonics.py`**: A baseline 10-micron straight optical waveguide. The fundamental highway for moving photons across a chip.
* **`ring_resonator.gds`**: A single ring resonator (10µm radius, 0.2µm gap). Designed to act as an optical filter, trapping and routing specific wavelengths of light via evanescent coupling.
* **`mzi_logic_gate.py`**: A Mach-Zehnder Interferometer (MZI). The core structure for optical logic and modulation, utilizing parallel waveguides to create constructive and destructive wave interference.

## About the Author
I am an incoming Aerospace Engineering student at the University of Central Florida (Expected Fall 2027) with a background in independent hardware operations (managing self-hosted blockchain nodes and ASIC networks) and healthcare. I am actively teaching myself layout automation and photonics physics to prepare for undergraduate research opportunities. 

**Tech Stack:** Python, GDSFactory, KLayout, Git.
