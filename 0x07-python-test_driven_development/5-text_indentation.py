#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """


    if not isinstance(text, str):
        raise TypeError('text must be a string')
    punc = text.replace('.', '.\n\n')
    punc = punc.replace('?', '?\n\n')
    punc = punc.replace(':', ':\n\n')
    newLine = punc.split('\n')
    for line in range(len(newLine)):
        print("{}".format(newLine[line].strip()),
              end=("" if (line == (len(newLine) - 1)) else '\n'))
