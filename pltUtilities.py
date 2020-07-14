def getNumbers(inString, typeFunc=float):
    '''
    transforms "(x,y,z,...)" into
    [typeFunc(x), typeFunc(y), typeFunc(z), ... ]
    e.g. cpp complex is transformed into a python list
    '''
    for cc in ['(', ',', ')']:
        inString = inString.replace(cc, ' ')
    resu = [typeFunc(word) for word in inString.split()]
    return resu


def checkWord(word, expression, exactForm):
    return ((word.find(expression) != -1 and not exactForm) or
            (word == expression and exactForm))


def getParameter(inLines, expression, typeFunc, exactForm=True, position=1):
    for line in inLines:
        words = line.split()
        if words != [] and checkWord(words[0], expression, exactForm):
            return typeFunc(words[position])
    raise Exception("Parameter not found")

    
def getList(inLines, expression, typeFunc=float, exactForm=True, position=1):
    for line in inLines:
        words = line.split()
        if words != [] and checkWord(words[0], expression, exactForm):
            return [typeFunc(word) for word in words[position:]]
    raise Exception("List not found")

        
def getArray(inLines, expression, typeFunc=float, exactForm=True):
    resu = None
    reading_started = False
    i_line = 0
    while i_line < len(inLines):
        words = inLines[i_line].split()
        if words == []:
            pass
        elif checkWord(words[0], expression, exactForm):
            words = inLines[i_line+1].split()
            if words != [] and checkWord(words[0], '{', True):
                reading_started = True
                resu = []
                i_line += 1
            else:
                break
        elif reading_started and checkWord(words[0], '}', True):
            break
        elif reading_started:
            resu.append(typeFunc(words[0]))
        i_line += 1
    if resu is None:
        raise Exception("Array not found")
    return resu
