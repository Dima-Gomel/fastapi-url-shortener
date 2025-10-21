import logging
from pathlib import Path

# D:\Dima\Python_Suren\Projects\fastapi-url-shortener\url-shortener\core\config.py
BASE_DIR = Path(__file__).resolve().parent.parent
SHORT_URLS_STORAGE_FILEPATH = BASE_DIR / "short-urls.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

# Never store real tokens here! Only fake values
API_TOKENS: frozenset[str] = frozenset(
    {
        "nw5WZLfFvedgNGFRChgwMA",
        "9O392iVWl-ij4HYHwERmvg",
        "8IGJtbL_bAXYJ2GCHOv4JQ",
    }
)
