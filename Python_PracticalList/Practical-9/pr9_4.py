f1 = open("demo.txt","r+")
word = f1.read()  

f1.seek(0)
word1 = f1.read(7)  

f1.seek(0)
word2 = f1.readline()   

f1.seek(0)
word3 = f1.readlines() 
print("word 1 : ",word)
print("word 2 : ",word1)
print("word 3 : ",word2)
print("word 4 : ",word3)
print("word 5 : ",word3[1])
f1.close()
