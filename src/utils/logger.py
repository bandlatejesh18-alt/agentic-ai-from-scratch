"""
Application logger configuration.
"""

from pathlib import Path
import logging

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)