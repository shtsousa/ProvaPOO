import livros
import sqlite3

db = sqlite3.connect('livros.db')
cursor = db.cursor()
 
class Interface:
  
    def search_book(self):

        print('Insert your desired option!\n')
        options = input('1 - Name \n2-Author\n3-Press 3 to cancel: \n')
        if options == 1:
            insN = input('Insert book name:\n')
            insNF = cursor.execute("SELECT nome FROM livros WHERE " + insN + " == name")
            db.commit()
            print(insNF)

        elif options == 2:
            resAu = input('Insert name from author:\n')
            resAF = cursor.execute("SELECT autor FROM livros WHERE " + resAu + " == author")
            db.commit()
            print(resAF)

        elif options == 3:
            return 0

    def register_book(self):
        name = input('Name of book?\n')
        cursor.execute("SELECT * FROM livros")
        autor = input('Author?\n')
        editor = input('Publishing Company?\n')
        read = input('Did you read the whole book? Yes\nNot')

        cursor.execute(
            "INSERT INTO livros(name, author, editor, read) VALUES(" + name + ", " + autor + ", " + editor + " " + read + ")")
        db.commit()
        print('Ok, book inserted')
    
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
