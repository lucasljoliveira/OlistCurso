class Produto:
    __id : int
    __nome : str
    __descricao : str
    __preco : float

    def set_id(self, id) -> None:
        self.__id = int(id)
    def set_nome(self, nome) -> None:
        if nome != '':
            self.__nome = str(nome)
    def set_descricao(self, descricao) -> None:
        if descricao != '':
            self.__descricao = str(descricao)
    def set_preco(self, preco) -> None:
        if int(preco) > 0:
            self.__preco = float(preco)


    def get_id_(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_descricao(self) -> str:
        return self.__descricao
    def get_preco(self) -> float:
        return self.__preco

produtos = []

t_produtos = 0

while(True):
    print('**** CADASTRO DE PRODUTOS ****\n1. Listar Protudos\n2. Cadastrar Produtos\n3. Alterar Produto\n4. Deletar Produto\n0. Sair')
    option = int(input('    Insira uma opção: '))
    if option == 1:
        if len(produtos) == 0:
            print('  Nenhum produto cadastrado.  ')
        else:
            achou = False
            option = int(input('1. Todos\n2. Por Nome\n3. Por Descrição\n4. Por Preço\n    Insira uma opção: '))
            if option == 1:
                for p in produtos:
                    print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                achou = True
            elif option == 2:
                option = str(input('Insira o nome: '))
                for p in produtos:
                    if p.get_nome() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            elif option == 3:
                option = str(input('Insira a descrição: '))
                for p in produtos:
                    if p.get_descricao() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            elif option == 4:
                option = int(input('Insira o preço: '))
                for p in produtos:
                    if p.get_preco() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            if achou == False: 
                print('  Nenhum registro encontrado.')

    elif option == 2:
        try:
            p = Produto()
            p.set_id = t_produtos + 1
            nome = input('    Nome do Produto: ')
            descricao = input('    Descricao do Produto: ')
            preco = input('    Preço do produto: ')
            p.set_nome(nome)
            p.set_descricao(descricao)
            p.set_preco(preco)
        except:
            print('  Informações de produto inválidas')
        finally:    
            produtos.append(p)
            t_produtos = t_produtos + 1

    elif option == 3:
        if len(produtos) == 0:
            print('  Nenhum produto cadastrado.')
        else:
            achou = False
            option = int(input('Pesquisar por: \n1. Nome\n2. Descrição\n3. Preço\nInsira uma opção: '))
            print('** Produtos **')
            for p in produtos:
                print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
            if option == 1:
                option = str(input('Insira o nome atual: '))
                for p in produtos:
                    if p.get_nome() == option:
                        p.set_nome(input('Insira o novo nome: '))
                        achou = True
            elif option == 2:
                option = str(input('Insira a descrição atual: '))
                for p in produtos:
                    if p.get_descricao() == option:
                        p.set_descricao(input('Insira a nova descrição: '))
                        achou = True
            elif option == 3:
                option = int(input('Insira o preço atual: '))
                for p in produtos:
                    if p.get_preco() == option:
                        p.set_preco(input('Insira o novo preço: '))
                        achou = True
            if achou == False: 
                print('  Nenhum registro encontrado.')
    elif option == 4:
        if produtos.count() == 0:
            print('  Nenhum produto cadastrado.')
        else:
            for p in produtos:
                print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
            option = input('Insira o nome do produto: ')
            for p in produtos:
                if p.get_nome() == option:
                    produtos.remove(p)
    elif option == 0:
        print('Saindo!')
        break
No newline at end of file
@@ -1,124 +0,0 @@
class Produto:
    __id : int
    __nome : str
    __descricao : str
    __preco : float

    def set_id(self, id) -> None:
        self.__id = int(id)
    def set_nome(self, nome) -> None:
        if nome != '':
            self.__nome = str(nome)
    def set_descricao(self, descricao) -> None:
        if descricao != '':
            self.__descricao = str(descricao)
    def set_preco(self, preco) -> None:
        if int(preco) > 0:
            self.__preco = float(preco)


    def get_id_(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_descricao(self) -> str:
        return self.__descricao
    def get_preco(self) -> float:
        return self.__preco

produtos = []

t_produtos = 0

while(True):
    print('**** CADASTRO DE PRODUTOS ****\n1. Listar Protudos\n2. Cadastrar Produtos\n3. Alterar Produto\n4. Deletar Produto\n0. Sair')
    option = int(input('    Insira uma opção: '))
    if option == 1:
        if len(produtos) == 0:
            print('  Nenhum produto cadastrado.  ')
        else:
            achou = False
            option = int(input('1. Todos\n2. Por Nome\n3. Por Descrição\n4. Por Preço\n    Insira uma opção: '))
            if option == 1:
                for p in produtos:
                    print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                achou = True
            elif option == 2:
                option = str(input('Insira o nome: '))
                for p in produtos:
                    if p.get_nome() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            elif option == 3:
                option = str(input('Insira a descrição: '))
                for p in produtos:
                    if p.get_descricao() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            elif option == 4:
                option = int(input('Insira o preço: '))
                for p in produtos:
                    if p.get_preco() == option:
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
                        achou = True
            if achou == False: 
                print('  Nenhum registro encontrado.')

    elif option == 2:
        try:
            p = Produto()
            p.set_id = t_produtos + 1
            nome = input('    Nome do Produto: ')
            descricao = input('    Descricao do Produto: ')
            preco = input('    Preço do produto: ')
            p.set_nome(nome)
            p.set_descricao(descricao)
            p.set_preco(preco)
        except:
            print('  Informações de produto inválidas')
        finally:    
            produtos.append(p)
            t_produtos = t_produtos + 1

    elif option == 3:
        if len(produtos) == 0:
            print('  Nenhum produto cadastrado.')
        else:
            achou = False
            option = int(input('Pesquisar por: \n1. Nome\n2. Descrição\n3. Preço\nInsira uma opção: '))
            print('** Produtos **')
            for p in produtos:
                print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
            if option == 1:
                option = str(input('Insira o nome atual: '))
                for p in produtos:
                    if p.get_nome() == option:
                        p.set_nome(input('Insira o novo nome: '))
                        achou = True
            elif option == 2:
                option = str(input('Insira a descrição atual: '))
                for p in produtos:
                    if p.get_descricao() == option:
                        p.set_descricao(input('Insira a nova descrição: '))
                        achou = True
            elif option == 3:
                option = int(input('Insira o preço atual: '))
                for p in produtos:
                    if p.get_preco() == option:
                        p.set_preco(input('Insira o novo preço: '))
                        achou = True
            if achou == False: 
                print('  Nenhum registro encontrado.')
    elif option == 4:
        if produtos.count() == 0:
            print('  Nenhum produto cadastrado.')
        else:
            for p in produtos:
                print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()))
            option = input('Insira o nome do produto: ')
            for p in produtos:
                if p.get_nome() == option:
                    produtos.remove(p)
    elif option == 0:
        print('Saindo!')
        break
