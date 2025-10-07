from pathlib import Path

# D:\Dima\Python_Suren\Projects\fastapi-url-shortener\url-shortener\core\config.py
BASE_DIR = Path(__file__).resolve().parent.parent
SHORT_URLS_STORAGE_FILEPATH = BASE_DIR / "short-urls.json"
