class numbs():
    def __iter__(self):
        self.pp = 11
        return self
    

    def __next__(self):
        ll = self.pp
        self.pp += 1
        return ll
    
ss = numbs()
ff = iter(ss)

print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))