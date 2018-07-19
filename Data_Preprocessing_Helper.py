import string
import re

urlPattern = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})"

def removePunctuations(text):
    '''

    :param text:
    :return:
    '''
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def removeNonAscii(s):
    '''

    :param s:
    :return:
    '''
    return "".join(i for i in s if ord(i)<128)

def isUrlThen1(urls):
    '''

    :param urls:
    :return:
    '''
    if not re.match(r"^[a-zA-Z0-9]", urls):
        return 0
    else:
        return 1

def removeEmoj(text):
    '''

    :param text:
    :return:
    '''
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002700-\U000027BF"
        u"\U00002A00-\U00002AFF"
        u"\U00002600-\U000026FF"
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r' ', text) # no emoji    
    return text

# a = "adfafa"
# b = []
# print(isUrlThen1(a))
