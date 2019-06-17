def dialogue(text):
    quotestart = []
    quoteend = []
    for i in range(len(text)):
        if text[i][0] == '"':
            quotestart.append(i)
        if text[i][-1] == '"':
            quoteend.append(i)
            print text[i]
        else:
            None
    return quotestart, quoteend
	
def main():
    book = raw_input("What book? (txt file)\n")
    with open(book, 'r') as f:
        text = f.read().split()
	
    wordcount = len(text)
    quotes = dialogue(text)
    print quotes
    print wordcount
main()