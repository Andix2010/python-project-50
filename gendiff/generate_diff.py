from gendiff.formatters import stylish_format_output
from gendiff.parsers import read_file


def generate_diff(file_path1: str, file_path2: str) -> str:
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)

    
    diff_dict = {
        "added": {},
        "removed": {},
        "unchanged": {},
    }

    all_keys = sorted(set(file1) | set(file2))
    for key in all_keys:
        if key not in file1:
            diff_dict["added"][key] = file2[key]
        elif key not in file2:
            diff_dict["removed"][key] = file1[key]
        elif file1[key] == file2[key]:
            diff_dict["unchanged"][key] = file1[key]
        elif file1[key] != file2[key]:                  ## changed
            diff_dict["added"][key] = file2[key]
            diff_dict["removed"][key] = file1[key]

    return stylish_format_output(all_keys, diff_dict)

