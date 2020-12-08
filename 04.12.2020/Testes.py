class Pessoa:
    __nome : str
    __sobrenome : str
    __idade : int

    def nome_completo(self) -> None:
        print(self.__nome + ' ' + self.__sobrenome)

    def set_nome(self, nome) -> None:
        self.__nome = nome
    def set_sobrenome(self, sobrenome) -> None:
        self.__sobrenome = sobrenome
    def set_idade(self, idade) -> None:
        self.__idade = idade

    def get_nome(self) -> str:
        return self.__nome
    def get_sobrenome(self) -> str:
        return self.__sobrenome
    def get_idade(self) -> int:
        return self.__idade

p = Pessoa()

p.set_nome('Lucas')
p.set_sobrenome('Oliveira')
p.set_idade(26)

p.nome_completo()
print(p.get_nome() + ' ' + p.get_sobrenome() + ', ' + str(p.get_idade()))