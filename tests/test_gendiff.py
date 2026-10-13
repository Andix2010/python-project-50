import sys
from pathlib import Path

from gendiff import generate_diff, parsing


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def test_cli_parsing(monkeypatch):
    file2_path = "test_data/file2.yml"
    monkeypatch.setattr(sys, 'argv', 
            ['gendiff', 'file1.json', file2_path, '-f', 'stylish'])
    args = parsing()
    assert args.first_file == 'file1.json'
    assert args.second_file == "test_data/file2.yml"
    assert args.format == 'stylish'


def test_stylish():
    result = get_test_data_path("stylish_output.txt").read_text()
    nested_result = get_test_data_path("nested_stylish_output").read_text()

    file1_path = get_test_data_path("file1.json")
    file2_path = get_test_data_path("file2.json")
    assert generate_diff(file1_path, file2_path) == nested_result

    file1_path = get_test_data_path("file1.yml")
    file2_path = get_test_data_path("file2.yml")
    assert generate_diff(file1_path, file2_path) == result