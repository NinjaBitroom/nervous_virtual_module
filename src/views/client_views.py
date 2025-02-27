"""."""

import io

import sounddevice as sd  # type: ignore[]
import soundfile as sf  # type: ignore[]
from websockets.asyncio.client import connect


async def client_view() -> None:
    """."""
    async with connect("ws://localhost:8000/nervous/api/ws") as ws:
        while True:
            response = await ws.recv(decode=False)
            data, samplerate = sf.read(io.BytesIO(response))  # type: ignore[]
            sd.play(data, samplerate)  # type: ignore[]
            sd.wait()
