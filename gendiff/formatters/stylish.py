def stylish_format_output(sorted_keys: set, diff_dict: dict) -> str:
    result = []
    for key in sorted_keys:
        if key in diff_dict['unchanged']:
            result.append(f"    {key}: {to_str(diff_dict['unchanged'][key])}")
        elif key in diff_dict['added'] and key in diff_dict['removed']:   ## changed
            result.append(f"  - {key}: {to_str(diff_dict['removed'][key])}")
            result.append(f"  + {key}: {to_str(diff_dict['added'][key])}")
        elif key in diff_dict['removed']:
            result.append(f"  - {key}: {to_str(diff_dict['removed'][key])}")
        else:
            result.append(f"  + {key}: {to_str(diff_dict['added'][key])}")

    return "{\n" + "\n".join(result) + "\n}"


def to_str(value) -> str:              ## for bool True -> true
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)