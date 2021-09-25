import re


# Recebe uma lista de strings e retorna-as concatenadas
def append_strings_in_list(lista):
    result = ''
    for string in lista:
        result += str(string)
    return result


# Gera o inicio de uma tag, i.e. <b>
def taggify_start(content):
    text = f'<{content[0]}'
    if content[1] != '':
        text += f' class="{content[1]}"'
    text += '>'
    return text


# Gera o final de uma tag, i.e. </b>
def taggify_end(text):
    return '</' + text + '>'


# Converte uma lista 1D em uma lista de tuplas com dois elementos, i.e. [1, 2, 3, 4] -> [(1, 2), (3, 4)]
def list_1d_to_2d(lista, column_size=2):
    var = []
    temp = []
    column_count = 0
    lista.append(None)

    for item in lista:
        if column_count >= column_size:
            column_count = 0
            var.append(tuple(temp))
            temp.clear()

        temp.append(item)
        column_count += 1

    lista.remove(None)

    return var


# Encontra em text as ocorrencias das tags de 'code_signal'
def update_locations(location, tag_start, tag_end, text):
    location.update(tuple([m.start() for m in re.finditer(tag_start, text)]))
    location.update(tuple([m.start() for m in re.finditer(tag_end, text)]))
    return location


# Verifica se, dado uma lista list_1d_to_2d, pos esta entre dois elementos quaisqueres das tuplas
def verify_if_pos_is_inside_cod(pos, locations):
    for item in locations:
        if item[0] < pos < item[1]:
            return False
    return True


def markdown_converter(text, signals=None):

    if signals is None:
        signals = {
            'code_signal': {
                '`': {
                    'pre': 'container',
                    'code': 'language-python code'
                }
            },
            'subsubtitle_signal': {
                '###': {
                    'h5': 'gray-text'
                }
            },
            'subtitle_signal': {
                '##': {
                    'h4': 'gray-text'
                }
            },
            'title_signal': {
                '#': {
                    'h3': 'gray-text'
                }
            },
            'bold_signal': {
                '--': {
                    'b': ''
                }
            },
            'list_signal': {
                '**': {
                    'li': ''
                }
            }
        }

    tag_code_start = ''
    tag_code_end = ''

    # Troca todas as ocorrencias de signals['code_signal'] pelo suas tags equivalentes
    for value in signals['code_signal'].values():
        tag_code_start = append_strings_in_list([taggify_start(j) for j in value.items()])
        tag_code_end = append_strings_in_list(reversed([taggify_end(j[0]) for j in value.items()]))

        code_signal = [item for item in signals['code_signal'].keys()][0]

        while True:
            verify = text
            text = text.replace(code_signal, append_strings_in_list([taggify_start(j) for j in value.items()]), 1)
            text = text.replace(code_signal,
                                append_strings_in_list(reversed([taggify_end(j[0]) for j in value.items()])), 1)

            if verify == text:
                break

    signals.pop('code_signal')

    # Para cada simbolo markdown exceto 'code_signal', troca-o por suas tags com classes se esses simbolos nao
    # estiverem dentro de tags 'code_signal'
    for key, value in signals.items():
        for key1, value1 in value.items():
            temp = 0
            locations = set([])
            var = True

            while var:
                locations = update_locations(locations, tag_code_start, tag_code_end, text)
                locations = set(list_1d_to_2d(sorted(locations)))
                temp = text.find(key1, temp + 1)

                for _ in locations:
                    if temp == -1:
                        var = False
                        break
                    elif verify_if_pos_is_inside_cod(temp, locations):
                        text = text[:temp] + text[temp:].replace(key1, append_strings_in_list(
                            [taggify_start(j) for j in value1.items()]), 1)
                        text = text[:temp] + text[temp:].replace(key1, append_strings_in_list(
                            reversed([taggify_end(j[0]) for j in value1.items()])), 1)
                        break
                    else:
                        break
                locations.clear()
    return text
