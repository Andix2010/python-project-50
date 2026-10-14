def plain(diff_dict: dict, path='') -> str:
    result = []

    for key, info in diff_dict.items():

        full_key = f"{path}.{key}" if path else key

        if info['type'] == 'unchanged':
            continue

        elif info['type'] == 'changed':
            old_value = format_value(info['old'])
            new_value = format_value(info['new'])
            line = (
                f"Property '{full_key}' was updated."
                f" From {old_value} to {new_value}"
            )
            result.append(line)

        elif info['type'] == 'removed':
            result.append(f"Property '{full_key}' was removed")

        elif info['type'] == 'added':
            value = format_value(info['value'])
            value = f"Property '{full_key}' was added with value: {value}"
            result.append(value)

        elif info['type'] == 'nested':
            result.append(plain(info['children'], full_key))

    return "\n".join(result)
    

def to_str(value) -> str:              # for bool True -> true and None -> null
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return to_str(value)