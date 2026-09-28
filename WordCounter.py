import string


class WordCounter:
    # creates instance varibles 
    def __init__(self):
        self.fileName = ""
        self.words = []
        self.mostCommonWordCount = 0
        self.mostCommonWord = ""

    # takes word friom valiud file strips lowers and removes to punctuation before adding
    def wordsList(self):
        with open(self.fileName, encoding = "utf-8") as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(string.punctuation)
                    if word:
                        self.words.append(word)

    # counts most common word and word count and assigns it to instance var
    def wordCounter(self):
        self.wordsList()
        uniqueWords = {}
        for word in self.words:
            if word in uniqueWords:
                uniqueWords[word] += 1
            else:
                uniqueWords[word] = 1
        for word in uniqueWords:
            if uniqueWords[word] > self.mostCommonWordCount:
                self.mostCommonWordCount = uniqueWords[word]
                self.mostCommonWord = word

    # ensures user input valid file 
    def setFileName(self):
        fileOpened = False
        while not fileOpened:
            tempFileName = input("Enter the name of your file: ").strip()
            try:
                with open(tempFileName, encoding = "utf-8"):
                    fileOpened = True
                    self.fileName = tempFileName
            except OSError as error:
                print("Invalid File Name!", error)
        print("File Found!")

# runs program 
def main():
    wordCounter = WordCounter()
    wordCounter.setFileName()
    wordCounter.wordCounter()
    print("File Name:", wordCounter.fileName)
    print("Most Common Word Count:", wordCounter.mostCommonWordCount)
    print("Most Common Word:", wordCounter.mostCommonWord)


if __name__ == "__main__":
    main()
