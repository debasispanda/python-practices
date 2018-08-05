class Fruit:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)


f1 = Fruit('mango')
f1.print_name()

print(isinstance(f1, Fruit)) # True
print(f1.__class__) # Fruit

f1.val = 1
Fruit.val = 10
print(f1.val, Fruit.val) # 1 10