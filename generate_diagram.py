import os
import asyncio
import aiofiles
from plantuml import PlantUML
import requests


async def generate_diagram(plantuml_code: str) -> str:
    # Configure the server URL from an environment variable, or default to the public server
    server_url = os.environ.get('PLANTUML_SERVER_URL', 'http://www.plantuml.com/plantuml/png/')
    
    # Create a PlantUML instance
    puml = PlantUML(url=server_url)

    # Get the PNG diagram as bytes
    diagram_bytes = puml.processes(plantuml_code)

    # Generate a destination path
    destination_path = os.path.join('static', 'diagrams', "diagram_{}.png".format(hash(plantuml_code)))

    # Use aiofiles to save the diagram asynchronously
    async with aiofiles.open(destination_path, 'wb') as f:
        await f.write(diagram_bytes)

    return destination_path
