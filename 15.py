sentence = input("Enter a sentence: ")

def reverser(words):
    return " ".join(words.split(" ")[::-1])

print(reverser(sentence))