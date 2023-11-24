#!/bin/bash

cd /home/docker/actions-runner

# Configure the runner in the background
./config.sh --url "$REPO_URL" --token "$TOKEN" &

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