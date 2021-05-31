import livros
import sqlite3

db = sqlite3.connect('livros.db')
cursor = db.cursor()

 
class Interface:

    def register_book(self):
        cursor.execute("SELECT * from livros")
        name = input('Qual é o nome do livro?\n')
        autor = input('Qual o autor?\n')
        editor = input('Editora responsável??\n')
        read = input('O livro foi lido até o final? Sim\nNao')

        cursor.execute(
            "INSERT INTO livros(nome, autor, editora, lido) VALUES(" + name + ", " + autor + ", " + editor + " " + read + ")")
        db.commit()
        print('livro adicionado!')

    def search_book(self):

        print('Qual sera o metodo de pesquisa?\n')
        options = input('Digite 1 para nome do livro\nDigite 2 para autor\nDigite 3 para cancelar:\n')
        if options == 1:
            resN = input('digite o nome do livro:\n')
            resNF = cursor.execute("SELECT nome FROM livros WHERE " + resN + " == nome")
            db.commit()
            print(resNF)

        elif options == 2:
            resAu = input('digite o nome do autor:\n')
            resAF = cursor.execute("SELECT autor FROM livros WHERE " + resAu + " == autor")
            db.commit()
            print(resAF)

        elif options == 3:
            return 0

    def show_list(self):
        #não consegui fazer a informação do sql aparecer
        return 0

    def loop(self):
        while True:
            cmd = input('\n1 - List book:\n2 - Register Book:\n3 - Show List:\n4 - Exit\n')
            if cmd == '1':
                self.search_book()
            elif cmd == '2':
                self.register_book()
            elif cmd == '3':
                self.show_list()
            elif cmd == '4':
                break
            else:
                print('Unknown option. Options only 1-4.')
                continue


if __name__ == '_main_':
    interface = Interface
    interface.loop()
