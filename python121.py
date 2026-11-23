# Shutil module in python
from pathlib import Path
import shutil

base_dir = Path("shutil_sandbox")
source_dir = base_dir / "raw_notes"
backup_dir = base_dir / "backup_notes"
archive_dir = base_dir / "organized_archive"

source_dir.mkdir(parents=True, exist_ok=True)
backup_dir.mkdir(parents=True, exist_ok=True)
archive_dir.mkdir(parents=True, exist_ok=True)


sample_file = source_dir / "walrus_notes.txt"
sample_file.write_text("practice notes for shutil module.\n", encoding="utf-8")


copied_file = shutil.copy2(sample_file, backup_dir/ "walrus_notes_backup.txt")
print("copied to:",copied_file)


zip_Path = shutil.make_archive(
    base_names=str(base_dir/ "notes_bundle"),
    format="zip",
    root_dir=backup_dir,
)
print("Zip created at:", zip_Path)

moved_file = shutil.move(str(sample_file), str(archive_dir / "walrus_notes.txt"))
print("Moved to:", moved_file)

