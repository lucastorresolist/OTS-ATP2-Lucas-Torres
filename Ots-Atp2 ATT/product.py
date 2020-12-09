from category import Category
class Product:
    name: str
    description: str
    price: float
    width: float
    height: float
    length: float
    category: Category


    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
    
    def get_width(self):
        return self.width
    
    def set_width(self, width):
        self.width = width
    
    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height
    
    def get_length(self):
        return self.length
    
    def set_length(self, length):
        self.length = length

    def get_category(self):
        return self.category
    
    def set_category(self, category):
        self.category = category

    # def __init__(self, name, description, price, width, height, length, category):
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.width = width
    #     self.height = height
    #     self.length = length
    #     self.category = category

    def __str__(self) -> str:
        return f' Name: {self.name}\n Description: {self.description}\n Price: {self.price}\n Width: {self.width}\n Height: {self.height}\n Length: {self.length}\n Category: {self.category.__str__()}'
