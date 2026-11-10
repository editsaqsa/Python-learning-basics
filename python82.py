# Excercise code
st = input("Enter message:")
words = st.split(" ")
coding = input("I for coding or O for Decoding:")
coding = True if (coding == "1") else False
if coding:
    nwords = []
    for word in words:
        if len(word)>3:
            r1 = "dsf"
            r2 = "jkl"
            stnew = r1 + word[1:]+word[0]+r2
            nwords.append(stnew)
else:
    nwords = []
    for word in words:
        if len(word)>3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
print(" ".join(nwords))