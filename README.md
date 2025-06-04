# DDNS Updater

DDNS Updater is a simple, systemd-based utility that periodically updates your dynamic DNS (DDNS) records. 

## Installation

Clone this repo in /usr/local/share

```bash
git clone https://github.com/isFakeAccount/ddns_updater.git
```

Change the ownership of the cloned directory by using this cmd

```bash
sudo chown -R $USER: ddns_updater
```

## Features
- Uses `systemd` to ensure periodic updates.
- Supports multiple DDNS providers via a JSON-based configuration.

## Configuration
Create a configuration file at `/etc/xdg/ddns_update/config.json` with the following format:

```json
{
    "ddns_updater": [
        {
            "provider": "<Provider Name>",
            "update_url": "<Provider Update URL>",
            "method": "GET",
            "params": {
                "key": "value"
            },
            "body": {
                "key": "value"
            }
        },
        {
            "provider": "<Provider Name>",
            "update_url": "<Provider Update URL>",
            "method": "GET",
            "params": {
                "key": "value"
            },
            "body": {
                "key": "value"
            }
        }
    ]
}
```

## Setting Up the Service

1. **Run the `add_service_files.sh` script**: 

This script will copy the necessary service and timer files to the correct systemd directory and start them.

```bash
./add_service_files.sh
```
