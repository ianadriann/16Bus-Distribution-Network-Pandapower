# 16-Bus Distribution Network Modeling with Pandapower

This repository contains a basic example of building, simulating, and visualizing a simple 16-bus radial distribution network using the [Pandapower](https://www.pandapower.org/) Python library. The network consists of:
- One external grid connection,
- 16 distribution buses (0.4 kV),
- Radial interconnections (15 lines),
- Small loads connected to each bus.

Power flow analysis is performed to compute voltage profiles and power consumption, with interactive visualization using Plotly.

---

## 📌 Features
- Creation of a simple 16-bus radial distribution network
- Modeling of external grid source, distribution lines, and loads
- Power flow calculation using `pp.runpp()`
- Visualization of the network topology with Plotly

---

## ⚙️ Dependencies
- Python 3.x
- [pandapower](https://www.pandapower.org/)
- [plotly](https://plotly.com/)

Install dependencies:
```bash
pip install pandapower plotly
```

🚀 How to Run
Ensure Python and dependencies are installed.
Place the code file (e.g. 16bus_network.py) in your project folder.
Run the script:
```bash
python 16bus_network.py

The script will print power flow results and display a network visualization.
