#!/usr/bin/env python3

import json
from typing import Any

import requests
from platformdirs import site_config_path

from utils import replace_ip_placeholders


def load_config() -> dict[str, Any]:
    ddns_config_dir = site_config_path("ddns_updater", appauthor=False)
    ddns_config_file = ddns_config_dir / "config.json"
    if not ddns_config_file.exists():
        raise FileNotFoundError(
            "Config file not found! Make sure ~/.config/ddns_update/config.json exists."
        )

    with ddns_config_file.open("r") as fp:
        config = json.load(fp)

    if not config or "ddns_updater" not in config:
        raise ValueError("Invalid configuration format.")

    return config


def main():
    config = load_config()
    ddns_list: list[dict[str, Any]] = config["ddns_updater"]

    for entry in ddns_list:
        provider = entry.get("provider", "Unknown Provider")
        url = entry.get("update_url")
        method = entry.get("method", "GET").upper()
        params = replace_ip_placeholders(entry.get("params", {}))
        body = replace_ip_placeholders(entry.get("body", {}))

        if not url:
            print(f"Skipping {provider}: Missing update_url")
            continue

        try:
            print(f"Making a {method} request to {url} with params: {params} and body: {body}")
            response = requests.request(method, url, params=params, json=body)

            
            if response.status_code == 200:
                print(f"[{provider}] Update successful: {response.text}")
            else:
                print(
                    f"[{provider}] Update failed ({response.status_code}): {response.text}"
                )
        except requests.RequestException as e:
            print(f"[{provider}] Request error: {e}")


if __name__ == "__main__":
    main()
