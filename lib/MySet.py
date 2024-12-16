class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}

        for value in enumerable:
            self.dictionary[value] = True

    def __str__(self):
        setTxt = "{"
        for i, key in enumerate(self.dictionary, start=1):
            if i == len(self.dictionary):
                setTxt += str(key) + "}"
            else:
                setTxt += str(key) + ","

        return(f"MySet: {setTxt}")

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        del self.dictionary[value]
        return self

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self


    


  

