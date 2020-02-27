def read_text():
    quotes = open("profinity.txt","r")
    contents_of_file = quotes.read()
    for line in contents_of_file:
        fields = line.split(";")
    print(fields)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    Word_db = ["hot","S***","A**"]
    quotes = open("profinity.txt")
    contents_of_file = quotes.read()
    output == Word_db
    if str(Word_db) in quotes.read():
        output == 1
    if output == 1:
        print("Profanity Alert!!")
    elif output == 0:
        print("This document has no curse words.")
    else:
        print("ERROR: Could not scan the document properly.")
read_text()