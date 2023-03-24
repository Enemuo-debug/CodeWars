def pig_it(text):
    Returned = []
    WordList = text.split(' ')
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in WordList:
        if i.isalpha():
            Returned.append(i[1:] + i[0] + 'ay')
        else:
            Returned.append(i)
    return ' '.join(str(x) for x in Returned)
