import livros
import sqlite3

db = sqlite3.connect('livros.db')
cursor = db.cursor()

 
class Interface:

    def register_book(self):
        cursor.execute("SELECT * from livros")
        name = input('Quais é o nome do livro?\n')
        autor = input('Quem foi o autor da Obra?\n')
        editor = input('qual editora foi responsável pela publicação?\n')
        read = input('voce terminou a leitura dele? s/n\n')

        cursor.execute(
            "INSERT INTO livros(nome, autor, editora, lido) VALUES(" + name + ", " + autor + ", " + editor + " " + read + ")")
        db.commit()
        print('livro adicionado!')

    def search_book(self):

        print('Qual sera o metodo de pesquisa?\n')
        opc = input('Digite 1 para nome do livro\nDigite 2 para autor\nDigite 3 para cancelar:\n')
        if opc == 1:
            resN = input('digite o nome do livro:\n')
            resNF = cursor.execute("SELECT nome FROM livros WHERE " + resN + " == nome")
            db.commit()
            print(resNF)

        elif opc == 2:
            resAu = input('digite o nome do autor:\n')
            resAF = cursor.execute("SELECT autor FROM livros WHERE " + resAu + " == autor")
            db.commit()
            print(resAF)

        elif opc == 3:
            return 0

    def show_list(self):
        #não consegui fazer a informação do sql aparecer

        print('o arquivo não pode ser lido na IDE. para mais informações, acesse o README.')

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
