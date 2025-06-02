import sys
import os
from pathlib import Path


def rename_file(source_path: str, destination_path: str):
    source = Path(source_path)
    destination = Path(destination_path)

    if not source.exists():
        print("⚠️ Error: Source path not found.")
        return

    if destination.exists():
        print(
            f"⚠️ Error: A file already exists at the destination path: '{destination}'")
        return

    try:
        os.rename(source_path, destination_path)
        print("✅ File renamed successfully.")
    except OSError as e:
        print(f"❌ Failed to rename file: {e}")


def cli(args):
    if len(args) == 1:  # No arguments provided
        print("⚠️ Error: No arguments provided.")
        return

    if len(args) != 3:  # Require exactly two arguments
        print("⚠️ Error: You must provide exactly 2 arguments: <source_path> <destination_path>")
        return

    source_path, destination_path = args[1], args[2]
    rename_file(source_path, destination_path)


cli(sys.argv)
