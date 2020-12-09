class Category:
    name: str
    subcategory: list

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_subcategory(self):
        return self.subcategory

    def set_subcategory(self, subcategory):
        self.subcategory = subcategory

    def __str__(self) -> str:
        return f'Name: {self.name} Subcategories: {self.subcategory}'

    def __repr__(self):
        return str(self.__dict__)