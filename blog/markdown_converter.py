def append_strings_in_list(list):
    result = ''
    for string in list:
        result += str(string)
    return result


def taggify_start(content):
    text = f'<{content[0]}'
    if content[1] != '':
        text += f' class="{content[1]}"'
    text += '>'
    return text


def taggify_end(text):
    return '</' + text + '>'


def markdown_converter(text):
    signals = {
        'code_signal': {
            '`': {
                'pre': 'container',
                'code': 'language-python code'
            }
        },
        'subsubtitle_signal': {
            ';;;': {
                'h5': ''
            }
        },
        'subtitle_signal': {
            ';;': {
                'h4': ''
            }
        },
        'title_signal': {
            ';': {
                'h3': ''
            }
        },
        'bold_signal': {
            '--': {
                'b': ''
            }
        },
    }

    for key, value in signals.items():
        for key1, value1 in value.items():
            var = True
            while (var):
                holder = text
                text = text.replace(key1, append_strings_in_list([taggify_start(j) for j in value1.items()]), 1)
                text = text.replace(key1, append_strings_in_list(reversed([taggify_end(j[0]) for j in value1.items()])), 1)
                if (holder == text):
                    var = False
    return text