class livro:
    def _init_(self, codigo, nome, autor, editora):
        self.nome = nome
        self.editora = editora
        self.codigo = codigo
        self.autor = autor

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getAutor(self):
        return self.autor

    def getEditora(self):
        return self.editora

    def setCodigo(self, codigo):
        self.numero = numero

    def setNome(self, nome):
        self.nome = nome

    def setAutor(self, autor):
        self.autor = autor

    def setEditora(self, editora):
        self.editora = editora


class Interface:
    alunos = []

    def registra_Livro(self):
        nome = input('Quais é o nome do livro?\n')
        autor = input('Quem foi o autor da Obra?\n')

        self.livros.append(livro(nome, autor, ))
        print('livro adicionado!')

    def procurar_Livros(self):
        for i, livro in enumerate(self.livros):
            print(i, livro.nome)

    def mostrar_Lista(self):

     def loop(self):
        while True:
            cmd = input('\n1 - Listar livros\n2 - registrar livro\n3 - Mudar senha\n')
            if cmd == '1':
                self.search_book()
            elif cmd == '2':
                self.registraLivro()
            elif cmd == '3':
                self.mudar_senha()
            else:
                print('opção invalida. por favor, selecione APENAS os itens listados.')
                continue

