#!/bin/bash

# Run the simulation script
echo "Starting the simulation..."
python3 simulation.py

if [ $? -ne 0 ]; then
    echo "Simulation script failed. Exiting."
    exit 1
fi

echo "Simulation completed successfully."

# Start the API server
echo "Starting the API server..."
python3 api.py

if [ $? -ne 0 ]; then
    echo "Failed to start the API server. Exiting."
    exit 1
fi
