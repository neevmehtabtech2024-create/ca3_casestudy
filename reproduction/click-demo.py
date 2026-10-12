"""Minimal Windows reproduction for the Click folder-location investigation."""
import pathlib
import click

ROOT_FOLDER = pathlib.Path(r"C:\Users\Public")

folder_without_spaces = ROOT_FOLDER / "click-demo"
folder_without_spaces.mkdir(exist_ok=True)
print(f"Opening folder without spaces: {folder_without_spaces}")
click.launch(str(folder_without_spaces), locate=True)

folder_with_spaces = ROOT_FOLDER / "click demo"
folder_with_spaces.mkdir(exist_ok=True)
print(f"Opening folder with spaces: {folder_with_spaces}")
click.launch(str(folder_with_spaces), locate=True)
