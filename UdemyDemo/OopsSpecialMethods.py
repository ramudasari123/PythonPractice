class drunds():
    def __init__(self,name, author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    def __str__(self):
        return "author is "+self.author
    def __len__(self):
        return self.pages
drunds=drunds('The Voice of Silence','Ram','101')
print(str(drunds))
print(drunds.__len__())