    #in python when defining properties or structures of an object we use the __init__() method
    #As a rule in python the first attribute of a class is self
class Phone:    
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

Apple = Phone("iPhone", "iPhone X", 3000, "Silver-Gold")
Samsung = Phone("Samsung", "Galaxy s20", 2500, "Black")
Nokia = Phone("Nokia", "Nokia z10", 2000, "Red")
Apple.price = 900
print(Apple.brand)
print(Apple.price)

for i in Apple:
    print(i)