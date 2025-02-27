"""."""

from typing import Any

import sounddevice as sd  # type: ignore[]
from rich import print as rprint

from src.views.client_views import client_view


async def create_app() -> None:
    """."""
    device: dict[str, Any]
    for device in sd.query_devices():  # type: ignore[]
        if device["max_output_channels"] > 0:
            index: int = device["index"]
            name: str = device["name"]
            hostapi: dict[str, Any] = sd.query_hostapis(device["hostapi"])  # type: ignore[]
            hostapi_name: str = hostapi["name"]
            default = (
                "*"
                if index == sd.query_devices(kind="output")["index"]  # type: ignore[]
                else ""
            )
            rprint(f"{index}{default}: {name} [{hostapi_name}]")
    choice = input("Choose device: ")
    sd.default.device = int(choice)  # type: ignore[]
    await client_view()
