from unittest import TestCase
import filehandling


class TestOpen(TestCase):
    def test_open_filename(self):
        file = filehandling.open_filename()
        self.assertTrue(type(file) == str)


class TestSave(TestCase):
    def test_save_filename(self):
        file = filehandling.save_filename()
        self.assertTrue(type(file) == str)
        self.assertTrue(len(file) > 0)


class TestOpenDirectory(TestCase):
    def test_open(self):
        direc = filehandling.open_directory()
        self.assertTrue(type(direc) == str)