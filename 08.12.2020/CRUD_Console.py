class Categoria:
    __id : int
    __nome : str
    __id_mae : int

    def set_id(self, id) -> None:
        self.__id = int(id)
    def set_nome(self, nome) -> None:
        if nome != '':
            self.__nome = str(nome)
    def set_id_mae(self, id) -> None:
            self.__id_mae = id

    def get_id(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_id_mae(self) -> int:
        return self.__id_mae

class Produto:
    __id : int
    __nome : str
    __descricao : str
    __preco : float
    __peso : float
    __dimensoes : list
    __categorias : list

    def set_id(self, id) -> None:
        self.__id = int(id)
    def set_nome(self, nome) -> None:
        try:
            if nome != '':
                self.__nome = str(nome)
            else:
                raise Exception
        except:
            print('O nome deve ser alfanumérico e não nulo.')
    def set_descricao(self, descricao) -> None:
        try:
            if len(descricao) >= 20:
                self.__descricao = str(descricao)
            else:
                raise Exception
        except:
            print('A descrição deve conter no minímo 20 caracteres alfanuméricos.')
    def set_preco(self, preco) -> None:
        try:
            if int(preco) > 0:
                self.__preco = float(preco)
            else:
                raise Exception
        except:
            print('O preço deve ser numérico e maior que zero.')
    def set_peso(self, peso) -> None:
        try:
            if float(peso) > 0:
                self.__peso = float(peso)
            else:
                raise Exception
        except:
            print('O peso deve ser numérico e maior do que zero.')

    def set_dimensoes(self, dimensoes) -> None:
        try:
            dimensoes[0] = float(dimensoes[0])
            dimensoes[1] = float(dimensoes[1])
            dimensoes[2] = float(dimensoes[2])
            if dimensoes[0] >= 0 and dimensoes[1] >= 0 and dimensoes[2] >= 0:
                self.__dimensoes = dimensoes

            else:
                raise Exception
        except:
            print('As dimensões devem conter valores numéricos acima de zero.')

    def set_categorias(self, cat):
        try:
            if len(cat) > 0:
                self.__categorias = cat
            else:
                raise Exception
        except:
            print('O produto deve pertencer a pelo menos uma categoria.')

    def get_id_(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_descricao(self) -> str:
        return self.__descricao
    def get_preco(self) -> float:
        return self.__preco
    def get_peso(self) -> float:
        return self.__peso
    def get_dimensoes(self) -> list:
        return self.__dimensoes
    def get_categorias(self) -> list:
        return self.__categorias
    
    
    

produtos = []
categorias = []

c = Categoria()
d = Categoria()
c.set_id(1)
c.set_nome('Lucas')
c.set_id_mae('')
categorias.append(c)
d.set_id(2)
d.set_nome('thiago')
d.set_id_mae(1)
categorias.append(d)

t_produtos = 0
t_categorias = 2

while(True):
    print('**** CADASTRO DE PRODUTOS ****\n1. Listar Categorias\n2. Listar Produtos\n3. Cadastrar Categorias\n4. Cadastrar Produtos\n5. Alterar Produto\n6. Deletar Produto\n0. Sair')
    option = int(input('    Insira uma opção: '))
    if option == 1:
        if len(categorias) == 0:
            print('  Nenhuma categoria cadastrada.  ')
        else:

            for c in categorias:
                    #mae = ''
                    #print(c.get_id_mae())
                    #if c.get_id_mae() != None:
                    #    for c2 in categorias:
                    #        if c2.get_id() == c.get_id_mae():
                    #            mae = c2.get_nome()
                    #            print(mae)
                print('ID: ' + str(c.get_id()) + ', Nome: ' + c.get_nome() + ', ID Categoria Principal: ' + str(c.get_id_mae()))
                achou = True
    if option == 2:
        if len(categorias) == 0:
            print('  Nenhum produto cadastrado.  ')
        else:
            achou = False
            option = int(input('1. Todos\n2. Por Nome\n3. Por Descrição\n4. Por Preço\n    Insira uma opção: '))
            if option == 1:
                for p in produtos:
                    cat = ''
                    for c in p.get_categorias():
                        for c1 in categorias:
                            if c1.get_id() == c:
                                cat = cat + c1.get_nome() + ', '
                    print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()) + ', Dimensões: ' + str(p.get_dimensoes()[0]) + ' x ' + str(p.get_dimensoes()[1]) + ' x ' + str(p.get_dimensoes()[2]) + ', Categorias: ' + cat)
                achou = True
            elif option == 2:
                option = str(input('Insira o nome: '))
                for p in produtos:
                    if p.get_nome() == option:
                        cat = ''
                        for c in p.get_categorias():
                            for c1 in categorias:
                                if c1.get_id() == c:
                                    cat = cat + c1.get_nome() + ', '
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()) + ', Dimensões: ' + str(p.get_dimensoes()[0]) + ' x ' + str(p.get_dimensoes()[1]) + ' x ' + str(p.get_dimensoes()[2]) + ', Categorias: ' + cat)
                        achou = True
            elif option == 3:
                option = str(input('Insira a descrição: '))
                for p in produtos:
                    if p.get_descricao() == option:
                        cat = ''
                        for c in p.get_categorias():
                            for c1 in categorias:
                                if c1.get_id() == c:
                                    cat = cat + c1.get_nome() + ', '
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()) + ', Dimensões: ' + str(p.get_dimensoes()[0]) + ' x ' + str(p.get_dimensoes()[1]) + ' x ' + str(p.get_dimensoes()[2]) + ', Categorias: ' + cat)
                        achou = True
            elif option == 4:
                option = int(input('Insira o preço: '))
                for p in produtos:
                    if p.get_preco() == option:
                        cat = ''
                        for c in p.get_categorias():
                            for c1 in categorias:
                                if c1.get_id() == c:
                                    cat = cat + c1.get_nome() + ', '
                        print('Nome: ' + p.get_nome() + ', Descrição: ' + p.get_descricao() + ', Preço: R$ ' + str(p.get_preco()) + ', Dimensões: ' + str(p.get_dimensoes()[0]) + ' x ' + str(p.get_dimensoes()[1]) + ' x ' + str(p.get_dimensoes()[2]) + ', Categorias: ' + cat)
                        achou = True
            if achou == False: 
                print('  Nenhum registro encontrado.')
    elif option == 3:
        try:
            c = Categoria()
            c.set_id(t_categorias + 1)
            c_mae = ''
            nome = input('    Nome da Categoria: ')
            option = input('É uma subcategoria? Digite 1 para Sim: ')
            if option == '1':
                for c1 in categorias:
                    if c1.get_id_mae() == '':
                        print('ID: ' + str(c1.get_id()) + ', Nome: ' + c1.get_nome())
                c_mae = input('    Insira o ID da principal: ')
            
            c.set_nome(nome)
            c.set_id_mae(c_mae)
        except Exception as e:
            print('  Informações da categoria inválidas. %s' % (str(e)))
        finally:    
            categorias.append(c)
            t_categorias = t_categorias + 1

    elif option == 4:
        
        p = Produto()
        p.set_id = t_produtos + 1
        nome = input('    Nome do Produto: ')
        descricao = input('    Descrição do Produto: ')
        preco = input('    Preço do produto: ')


        altura = input('    Altura do produto: ')
        largura = input('    Largura do produto: ')
        comprimento = input('    Comprimento do produto: ')
        dimensoes = [altura, largura, comprimento]

        p_categorias = []
        while(True):
            existe = False
            for c in categorias:
                if c.get_id_mae() == '':
                    print('ID: ' + str(c.get_id()) + ', Nome: ' + c.get_nome())
            try:
                c_id = int(input('Insira o ID da categoria: '))
                for c in categorias:
                    if c.get_id_mae() == '':
                        if c.get_id() == c_id:
                            existe = True
                if existe == True:
                    p_categorias.append(c_id)
                    option = input('Deseja inserir outra categoria? Digite 1 para Sim: ')
                    if option != '1':
                        break
                else:
                    raise Exception
            except:
                print('ID da categoria inválido.')

        option = input('Deseja inserir uma subcategoria? Digite 1 para Sim: ')
        if option == '1':
            for c1 in p_categorias:
                print('Categoria ID ' + str(c1) + ': ')
                while(True):
                    existe = False
                    t_subcategoria = 0
                    for c in categorias:
                        if c.get_id_mae() != '':
                            if int(c.get_id_mae()) == c1:
                                print('ID: ' + str(c.get_id()) + ', Nome: ' + c.get_nome())
                                t_subcategoria += 1
                    if t_subcategoria > 0:
                        try:
                            c_id = int(input('Insira o ID da subcategoria: '))
                            for c in categorias:
                                if c.get_id_mae() == c1:
                                    if c.get_id() == c_id:
                                        existe = True
                            if existe == True:
                                p_categorias.append(c_id)
                                option = input('Deseja inserir outra subcategoria da categoria ' + str(c1) + '? Digite 1 para Sim: ')
                                if option != '1':
                                    break
                            else:
                                raise Exception
                        except:
                            print('ID da subcategoria inválido.')
                    else:
                        print('A categoria ' + str(c1) + ' não possui subcategoria a serem inseridas.')
                        break
            


        p.set_nome(nome)
        p.set_descricao(descricao)
        p.set_preco(preco)
        p.set_dimensoes(dimensoes)
        p.set_categorias(p_categorias)

        produtos.append(p)
        t_produtos = t_produtos + 1

        print('Produto cadastrado com sucesso.')

    elif option == 5:
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
    elif option == 6:
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
        print('Apagando galeria de produtos e categorias!')
        print('Saindo!')
        break