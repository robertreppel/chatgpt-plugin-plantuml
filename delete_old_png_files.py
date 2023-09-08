import os
import time
import logging

logger = logging.getLogger(__name__)

async def delete_old_png_files(directory_path: str, age_threshold_minutes: int = 5):
    """
    Delete .png files in the specified directory that are older than the given age threshold.

    :param directory_path: Path to the directory to check for old files.
    :param age_threshold_minutes: Age threshold in minutes. Files older than this will be deleted.
    """
    age_threshold_seconds = age_threshold_minutes * 60  # Convert minutes to seconds
    current_time = time.time()

    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):
            file_path = os.path.join(directory_path, filename)
            
            # Ensure it's a file
            if os.path.isfile(file_path):
                # Get the file's modification time
                file_age = current_time - os.path.getmtime(file_path)
                
                # Check if the file is older than the threshold
                if file_age > age_threshold_seconds:
                    os.remove(file_path)
                    logger.info(f"Deleted {file_path}")

