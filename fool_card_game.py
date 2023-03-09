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

#        print('Ваши карты: ', str(self.my_keys))
#        print('Карты компьютера: ', str(self.pc_keys))

    def my_move(self):
        move_random_card = random.choice(self.my_card)
        index_card = self.my_card.index(move_random_card)
        print("Ваш ход:", self.my_card[index_card])
        my_move = self.my_keys[index_card]

        for i in self.pc_keys:
            if i > my_move:
                index_card_pc = self.pc_keys.index(i)
                self.pc_keys.remove(i)
                self.pc_card.pop(index_card_pc)
                index_card_my = self.my_keys.index(my_move)
                self.my_keys.remove(my_move)
                self.my_card.pop(index_card_my)
                return "Карты отбиты!"
                break
            elif i < my_move:
                continue
            else:
                index_card_my = self.my_keys.index(my_move)
                card_my_move = self.my_card[index_card_my]
                self.pc_keys.append(my_move)
                self.pc_card.append(card_my_move)
                self.my_keys.remove(i)
                self.my_card.pop(index_card_my)
                return 'Карты приняты!'

    def pc_move(self):
        move_random_card = random.choice(self.pc_card)
        index_card = self.pc_card.index(move_random_card)
        print("Ход компьютера:", self.pc_card[index_card])
        pc_move = self.pc_keys[index_card]

        for i in self.my_keys:
            if i > pc_move:
                index_card_my = self.my_keys.index(i)
                self.my_keys.remove(i)
                self.my_card.pop(index_card_my)
                index_card_pc = self.pc_keys.index(pc_move)
                self.pc_keys.remove(pc_move)
                self.pc_card.pop(index_card_pc)
                return "Карты отбиты!"
                break
            elif i < pc_move:
                continue
            else:
                index_card_pc = self.pc_keys.index(pc_move)
                card_pc_move = self.pc_card[index_card_pc]
                self.my_keys.append(pc_move)
                self.my_card.append(card_pc_move)
                self.pc_keys.remove(i)
                self.pc_card.pop(index_card_pc)
                return 'Карты приняты!'
    def mode_game(self):
        if len(self.my_card) < len(self.pc_card):
                return 'Вы выиграли!'
        if len(self.my_card) > len(self.pc_card):
                return 'Вы проиграли!'
        if len(self.my_card) == len(self.pc_card):
                return 'Ничья!'

if __name__ == '__main__':
    fool_game = Fool()
    print(fool_game.my_card, fool_game.pc_card)
    print(fool_game.my_move())
    print(fool_game.pc_move())
    print(fool_game.mode_game())

