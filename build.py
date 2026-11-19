from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent
MEDIA_SOURCE = ROOT / "media"
PUBLIC_MEDIA = ROOT / "public" / "media"

if not MEDIA_SOURCE.is_dir():
    raise SystemExit(f"Media source directory does not exist: {MEDIA_SOURCE}")

shutil.copytree(MEDIA_SOURCE, PUBLIC_MEDIA, dirs_exist_ok=True)
print(f"Copied {sum(1 for path in PUBLIC_MEDIA.rglob('*') if path.is_file())} media files to {PUBLIC_MEDIA}")
