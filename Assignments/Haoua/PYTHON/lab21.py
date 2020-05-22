import string
# letter=ascii_letters
punc=string.punctuation
# path="C:/Users/hdogo/Desktop/pdxcodeguild/PYTHON/text.txt"
f = open("PYTHON/text.txt","r",  encoding="utf-8")


stripp=f.read().strip("\n")
stripper=stripp.strip(punc)

stripper2=stripper.split()
# s3=stripper2.strip(punc)
# print(stripper2)
print(stripper2[i])
# for be in stripper2:
#     for i in punc:
#         # print(i)
#         he=be.strip(i)
#         print(he)
#         for  in i:
#             b
#         # if i in punc:
        #     s4=be.strip(i)
            # print(i)
            # q=be.repi,"")
            # print(s4)

        # s4=striper2.remove(i)
        # print(s4)
        # for b in s4:
        #     if b in punc:
        #         s5=s4.strip(b)
        #         print(s5)