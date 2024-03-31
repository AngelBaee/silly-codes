class numbs():
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
cclass = numbs()
iiter = iter(cclass)

print(next(iiter))
print(next(iiter))
print(next(iiter))
print(next(iiter))
print(next(iiter))
