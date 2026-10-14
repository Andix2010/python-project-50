from gendiff.formatters import plain, stylish
from gendiff.parsers import read_file

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': ''
}


def generate_diff(file_path1, file_path2, format_func='stylish') -> str:
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)

    def search(file1, file2):

        diff_dict = {}

        all_keys = sorted(set(file1) | set(file2))
        for key in all_keys:
            if key not in file1:
                diff_dict[key] = {'type': 'added', 
                                  'value': file2[key]}
                
            elif key not in file2:
                diff_dict[key] = {'type': 'removed',
                                  'value': file1[key]}
                
            elif file1[key] == file2[key]:
                diff_dict[key] = {'type': 'unchanged',
                                  'value': file1[key]}
                
            elif file1[key] != file2[key]:
                if not isinstance(file1[key], dict) or not isinstance(file2[key], dict):  # ruff: ignore[line-too-long]
                    diff_dict[key] = {'type': 'changed',
                                      'old': file1[key],
                                      'new': file2[key],
                                      }
                    
                else:
                    children1 = file1[key]
                    children2 = file2[key]
                    diff_dict[key] = {'type': 'nested',
                                      'children': search(children1, children2)
                                      }

        return diff_dict

    diff_dict = search(file1, file2)
    return FORMATTERS[format_func](diff_dict)

