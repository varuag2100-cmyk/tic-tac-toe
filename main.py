
import tkinter as tk
from tkinter import messagebox

HUMAN="X"
AI="O"

WINS=[
(0,1,2),(3,4,5),(6,7,8),
(0,3,6),(1,4,7),(2,5,8),
(0,4,8),(2,4,6)
]

board=[""]*9

def winner(b):
    for a,c,d in WINS:
        if b[a] and b[a]==b[c]==b[d]:
            return b[a]
    if "" not in b:
        return "Draw"
    return None

def minimax(b,maxing):
    w=winner(b)
    if w==AI: return 1
    if w==HUMAN: return -1
    if w=="Draw": return 0
    if maxing:
        best=-2
        for i,v in enumerate(b):
            if v=="":
                b[i]=AI
                best=max(best,minimax(b,False))
                b[i]=""
        return best
    else:
        best=2
        for i,v in enumerate(b):
            if v=="":
                b[i]=HUMAN
                best=min(best,minimax(b,True))
                b[i]=""
        return best

def ai_move():
    best=-2
    move=None
    for i,v in enumerate(board):
        if v=="":
            board[i]=AI
            score=minimax(board,False)
            board[i]=""
            if score>best:
                best=score
                move=i
    if move is not None:
        board[move]=AI
        buttons[move]["text"]=AI
    end=winner(board)
    if end:
        finish(end)

def click(i):
    if board[i] or winner(board):
        return
    board[i]=HUMAN
    buttons[i]["text"]=HUMAN
    end=winner(board)
    if end:
        finish(end)
    else:
        root.after(250,ai_move)

def finish(result):
    if result=="Draw":
        message="It's a Draw!"
    elif result==HUMAN:
        message="You Win!"
    else:
        message="AI Wins!"
    if messagebox.askyesno("Game Over",message+"\n\nPlay again?"):
        reset()

def reset():
    global board
    board=[""]*9
    for b in buttons:
        b.config(text="")

root=tk.Tk()
root.title("Unbeatable Tic Tac Toe")

buttons=[]
for r in range(3):
    for c in range(3):
        idx=r*3+c
        bt=tk.Button(root,text="",font=("Arial",28),width=4,height=2,
                     command=lambda i=idx:click(i))
        bt.grid(row=r,column=c,padx=4,pady=4)
        buttons.append(bt)

tk.Button(root,text="Restart",font=("Arial",12),
          command=reset).grid(row=3,column=0,columnspan=3,sticky="ew",pady=5)

root.mainloop()
