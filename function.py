from fileinput import filename


def countWordsFromFile():
    filename=input("enter the filename")
    numberOfWords=0
    file=open(filename,'r') 
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("numberOfWords =",numberOfWords)
countWordsFromFile()