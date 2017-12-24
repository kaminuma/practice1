# ブロック崩し
from tkinter import *

#ボールを表す辞書型データ
ball = {
          "dirx": 15 , #ｘ方向のボールの速さ
          "diry": -15 , #y方向のボールの速さ
          "x" : 350 , #ボールの位置
          "y" : 300 ,
          "w" : 10 , #ボールの幅
        }

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600 , height = 400)
cv.pack()

#画面を描写する
def draw_objects():
    cv.delete('all') #既存の描画を破棄
   #ボールを描画
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"] ,
        ball["x"] + ball["w"], ball["y"] + ball["w"] ,
        fill="green" )

#ボールの移動
def move_ball():
    #仮の変数に移動後の値を記録
    bx = ball["x"] + ball ["dirx"]
    by = ball["y"] + ball ["dirx"]
    #　上左右の壁に当たった？
    if bx < 0 or bx > 600 : ball["dirx"] *= -1
    if by < 0 or by > 400 : ball["diry"] *= -1
    #移動内容を反映
    if 0 <= bx <= 600: ball["x"] = bx
    if 0 <= by <= 400: ball["y"] = by
    
 #ゲームループ
def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)
    
game_loop()
win.mainloop() #ゲームウィンドウを表示