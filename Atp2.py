class Categoria:
    # __id: int
    __nome: str

    # def __init__(self, nome):
    #     self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


class Produto:

    nome: str
    descricao: str
    peso: float
    altura: float
    preco: float
    quantidade: int
    categoria: list

    # def __init__(self, nome, descricao, peso, altura, preco, quantidade, categoria):
    #     self.nome = nome
    #     self.descricao = descricao
    #     self.peso = peso
    #     self.altura = altura
    #     self.preco = preco
    #     self.quantidade = quantidade
    #     self.categoria = categoria

    def __repr__(self):
        return str(self.__dict__)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_peso(self):
        return self.peso
    
    def set_peso(self, peso):
        self.peso = peso

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria


if __name__ == "__main__":

    menu: int = 1

    cat = Categoria()
    prod = Produto()
    categorias = []
    produtos = []

    while(menu != 0):
        print("\n")
        print("------------Opções------------")
        print("1 - Categorias")
        print("2 - Produtos")
        print("0 - Parar execucao")
        menu = int(input("Informe o numero de qual das opcoes deseja: "))

        if(menu == 1):
            input_usuario = 1
            while(input_usuario != 0):
                print("\n")
                print("1 - Inserir categoria")
                print("2 - Deletar categoria")
                print("3 - Atualizar categoria")
                print("4 - Listar categoria")
                print("0 - Voltar ao menu anterior")
                input_usuario = int(
                    input("Informe o numero de qual das opcoes deseja: "))

                if(input_usuario == 1):
                    cat.set_nome(
                        input("Favor inserir o nome da categoria: ").lower())
                    categorias.append(cat.get_nome())

                elif(input_usuario == 2):
                    categorias.remove(
                        input("Fovor inserir o nome da categoria a ser deletada: ").lower())

                elif(input_usuario == 3):

                    categoria_old = input(
                        "Favor inserir o nome da categoria a ser atualizada: ").lower()
                    cat.set_nome(
                        input("Favor inserir o novo nome da categoria: ").lower())
                    categorias.remove(categoria_old)

                elif(input_usuario == 4):
                    if(len(categorias) == 0):
                        print("Nao existem categorias cadastradas")
                    else:
                        print(categorias)
                        # for categoria in categorias:
                        #     print("Nome da categoria: " + categoria)

        elif(menu == 2):

            input_usuario = 1
            while(input_usuario != 0):
                print("\n")
                print("1 - Inserir produto")
                print("2 - Deletar produto")
                print("3 - Atualizar produto")
                print("4 - Listar produtos")
                print("0 - Voltar ao menu anterior")
                input_usuario = int(
                    input("Informe o numero de qual das opcoes deseja: "))

                if(input_usuario == 1):
                    exit = 's'
                    categoria_insert = []
                    while(exit != "n"):
                        count = 0
                        for cat in categorias:
                            print("ID: " + str(count) + " Nome: " + cat)
                            count += 1

                        categoria_selecionada = int(input("Favor informar o id da categoria: "))
                        categoria_insert.append(categorias[categoria_selecionada])
                        
                        exit = input("Deseja adicionar mais uma categoria? S/N: ")

                    prod.set_nome(input("Favor inserir o nome do produto: ").lower())
                    
                    desc_valid = False
                    while(desc_valid != True):
                        descricao = input("Favor inserir a descricao do produto: ")
                        if(len(descricao) >= 20):
                            desc_valid = True
                            prod.set_descricao(descricao)
                        else:
                            print("Favor inserir uma descricao com no minimo 20 caracteres")

                    prod.set_peso(float(input("Insira o peso do produto: ")))

                    prod.set_altura(float(input("Insira a altura do produto")))
                     
                    prod.set_preco(float(input("Insira o preco para o produto: "))) 

                    prod.set_quantidade(int(input("Insira a quantidade do produto: ")))
                    prod.set_categoria(categoria_insert)

                    produtos.append(prod.__repr__())
                    # for obj in produtos:
                    #     print(obj.__repr__())
                    
                elif(input_usuario == 2):
                    if(len(produtos) > 0):
                        count = 0
                        for produto in produtos:
                            print(str(count) + ' - ' + produto)
                            count += 1
                        
                        opcao_escolhida = int(input("Favor informar o indice do produto"))
                        produtos.remove(produtos[opcao_escolhida])
                    else:
                        print("A lista esta vazia")
                elif(input_usuario == 3):

                    nome_produto_old = input(
                        "Qual produto gostaria de alterar? ")

                    for produto in produtos:
                        print(produto.nome)
                        if nome_produto_old == produto.nome:
                            produtos.remove(produto)

                            count = 0
                            for cat in categorias:
                                print("ID: " + str(count) + "Nome: " + cat)
                                count += 1

                            categoria_selecionada = int(
                                input("Favor informar o id da categoria: "))

                            produtos.append(Produto(input("Favor inserir o nome do produto: "),
                                                    input(
                                                    "Insira uma descricao para o produto: "),
                                                    input(
                                                        "Insira um valor para o produto: "),
                                                    input(
                                                        "Insira a quantidade do produto: "),
                                                    categorias[categoria_selecionada]))
                        else:
                            print("O produto informado não foi existe na lista")

                elif(input_usuario == 4):
                    for produto in produtos:
                        print(produto)
