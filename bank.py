import sqlite3

class bank():

    def __init__(self):
        self._balance = 0
        self._user = None
        self._password = None

    def start(self) -> None:
        with sqlite3.connect('bankUsers.db') as db:
            c = db.cursor()
            inputl = input('1) LogIn\n2) SingUp\n')
            if inputl == '1':
                try:
                    self._user = input('--------------------------------------\nUsername: ')
                    self._password = input('Password: ')
                    c.execute(f"SELECT * FROM bankUsers WHERE user = '{self._user}' AND password = '{self._password}'")
                    balance = c.fetchall()
                    print('>>>Succesful')
                    self._balance = balance[0][2]
                    
                except:
                    print('>>>Userame or password not correct, try again or singUp\n--------------------------------------')
                    self.start()

            elif inputl == '2':
                self._user = input('--------------------------------------\nUsername: ')
                self._password = input('Password: ')
                c.execute(f"INSERT INTO bankUsers VALUES ('{self._user}', '{self._password}', {0})")
                return 0
            else:
                print('>>>Unidentified operation')
                self.start()
            db.commit()
    
    def save(self) -> None:
        with sqlite3.connect('bankUsers.db') as db:
            c = db.cursor()
            c.execute(f"UPDATE bankUsers SET balance = {self._balance} WHERE user = '{self._user}' AND password = '{self._password}'")
            db.commit()

    def confirmation() -> bool:
        print('Confirm the operation: ' + '\n' + '1) Confirm' + '\n' + '2) Refuse')
        return True if int(input('--------------------------------------\n')) == 1 else False

    def transfer(self, sum: int) -> None:
        if self._balance >= sum:
            if bank.confirmation():
                self._balance -= sum
                print('>>>Succesful')
            else: print('>>>You canceled the operation')
        else: print(">>>You don't have enough money")
    def topUp(self, sum: int) -> None:
        if bank.confirmation():
                self._balance += sum
                print('>>>Succesful')
        else: print('>>>You canceled the operation')

    def menu(self) -> None:
        print('1) View the balance' + '\n' + '2) Transfer money' + '\n' + '3) Top up your account' + '\n' + '4) Exit')

"""with sqlite3.connect('bankUsers.db') as db:
    c = db.cursor()

    c.execute('''
    CREATE TABLE bankUsers (
        user text,
        password text,
        balance integer        
    )
    ''')

    c.execute("INSERT INTO bankUsers VALUES ('J-zzz0', 'admin', 999)")
    db.commit()"""

def main():
    account = bank()
    account.start()
    print('\n======================================\n')
    while True:
        account.menu()
        inputl = input('--------------------------------------\n')
        print('\n======================================\n')
        if inputl == '1':
            print(f'Your balance: {account._balance}')
        elif inputl == '2':
            account.transfer(int(input('Amount: ')))
        elif inputl == '3':
            account.topUp(int(input('Amount: ')))
        elif inputl == '4':
            break
        else:
            print('>>>Unidentified operation')
            
        print('\n======================================\n')
    account.save()

if __name__ == '__main__':

    main()

