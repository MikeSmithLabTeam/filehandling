import tkinter
from tkinter import filedialog
import os
import glob
import time


def get_filename(
        initialdir='/',
        title="Select File",
        filetypes=(("all files", "*.*"),),
        parent=None):
    """
    Opens a filedialog to return a filename to open

    Parameters
    ----------
    initialdir : str
        The initial directory

    title : str
        Message box title

    filetypes : tuple
        Sequence of (label, pattern) tuples. The same label may occur
        with several patterns. Use "*" as the pattern to indicate all files.

    parent : widget
        If using with tkinter gui provide the parent so focus is returned.

    Returns
    -------
    filename : str
        The selected filename
    """
    if parent is None:
        root = tkinter.Tk()
    filename = filedialog.askopenfilename(
        initialdir=initialdir,
        title=title,
        filetypes=filetypes,
        parent=parent
    )
    if parent is None:
        root.quit()
        root.destroy()
    return filename


open_filename = get_filename

def get_name(filepath):
    """Returns the filename of a path without the directory

    /foo/bar/name.txt  -> name.txt
    """
    return os.path.split(filepath)


def create_filename(
        initialdir='/',
        title="Save File",
        filetypes=(("all files", "*.*"),),
        append_time=False,
        parent=None):
    """
    Opens a filedialog to save a file.

    Parameters
    ----------
    initialdir : str
        The initial directory

    title : str
        Message box title

    filetypes : tuple
        Sequence of (label, pattern) tuples. The same label may occur
        with several patterns. Use "*" as the pattern to indicate all files.

    parent : widget
        If using with tkinter gui provide the parent so focus is returned.

    Returns
    -------
    filename : str
        The selected filename
    """
    if parent is None:
        root = tkinter.Tk()
    filename = filedialog.asksaveasfilename(
        title=title,
        initialdir=initialdir,
        filetypes=filetypes,
        parent=parent
    )
    if append_time==True:
        filename=filename + datetime_stamp()

    if parent is None:
        root.quit()
        root.destroy()
    return filename

save_filename = create_filename

def get_directory(
        initialdir='/',
        title="Select a directory",
        parent=None):
    """
    Opens a filedialog to select a directory

    Parameters
    ----------
    initialdir : str
        The initial directory

    title : str
        Message box title

    parent : widget
        If using with tkinter gui provide the parent so focus is returned.

    Returns
    -------
    filename : str
        The selected directory
    """
    if parent is None:
        root = tkinter.Tk()
    filename = filedialog.askdirectory(
        initialdir=initialdir,
        title="Select directory",
        parent=parent
    )
    if parent is None:
        root.quit()
        root.destroy()
    return filename

open_directory = get_directory


def create_directory(
        initialdir='/',
        title="Create directory",
        parent=None
):
    """
    Opens a filedialog to create a directory

    Parameters
    ----------
    initialdir : str
        The initial directory

    title : str
        Message box title

    parent : widget
        If using with tkinter gui provide the parent so focus is returned.

    Returns
    -------
    filename : str
        The path of the created directory
    """
    if parent is None:
        root = tkinter.Tk()
    filepath = save_filename(
        initialdir=initialdir,
        title=title,
        filetypes=(("No extension", "*"),),
        parent=parent)
    filepath = remove_ext(filepath)
    os.mkdir(filepath)
    if parent is None:
        root.quit()
        root.destroy()
    return filepath


def remove_ext(filepath):
    """Returns the file without extension from a filepath"""
    return os.path.splitext(filepath)[0]


def remove_file(filepath):
    """Returns the top directory from a filepath"""
    return os.path.split(filepath)[0]


def get_ext(filepath):
    """Returns the extension from a filepath"""
    return os.path.splitext(filepath)[1]


def remove_path(filepath):
    """Returns the name of the file from a filepath"""
    return os.path.split(filepath)[1]


def smart_number_sort(filenames):
        filename_sort=[]

        #Secondary sort criterion is the numerical value
        for filename in filenames:
            filename_sort.append(''.join([i for i in filename if i in ['0','1','2','3','4','5','6','7','8','9']]))
        
        #Sort by length of number first. This means 01 goes before 001.
        len_filenames = [len(number) for number in filename_sort]

        sorted_filenames = [x for _,_,x in sorted(zip(len_filenames, filename_sort,filenames))] 
               
        return sorted_filenames


def list_files(directory, reverse_sort=False, smart_sort=None, relative=False,
                            extension=None):
    """
    Returns all the files from a directory.

    Can set the filetype using extension.

    Parameters
    ----------
    directory : str
        Filepath pointing to the directory with the final /
        Can use this with glob wildcards to use more complicated patterns.

    reverse_sort : bool
        If true files returns in reverse alphabetical order

    relative : bool
        If True files will be returned without the directory

    smart_sort : function_handle or None

    extension : str
        Extension filetype to be used as filter.

    Returns
    -------
    files : list
        List of all the files that match the pattern.

    """
    if extension is not None:
        directory += '*'+extension
    files = glob.glob(directory)

    if smart_sort is None:
        files.sort(reverse=reverse_sort)
    else:
        files = smart_sort(files)
    
    if relative:
        return [remove_path(f) for f in files]
    else:
        return files

get_directory_filenames = list_files


def get_filenames():
    root = tkinter.Tk()
    files = filedialog.askopenfilenames(parent=root, title='Choose files')
    return files


class BatchProcess:
    """
    BatchProcess is a generator that enables you to easily iterate through a selection
    of files in a directoy.

    Attributes
    ----------
    num_files : int     The number of files in the selection
    current : int       The index of the file currently pointed at
    files : list        A list of strings of the filenames to be iterated over

    Returns
    -------
    file : str          A filename

    Examples
    --------
    directory is a path to a folder or expression for pattern matching.
    eg. /Documents/Example/a*b?.txt
    This returns files beginning in a with a b as the penultimate letter and file extension .txt

    for filename in BatchProcess(directory):
        print(filename)

    """

    def __init__(self, directory, extension=None, relative=False, smart_sort=None, reverse_sort=False):
        self.files = get_directory_filenames(
            directory,
            reverse_sort=reverse_sort,
            relative=relative,
            smart_sort=smart_sort,
            extension=extension)
        self.num_files = len(self.files)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            file = self.files[self.current]
            self.current += 1
        except IndexError:
            raise StopIteration
        return file

def datetime_stamp(format_string = "%Y%m%d_%H%M%S"):
    """
    Get string for current date and time
    """
    now=time.gmtime()
    return time.strftime(format_string)
