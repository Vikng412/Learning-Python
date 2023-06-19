def sentence_to_list(sentence):
    words = sentence.split()
    return words


task = input("What do you want to do? (code/decode): ")

if task == "code":
    sentence_to_code = input("Input the sentence to code: ")
    sentence = sentence_to_code
    words = sentence_to_list(sentence)
elif task == "decode":
    sentence_to_decode = input("Input the sentence to decode: ")
    sentence = sentence_to_decode
    words = sentence_to_list(sentence)
else:
    print("Invalid Option chosen!")
    quit()

for i in words:
    if len(i)<3:
        new_word = words[-1:-2]
    print(new_word)