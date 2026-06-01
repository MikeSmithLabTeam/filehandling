# filehandling
Repository for basic file handling tasks

## documentation
https://filehandling.readthedocs.io/en/latest/

## github installation
To install run the following line in your environment

    pip install git+https://github.com/MikeSmithLabTeam/filehandling

This package now uses PyQt6 for file and directory dialogs instead of tkinter.

## github update
To update run the following line in your environment

    pip install --upgrade git+https://github.com/MikeSmithLabTeam/filehandling

## UV packaging
This project is configured as a UV project using `pyproject.toml` and the `uv` build backend.

Install `uv` and build the distribution with:

    python -m pip install uv
    uv build
