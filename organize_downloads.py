import shutil
from pathlib import Path

categories = {
    # Images
    "jpg": "Images", "jpeg": "Images", "png": "Images",
    "gif": "Images", "heic": "Images", "webp": "Images", "svg": "Images",

    # Documents
    "pdf": "Documents", "doc": "Documents", "docx": "Documents",
    "txt": "Documents", "rtf": "Documents", "pages": "Documents",

    # Spreadsheets
    "xls": "Spreadsheets", "xlsx": "Spreadsheets", "csv": "Spreadsheets",
    "numbers": "Spreadsheets",

    # Presentations
    "ppt": "Presentations", "pptx": "Presentations", "key": "Presentations",

    # Audio
    "mp3": "Audio", "wav": "Audio", "m4a": "Audio", "aac": "Audio",

    # Video
    "mp4": "Video", "mov": "Video", "avi": "Video", "mkv": "Video",

    # Archives
    "zip": "Archives", "rar": "Archives", "tar": "Archives", "gz": "Archives",

    # Installers
    "dmg": "Installers", "pkg": "Installers",
}

folder = Path.home() / "Downloads"
for item in folder.iterdir():
    if item.is_file():
        extension = item.suffix.replace(".", "").lower()
        category = categories.get(extension, "Other")
        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(item), str(target_folder / item.name))
        print(f"Moved {item.name} into {target_folder}")
