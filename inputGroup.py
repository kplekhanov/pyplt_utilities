class InputGroup():
    def __init__(self, name):
        self.__name__ = name

    def __write__(self, f):
        '''
        write the InputGroup to the file 'f' in the format
        __name__
        {
        attributeName = attributeValue
        ...
        }
        '''
        f.write(self.__name__ + "\n{\n")
        for a in dir(self):
            if not a.startswith('__'):
                str_to_write = a + " = " + str(getattr(self, a)) + "\n"
                f.write(str_to_write)
        f.write("}")
