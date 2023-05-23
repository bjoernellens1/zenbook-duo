#!/bin/bash

# Step 1: Copy Python script
cp sync-sp-brightness.py ~/sync-sp-brightness.py
cp screenpad.py ~/screenpad.py

# Install dependencies
pip3 install watchdog

# Step 2: Create systemd service unit file
cat <<EOF | sudo tee /etc/systemd/system/sync-sp-brightness.service > /dev/null
[Unit]
Description=Run sync-sp-brightness at login
After=network.target

[Service]
User=bjoern
ExecStart=/usr/bin/python3 /home/bjoern/sync-sp-brightness.py

[Install]
WantedBy=default.target
EOF

# Step 3: Set permissions
sudo chmod 644 /etc/systemd/system/sync-sp-brightness.service

# Step 4: Enable the service
sudo systemctl enable sync-sp-brightness.service

# Step 5: Start the service
sudo systemctl start sync-sp-brightness.service

echo "The service has been created and started."

