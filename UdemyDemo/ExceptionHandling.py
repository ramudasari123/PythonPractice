class Exception():
    def handles(self):
        list1=list()
        val1=int(input("Enter value 1: "))
        list1.append(val1)
        try:
            for i in range(1,4):
                val=int(input("enter value: "))
                list1.append(val)

        except:
            print("Exceeds limit")
        finally:
            print("completed the operation")
        print(list1)
exceptions=Exception()
exceptions.handles()
print(2**3)