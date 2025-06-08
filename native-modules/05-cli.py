import sys
import os
from pathlib import Path


def rename_file(source_path: str, destination_path: str):
    result = validate_paths(source_path, destination_path)
    if result is None:
        return

    source, destination = result
    try:
        os.rename(source, destination)
        print(
            f"✅ File renamed successfully: {source.name} → {destination.name}")
    except OSError as e:
        print(f"❌ Failed to rename file: {e}")


def validate_paths(source_path: str, destination_path: str):
    base_dir = Path("./native-modules")
    source = base_dir / source_path
    destination = base_dir / destination_path

    if not source.exists():
        print("⚠️ Error: Source path not found.")
        return None

    if not source.is_file():
        print("⚠️ Error: The source path is not a file.")
        return None

    if destination.exists():
        print(
            f"⚠️ Error: A file already exists at destination path: {destination}")
        return None

    return source, destination


def cli(argv):
    if len(argv) != 3:
        print("⚠️ Usage: python script.py <source_path> <destination_path>")
        return

    source_path, destination_path = argv[1], argv[2]
    rename_file(source_path, destination_path)


cli(sys.argv)
