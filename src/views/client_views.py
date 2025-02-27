"""."""

import io

import sounddevice as sd  # type: ignore[]
import soundfile as sf  # type: ignore[]
from rich import print as rprint
from websockets.asyncio.client import connect


async def client_view() -> None:
    """."""
    async with connect("ws://localhost:8000/nervous/api/ws") as ws:
        rprint("Connected to server")
        while True:
            rprint("Waiting for audio from server")
            response = await ws.recv(decode=False)
            rprint("Received from server")
            data, samplerate = sf.read(io.BytesIO(response))  # type: ignore[]
            rprint("Playing audio")
            sd.play(data, samplerate)  # type: ignore[]
