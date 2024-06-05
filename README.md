# flying-objects-simulator
A Python-based simulation of flying objects in a 2D plane with a REST API for querying object trajectories and sector snapshots.

# Flying Objects Simulator

## Description

**Flying Objects Simulator** is a Python-based simulation application that models the movement of flying objects in a 2D plane. The world is divided into sectors, and objects move along quadratic Bézier curves. The simulation logs object positions and other relevant data, and provides a REST API to query this data.

## Features

- Simulates 500 flying objects with random trajectories and speeds.
- Objects move on a quadratic Bézier curve from an origin point through a waypoint to a destination point.
- REST API for querying object trajectories and sector snapshots.
- Data logging with detailed object information at regular intervals.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/amrahhh/flying-objects-simulator.git
    cd flying-objects-simulator
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Generate Simulation Data
chmod +x run.sh
Run the bash script to generate data:
./run.sh
