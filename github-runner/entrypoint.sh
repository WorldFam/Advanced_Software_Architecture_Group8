#!/bin/bash

cd /home/docker/actions-runner

# Configure the runner in the background
./config.sh --url https://github.com/WorldFam/Advanced_Software_Architecture_Group8 --token ANKVGK3NWV2CW33Z4WF42ULFL7YYK &

# Wait for the background process to finish
wait $!

# Check the exit status of the previous command
if [ $? -eq 0 ]; then
    # If the configuration was successful, run the GitHub Actions runner
    ./run.sh
else
    # If the configuration failed, exit with an error message
    echo "Runner configuration failed. Exiting..."
    exit 1
fi