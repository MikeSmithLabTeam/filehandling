import tkinter
from tkinter import filedialog
import os
import glob


def open_filename(initialdir='/'):
    root = tkinter.Tk()
    filename = filedialog.askopenfilename(
        initialdir=initialdir,
        title="Select File",
        filetypes=(("all files","*.*"),)
    )
    return filename


def save_filename(title=""):
    root = tkinter.Tk()
    filename = filedialog.asksaveasfilename(
        title=title,
    )
    return filename


def open_directory(initialdir='/'):
    root = tkinter.Tk()
    filename = filedialog.askdirectory(
        initialdir=initialdir,
        title="Select directory"
    )
    return filename


def create_directory():
    filepath = save_filename()
    filepath = remove_ext(filepath)
    os.mkdir(filepath)


def remove_ext(filepath):
    return os.path.splitext(filepath)[0]


def remove_file(filepath):
    return os.path.split(filepath)[0]


def get_ext(filepath):
    return os.path.splitext(filepath)[1]


def remove_path(filepath):
    return os.path.split(filepath)[1]


def get_directory_filenames(directory=None, reverse_sort=False, relative=False,
                            extension=None):
    if directory is None:
        directory = open_directory()
    if extension is not None:
        directory += '*'+extension
    files = glob.glob(directory)
    files.sort(reverse=reverse_sort)

    if relative:
        return [remove_path(f) for f in files]
    else:
        return files


class BatchProcess:
    def __init__(self, directory=None, extension=None, reverse_sort=False):
        self.files = get_directory_filenames(
            directory=directory,
            reverse_sort=False,
            relative=False,
            extension=False)
        self.num_files = len(self.files)
        self.current = 0

    def __iter__(self):
        return self

    def __next(self):
        try:
            file = self.files[self.current]
            self.current += 1
        except IndexError:
            raise StopIteration
        return file
