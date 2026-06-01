import os

import filehandling


def test_get_name():
    assert filehandling.get_name('/foo/bar/name.txt') == ('/foo/bar', 'name.txt')


def test_remove_ext():
    assert filehandling.remove_ext('document.txt') == 'document'
    assert filehandling.remove_ext('archive.tar.gz') == 'archive.tar'


def test_remove_path():
    assert filehandling.remove_path('/foo/bar/name.txt') == 'name.txt'
    assert filehandling.remove_path('name.txt') == 'name.txt'


def test_get_ext():
    assert filehandling.get_ext('document.txt') == '.txt'
    assert filehandling.get_ext('archive') == ''


def test_smart_number_sort():
    filenames = ['file10.txt', 'file2.txt', 'file1.txt', 'file01.txt']
    
    assert filehandling.smart_number_sort(filenames) == ['file1.txt', 'file2.txt', 'file01.txt', 'file10.txt']


def test_list_files_relative(tmp_path):
    (tmp_path / 'a1.txt').write_text('1')
    (tmp_path / 'a10.txt').write_text('10')
    (tmp_path / 'a2.txt').write_text('2')

    results = filehandling.list_files(
        str(tmp_path) + os.sep,
        extension='.txt',
        relative=True,
        smart_sort=filehandling.smart_number_sort,
    )

    assert results == ['a1.txt', 'a2.txt', 'a10.txt']


def test_datetime_stamp_format():
    stamp = filehandling.datetime_stamp(format_string='%Y%m%d')
    assert len(stamp) == 8
    assert stamp.isdigit()
