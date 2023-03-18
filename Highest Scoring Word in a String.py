def high(xx):
    # Code here
    letters = 'abcdefghijklmnopqrstuvwxyz'
#     LettersList = letters.split('')
    x = xx.lower()
    list = x.split(' ')
    scores = []
    for i in list:
        score = 0
        for j in i:
            score += (letters.index(j) + 1)
        scores.append(score)
    maxNum = max(scores)
    return list[scores.index(maxNum)]
