def popular_words (text: str, words: list):
    """
    Count the occurrences of each word in the text and return a dictionary
    :param text: the text to be counted
    :param words: the list of words
    :return: a dictionary
    """

    text = text.lower()
    text_list = text.split()
    result_dict = {}
    for word in words:
        a = text_list.count(word)
        result_dict[word] = a
    return result_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
