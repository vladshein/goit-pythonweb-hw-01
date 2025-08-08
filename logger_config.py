# logger
import logging

# Configure logging once
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Optional: expose a named logger
logger = logging.getLogger("my_project")
