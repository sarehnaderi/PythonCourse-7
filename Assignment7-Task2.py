def counter():
    print("Enter your text to recieve the count of words.")
    sentence = input("Enter your text:")
    count = len(sentence.split(" "))
    print("Your words count: ",count)
counter()