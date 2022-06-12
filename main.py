from turtle import clear


def read_file_content(filename):
    #filename = "story.txt"
    print()
    with open(filename, 'r') as filehandle:
        filecontent = filehandle.read()
    return filename

def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    d = dict()
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    return d
print(count_words())