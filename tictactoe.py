import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        #show board
        print(self.game_engine)
        #무한반복
        while True:
            #row, col 입력받자
            row = int(input('row: '))
            col = int(input('col: '))
            #말을 놓자
            self.game_engine.set(row, col)
            #show board
            print(self.game_engine)
            #만약에 승자나 무승부가 있으면 끝
            winner = self.game_engine.check_winner
            if winner == 'O' or winner == 'X' or winner == 'd':
                break

        #결과 출력하자
        if winner == 'O':
            print('O 승리')
        elif winner == 'X':
            print('X 승리')
        elif winner == 'd':
            print('무승부')

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        #창의 크기
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE / 3

        #윈도우 그리기
        self.root = tkinter.Tk()

        #창
        self.root.geometry(str(CANVAS_SIZE) + 'x' + str(CANVAS_SIZE))   #300x300
        self.root.title('틱 택 토')  #프로그램 이름
        self.root.resizable(width=False, height=False)  #사이즈를 바꿀 수 없도록 고정
        self.canvas = tkinter.Canvas(self.root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        #이미지 가져오기
        self.images = {}        #{'O': PhotoImage객체(O.gif), 'X' : PhotoImage객체(X.gif)}
        self.images['O'] = tkinter.PhotoImage(file='O.gif') #git만 가능
        self.images['X'] = tkinter.PhotoImage(file='X.gif')

        #클릭 핸들러를 가져옴
        self.canvas.bind('<Button-1>', self.click_handler)  #바로 실행하는 것이 아니라 함수 지정만 해줌

    def click_handler(self, event):
        x = event.x
        y = event.y
        col = x // 100 + 1
        row = y // 100 + 1
        self.game_engine.set(row, col)
        #print(self.game_engine)     #draw_board()
        self.draw_board()   #화면에 그림
        if self.game_engine.check_winner == 'O':
            messagebox.showinfo('Game Over', 'O가 이겼습니다.')
            #끝내기
            self.root.quit()
        elif self.game_engine.check_winner == 'X':
            messagebox.showinfo('Game Over', 'X가 이겼습니다.')
            #끝내기
            self.root.quit()
        elif self.game_engine.check_winner == 'd':
            messagebox.showinfo('Game Over', '무승부입니다.')
            #끝내기
            self.root.quit()

    def draw_board(self):
        #self.game_engine.board
        x = 0
        y = 0
        for i, v in enumerate(self.game_engine.board):
            # if v == 'X':
            #     self.canvas.create_image(x, y, anchor='nw', image=self.images['X'])
            # elif v == 'O':
            #     self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])

            if v != '.':
                self.canvas.create_image(x, y, anchor='nw', image=self.images[v])

            x += self.TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TILE_SIZE

    def play(self):
        # self.canvas.create_image(0, 0, anchor='nw', image=self.images['X'])
        # self.canvas.create_image(200, 0, anchor='nw', image=self.images['X'])
        # self.canvas.create_image(0, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(200, 100, anchor='nw', image=self.images['O'])
        # self.canvas.create_image(100, 200, anchor='nw', image=self.images['O'])
        self.root.mainloop()    #창이 뜸


if __name__ == '__main__':
    #ttt = Tictactoe()
    ttt = TictactoeGUI()
    ttt.play()