class livro:
    def _init_(self, numero, nome, autor, editora):
        self.numero = numero
        self.nome = nome
        self.autor = autor
        self.editora = editora

    def setNumero(self, numero):
        self.numero = numero

    def setNome(self, nome):
        self.nome = nome

    def setAutor(self, autor):
        self.autor = autor

    def setEditora(self, editora):
        self.editora = editora

    def getNumero(self):
        return self.numero

    def getNome(self):
        return self.nome

    def getAutor(self):
        return self.autor

    def getEditora(self):
        return self.editora
