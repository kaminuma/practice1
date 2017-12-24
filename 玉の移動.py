# �u���b�N����
from tkinter import *

#�{�[����\�������^�f�[�^
ball = {
          "dirx": 15 , #�������̃{�[���̑���
          "diry": -15 , #y�����̃{�[���̑���
          "x" : 350 , #�{�[���̈ʒu
          "y" : 300 ,
          "w" : 10 , #�{�[���̕�
        }

# �E�B���h�E�̍쐬
win = Tk()
cv = Canvas(win, width = 600 , height = 400)
cv.pack()

#��ʂ�`�ʂ���
def draw_objects():
    cv.delete('all') #�����̕`���j��
   #�{�[����`��
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"] ,
        ball["x"] + ball["w"], ball["y"] + ball["w"] ,
        fill="green" )

#�{�[���̈ړ�
def move_ball():
    #���̕ϐ��Ɉړ���̒l���L�^
    bx = ball["x"] + ball ["dirx"]
    by = ball["y"] + ball ["dirx"]
    #�@�㍶�E�̕ǂɓ��������H
    if bx < 0 or bx > 600 : ball["dirx"] *= -1
    if by < 0 or by > 400 : ball["diry"] *= -1
    #�ړ����e�𔽉f
    if 0 <= bx <= 600: ball["x"] = bx
    if 0 <= by <= 400: ball["y"] = by
    
 #�Q�[�����[�v
def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)
    
game_loop()
win.mainloop() #�Q�[���E�B���h�E��\��