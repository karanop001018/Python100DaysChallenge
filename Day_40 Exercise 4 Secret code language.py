# Write a python program to translate into secret code language.
# Use the rules below to translate normal English into secret code language.

# Coding:
#     if the word contains atleast 3 characters, remove the first letter and append it at the end 
#     now append three random characters at the starting and the end
#     else:
#         simply reverse the string

# Decoding:
#     if  the word contains less than 3 characters, reverse it
#     else:
#         removw 3 random characters from start and end.
#         Now remove the last letter and apppend the last letter and append it to the beginning






st = input('Enter the message')
words = st.split("   ")
# coding = True # For coding: True and to decode: False
coding = input('1 for coding or 0 for Decoding')
coding = True if (coding == "1") else False
if (coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = 'art'
            r2 = 'cod'
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            r1 = 'art'
            r2 = 'cod'
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("".join(nwords))