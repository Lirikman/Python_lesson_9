import random


class Fool:

    def __init__(self):
        cards = {1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 'Jack', 7: 'Queen', 8: 'King', 9: 'Ace'}

        self.my_card = []
        self.my_keys = []

        self.pc_card = []
        self.pc_keys = []

        for i in range(6):
            random_card = random.choice(list(cards.items()))
            self.my_card.append(random_card[1])
            self.my_keys.append(random_card[0])

        for i in range(6):
            random_card = random.choice(list(cards.items()))
            self.pc_card.append(random_card[1])
            self.pc_keys.append(random_card[0])

        print('Ваши карты: ', str(self.my_keys))
        print('Карты компьютера: ', str(self.pc_keys))

    def my_move(self):
        move_random_card = random.choice(self.my_card)
        index_card = self.my_card.index(move_random_card)
        print("Ваш ход:", self.my_card[index_card])
        my_move = self.my_keys[index_card]

        for i in self.pc_keys:
            if self.pc_keys[i] > my_move:
                self.pc_keys.remove(i)
                self.pc_card.pop(i)
                self.my_keys.remove(i)
                self.my_card.pop(i)
                return "Карты отбиты!"
                break
            elif self.pc_keys[i] < my_move:
                continue
            else:
                self.pc_keys.append(my_move)
                self.pc_card.append(self.my_card[i])
                self.my_keys.remove(i)
                self.my_card.pop(i)
                return 'Карты приняты!'

    def pc_move(self):
        move_random_card = random.choice(self.pc_card)
        index_card = self.pc_card.index(move_random_card)
        print("Ход компьютера:", self.pc_card[index_card])
        pc_move = self.pc_keys[index_card]

        for i in self.my_keys:
            if self.my_keys[i] > pc_move:
                self.my_keys.remove(i)
                self.my_card.pop(i)
                return "Карты отбиты!"
                break
            elif self.my_keys[i] < pc_move:
                i += 1
                continue
            else:
                self.my_keys.append(pc_move)
                self.my_card.append(self.my_card[i])
                return 'Карты приняты!'


if __name__ == '__main__':
    fool_game = Fool()
    print(fool_game.my_card, fool_game.pc_card)
    print(fool_game.my_move())
    print(fool_game.pc_move())

