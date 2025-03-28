# Autonomous Cleaning Agent with SLAM and A* Pathfinding

An autonomous grid-based cleaning agent that uses SLAM (Simultaneous Localization and Mapping) and A* pathfinding to explore and clean unknown environments. The agent dynamically prioritizes frontier exploration and ensures complete coverage of reachable cells.

![Simulation Demo](https://github.com/uzayyildiztaskan/Autonomous-Cleaning-Agent/blob/main/demos/simulation_demo_result.gif)  
*Example simulation output (replace with your own GIF/video)*

---

## Features

- 🧠 **SLAM Implementation**: Builds a memory map of obstacles and cleaned areas in real time.
- 🚀 **Reverse A\* Pathfinding**: Efficiently navigates to frontiers (unexplored boundaries) and uncleaned cells.
- 📍 **Dynamic Frontiers**: Prioritizes exploration of unknown regions while ensuring full coverage.
- 🧩 **Customizable Grids**: Choose from predefined environments (`simple`, `complex`, `large`) or provide custom start positions.
- 📊 **Visualization**: Real-time grid visualization with Matplotlib.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/autonomous-cleaning-agent.git
   cd autonomous-cleaning-agent
   ```
2. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

---

## Usage

**Basic Command**
```
python main.py [--grid_choice {simple,complex,large}] [--start_pos X Y]
```

**Defaults**
- **grid_choice:** Large
- **start_pos**
    - **simple:** 2, 3
    - **large:** 21, 2
    - **complex:** 7, 8

## Examples
Run the large grid with its default start position:
```
python main.py
```
Use the complex grid with a custom start position (7, 8):
```
python main.py --grid_choice complex --start_pos 7 8
```

Run the simple grid with default start position (2, 3):
```
python main.py --grid_choice simple
```

---

## Simulation Output
The agent's progress is visualized in real time:

- 🧱 **Obstacles:** Black cells

- 🧼 **Cleaned areas:** Light green cells

- 🤖 **Agent:** Red cell

---

## Project Structure

```
.
└── autonomous-cleaning-agent/
    ├── agents/
    │   ├── a_star_agent.py                     # Reversed A* path finding logic
    │   └── ...
    ├── environment.py                          # Grid environment and agent movement logic
    ├── enums.py                                # Enums for directions and grid states
    ├── main.py                                 # Main simulation runner
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

---

## License

License
Distributed under the MIT License.

See [LICENSE](https://github.com/uzayyildiztaskan/Autonomous-Cleaning-Agent/blob/main/LICENSE) for more information.
