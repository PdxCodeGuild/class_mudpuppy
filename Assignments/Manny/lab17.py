#w1 = input("enter a word: ")
#w2 = input("enter a word: ")

def check_palindrone(st1):
    is_palindrone = True
    for index in range(len(st1)):
        r_index = len(st1) - index - 1
        print(index, r_index)
        print(st1[index], st1[r_index])
        if st1[index] != st1[r_index]:
            is_palindrone = False
    return is_palindrone                
def check_angram(st1, st2):
    
   
    an1 = list(st1.lower())
    an2 = list(st2.lower())
    an1.sort() 
    an2.sort()
    if an1 == an2:
        return f"{st1} and {st2} are anagrams"
    else: 
        return f"{st1} and {st2} are not anagrams"
#print(check_angram(w1, w2))       
print(check_palindrone("racecar"))
print(check_palindrone("abc"))
