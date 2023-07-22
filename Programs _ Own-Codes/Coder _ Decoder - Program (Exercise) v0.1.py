st = input("What is the sentence?: ")
words = st.split(" ")
operation = input("Write 0 for coding 1 for decoding: ")
operation = True if operation == "0" else False
if operation:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "has"
            r2 = "jsh"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[:-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            # print(stnew)
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[:-1])
    print(" ".join(nwords))