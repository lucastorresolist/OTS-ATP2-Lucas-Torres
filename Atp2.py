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
    # __id: int
    # __nome: str
    # __descricao: str
    # __preco: float
    # __quantidade: int
    # __categoria: Categoria

    def __init__(self, nome, descricao, preco, quantidade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    # def __repr__(self):
    #     return str(self.__dict__)

    # def get_nome(self):
    #     return self.__nome

    # def set_nome(self, nome):
    #     self.__nome = nome

    # def get_descricao(self):
    #     return self.__descricao

    # def set_descricao(self, descricao):
    #     self.__descricao = descricao

    # def get_preco(self):
    #     return self.__preco

    # def set_preco(self, preco):
    #     self.__preco = preco

    # def get_quantidade(self):
    #     return self.__quantidade

    # def set_quantidade(self, quantidade):
    #     self.__quantidade = quantidade

    # def get_categoria(self):
    #     return self.__categoria

    # def set_categoria(self, categoria):
    #     self.__categoria = categoria


if __name__ == "__main__":

    menu: int = 1

    cat = Categoria()
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

                elif(input_usuario == 2):
                    nome_produto = input(
                        "Favor inserir o nome do produto a ser excluido: ")
                    for produto in produtos:
                        if produto.nome == nome_produto:
                            produtos.remove(produto)

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
                        print("Nome: " + produto.nome +
                              " Descricao: " + produto.descricao +
                              " Preco: " + produto.preco +
                              " Quantidade: " + produto.quantidade +
                              " Categoria: " + produto.categoria)
