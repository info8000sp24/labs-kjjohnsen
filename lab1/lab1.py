# Kyle Johnsen
# Lab 1
f = open('data.txt')
content = f.read()
num_lines = len(content.split('\n'))
num_words = len(content.split()) # splits on any whitespace
num_characters = len(content.replace('\n',''))
print(num_lines, "lines,", num_words, "words, and", num_characters, "characters")
f.close()


