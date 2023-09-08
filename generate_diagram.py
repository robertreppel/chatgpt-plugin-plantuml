import os
import asyncio
import tempfile
import shutil
import aiofiles

async def generate_diagram(plantuml_code: str) -> str:
    # Use aiofiles for asynchronous file operations
    async with aiofiles.open(tempfile.mktemp(suffix=".txt"), mode='wb') as temp:
        temp_filename = temp.name
        await temp.write(plantuml_code.encode('utf-8'))

    # Correct the output filename
    output_filename = temp_filename.replace('.txt', '.png')

    # Generate the diagram using PlantUML
    plantuml_path = "plantuml.jar"  # Update this path to your PlantUML jar location
    command = ['java', '-jar', plantuml_path, '-tpng', temp_filename, '-o', os.path.dirname(output_filename)]

    # Use asyncio to run the subprocess command asynchronously
    process = await asyncio.create_subprocess_exec(*command)
    await process.communicate()

    # Clean up the temporary text file
    os.remove(temp_filename)

    if not os.path.exists(output_filename):
        raise FileNotFoundError(f"Expected output file {output_filename} not found.")

    # Copy the generated file to /static/diagrams
    destination_path = os.path.join('static', 'diagrams', os.path.basename(output_filename))
    shutil.copy(output_filename, destination_path)

    # Clean up the original generated file
    os.remove(output_filename)

    return destination_path
