def word_frequency(sentence,find):
    words = sentence.split()
    frequency=0
    for i in words:
        if i==find:
            frequency +=1
        else:
            frequency = 1
    return frequency

sentence = input("Enter a sentence" )
find=input("Enter word to be searched")
print(word_frequency(sentence,find))