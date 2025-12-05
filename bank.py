class bank():

    def __init__(self, balance: int):
        self._balance = balance

    def confirmation() -> bool:
        print('Confirm the operation: ' + '\n' + '1) Confirm' + '\n' + '2) Refuse')
        return True if int(input('--------------------------------------\n')) == 1 else False

    def transfer(self, sum: int) -> None:
        if self._balance >= sum:
            if bank.confirmation():
                self._balance -= sum
                print('Succesful')
            else: print('You canceled the operation')
        else: print("You don't have enough money")
    def topUp(self, sum: int) -> None:
        if bank.confirmation():
                self._balance += sum
                print('Succesful')
        else: print('You canceled the operation')

    def menu() -> None:
        print('1) View the balance' + '\n' + '2) Transfer money' + '\n' + '3) Top up your account' + '\n' + '4) Exit')


def main():
    account = bank(1000)
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
            print('Unidentified operation')
            
        print('\n======================================\n')

if __name__ == '__main__':

    main()
