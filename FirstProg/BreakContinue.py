name = 'Rams'
word = input("enter name")
for i in range(3):
    j=2
    if(word==name):
        print("you are correct",word)
        continue
    else:
        print("you missed it, and chances left are ",j-1)
        j = j - i
        break