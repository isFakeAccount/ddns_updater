from typing import Any

import requests


def get_public_ip(ipv6: bool = False) -> str:
    url = "https://api64.ipify.org" if ipv6 else "https://api.ipify.org"
    response: dict[str, Any] = requests.get(url, params={"format": "json"}).json()
    return response.get("ip")


def replace_ip_placeholders(data: dict[str, Any]) -> dict[str, Any]:
    ipv4 = get_public_ip(ipv6=False)
    ipv6 = get_public_ip(ipv6=True)

    for key, value in data.items():
        if "ip" in key.lower():
            if value == "<ipv4>":
                data[key] = ipv4 or ""
            elif value == "<ipv6>":
                data[key] = ipv6 or ""

    return data
