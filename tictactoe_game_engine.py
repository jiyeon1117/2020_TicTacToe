#    그림 그릴 때와 이벤트 처리할 때 오류 나기 쉬움

class TictactoeGameEngine:
    def __init__(self): #객체 초기화 자료 생성
        self.board = list('.' * 9)  #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_turn = 'X'

    def get(self, row, col):
        row -= 1
        col -= 1
        return self.board[row * 3 + col]

    def set(self, row, col):
        if row < 1 and row > 3:
            return
        if col < 1 and col > 3:
            return
        if self.get(row, col) != '.':
            return

        row -= 1
        col -= 1
        self.board[row * 3 + col] = self.current_turn
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'
        # if self.current_turn == 'X':
        #     self.current_turn = 'O'
        # else:
        #     self.current_turn = 'X'

    @property
    def check_winner(self):
        #-
        for i in range(1, 3+1):
            if self.get(i, 1) == self.get(i, 2) == self.get(i, 3) != '.':
                return self.get(i, 1)
            #|
            if self.get(1, i) == self.get(2, i) == self.get(3, i) != '.':
                return self.get(1, i)
        #/
        if self.get(1, 3) == self.get(2, 2) == self.get(3, 1) != '.':
            return self.get(2, 2)
        #\
        if self.get(1, 1) == self.get(2, 2) == self.get(3, 3) != '.':
            return self.get(2, 2)
        #draw
        if not '.' in self.board:
            return 'd'

    def __str__(self):  #화면에 보이는 것
        s = ''
        for i, v in enumerate(self.board):
            s += v + '\t'
            if i % 3 == 2:
                s += '\n'

        return s


if __name__ == '__main__':
    ttt_game_engine = TictactoeGameEngine()
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(2, 2)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(1, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(2, 1)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(1, 2)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    ttt_game_engine.set(2, 3)
    print(ttt_game_engine)
    print(ttt_game_engine.check_winner)
    #이미 올린 자리에 올리면 게임이 끝나지 안흔다.