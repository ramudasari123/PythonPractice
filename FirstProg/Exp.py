class demo:
    
    def testmethod1(self):
        from _collections_abc import range_iterator
        r=2
        for letter in 'ram':
            r=r-1
            print("letter is",letter)
    def testmethod2(self, num):
        print("param is ",num)
        if num == 2:
            print("hiiiiiiiii value is ",num)
        else:
            print("byyeee is ",num-1)
        ram = ['kajal','sriya', 'prabhas']
        for hr in ram:
            print("hr is ",hr)
        
        for i in range(0,10,1):
            print ("i value is ",i)
def welcome(title):
    """Welcome the player and get his/her name."""
    print ("\t\t", title, "\n")
   
welcome("ram")        
ob = demo()
#print(ob.testmethod1())
#print(ob.testmethod2())
#print(ob.testmethod2())
ob.testmethod2(5)