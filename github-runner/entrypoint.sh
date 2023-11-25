#!/bin/bash

cd /home/docker/actions-runner

# Check if the runner is already configured
if [ -f ".runner" ]; then
    echo "Runner is already configured."
else
    # Prompt the user to insert REPO_URL and TOKEN
    read -p "Enter REPO_URL: " REPO_URL
    read -p "Enter TOKEN: " TOKEN

    # Configure the runner in the background
    ./config.sh --url "$REPO_URL" --token "$TOKEN" &

    # Wait for the background process to finish
    wait $!

    # Check the exit status of the previous command
    if [ $? -eq 0 ]; then
        echo "Runner configuration successful."
        touch .runner  # Create a marker file to indicate that the runner is configured
    else
        # If the configuration failed, exit with an error message
        echo "Runner configuration failed. Exiting..."
        exit 1
    fi
fi

# Check if the runner is already running
if pgrep -f "run.sh" > /dev/null; then
    echo "Runner is already running."
else
    # If the runner is not running, start it
    ./run.sh
fi