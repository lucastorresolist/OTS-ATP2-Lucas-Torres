from category import Category
from product import Product


def insert_category():
    category = Category()
    category.set_name(input('\nFavor inserir o nome da categoria: '))
                    
    selected_insert_subcategory = 1
    subcategories: list = []
    while selected_insert_subcategory != 0:
        selected_insert_subcategory = int(input('\nDeseja inserir uma subcategoria? (SIM = 1/ NÃO = 0): '))
        if selected_insert_subcategory == 1:
            subcategories.append(input('Favor inserir o nome da subcategoria: '))
                    
    category.set_subcategory(subcategories)

    categorys.append(category)


def remove_category():
    if(len(categorys) == 0):
        print('\nNão há categorias cadastradas!')
    else:
        print('\nCategorias:')
        count = 0
        for obj in categorys:
            print('ID - ' + str(count) + ' ' + obj.__repr__())
            count += 1
                        
        category_selected = int(input("\nFavor inserir o número do id da categoria: "))
        categorys.remove(categorys[category_selected])

def insert_product():
    if len(categorys) == 0:
        print("\nNão é possível cadastrar um produto sem cadastrar uma categoria antes!")
    else:

        product = Product()

        product.set_name(input('\nFavor inserir o nome do produto: '))

        description = ''
        while len(description) < 20:
            description = input('\nFavor inserir a descrição do produto: ')
            if len(description) < 20:
                print('\nFavor inserir uma drescrição com no mínimo 20 caracteres')
            else:
                product.set_description(description)
                        
                product.set_price(input('\nFavor inserir um preço para o produto: '))
                product.set_height(input('\nInsira a altura do produto: '))
                product.set_width(input('Insira a largura do produto: '))
                product.set_length(input('Insira o comprimento do produto: '))

                option = 1
                cat: list = []
                while option != 0:

                    print('\nSelecione uma categoria')
                    print('\nCategorias:')
                    count = 0
                    for obj in categorys:
                        print('ID - ' + str(count) + ' ' + obj.__repr__())
                        count += 1
                            
                        category_selected = int(input("\nFavor inserir o número do id da categoria: "))
                        cat.append(categorys[category_selected])
                        option = int(input('Deseja selecionar mais uma categoria? (SIM = 1 / NÃO = 0)'))

                product.set_category(cat)
                products.append(product)

def remove_category():
    if(len(products) == 0):
        print('\nNão há produtos cadastrados!')
    else:
        print('\------------Produtos:------------')
        count = 0
        for obj in products:
            print('ID - ' + str(count) + ' ' + obj.__repr__())
            count += 1
                        
        product_selected = int(input("\nFavor inserir o número do id do produto: "))
        products.remove(products[product_selected])


if __name__ == "__main__":

    products = []

    categorys = []
    # category = Category()

    menu: int = 1
    while(menu != 0):

        print('\n------------Menu------------\n')
        print('1 - Categories')
        print('2 - Products')
        print('0 - exit program')

        menu = int(input("Selecione uma das opções: "))

        if menu == 1:
            option_selected = 1
            while option_selected != 0:
                print('\n------------Categories------------\n')
                print('1 - Cadastrar categoria')
                print('2 - Atualizar categoria')
                print('3 - Deletar categoria')
                print('4 - Listar categorias')
                print('0 - Voltar ao menu anterior')

                option_selected = int(input('Selecione uma das opções: '))

                if option_selected == 1:
                    insert_category()
                
                elif option_selected == 2:
                    remove_category()
                    insert_category()
                
                elif option_selected == 3:
                    remove_category()

                elif option_selected == 4:
                    if len(categorys) == 0:
                        print('\nNão há categorias cadastradas!')
                    else:
                        print('\nCategorias:')
                        for obj in categorys:
                            print(obj)
        
        if menu == 2:
            option_selected = 1
            while option_selected != 0:
                print('\n------------Products------------\n')
                print('1 - Cadastrar produto')
                print('2 - Atualizar produto')
                print('3 - Deletar produto')
                print('4 - Listar produto')
                print('0 - Voltar ao menu anterior')

                option_selected = int(input('Selecione uma das opções: '))

                if option_selected == 1:
                    insert_product()
                
                elif option_selected == 2:
                    remove_category()
                    insert_product()
                
                elif option_selected == 3:
                    remove_category()

                elif option_selected == 4:
                    if len(products) == 0:
                        print('\nNão há produtos cadastrados!')
                    else:
                        print('\------------Produtos:------------')
                        for obj in products:
                            print(obj)
                            print('\n')
