def stylish(diff_dict: dict, nested: int = 0) -> str:
    indent = nested * '    '
    result = []
    for key, info in diff_dict.items():
        if info['type'] == 'unchanged':
            value = format_line(indent, ' ', key, info['value'], nested + 1)
            result.append(value)

        elif info['type'] == 'changed':
            old_value = format_line(indent, '-', key, info['old'], nested + 1)
            result.append(old_value)
            new_value = format_line(indent, '+', key, info['new'], nested + 1)
            result.append(new_value)

        elif info['type'] == 'removed':
            value = format_line(indent, '-', key, info['value'], nested + 1)
            result.append(value)

        elif info['type'] == 'added':
            value = format_line(indent, '+', key, info['value'], nested + 1)
            result.append(value)

        elif info['type'] == 'nested':
            result.append(f"{indent}    {key}: {{")
            result.append(stylish(info['children'], nested + 1))
            result.append(f"{'    ' + indent}}}")

    body = "\n".join(result)
    if nested:
        return body
    return "{\n" + body + "\n}"


def to_str(value) -> str:              # for bool True -> true and None -> null
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def render_value(value, nested):
    indent = nested * '    '
    if isinstance(value, dict):
        line = []
        for k, v in value.items():
            line.append(f"{indent}    {k}: {render_value(v, nested + 1)}")
        return "{\n" + "\n".join(line) + "\n" + indent + "}"
    return to_str(value)

        
def format_line(indent, prefix, key, value, nested):
    rendered = render_value(value, nested)
    if rendered:
        return f"{indent}  {prefix} {key}: {rendered}"
    return f"{indent}  {prefix} {key}:"