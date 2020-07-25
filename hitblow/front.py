# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as mesg

def ButtonClick():

    b = editbox1.get()

    isok = False
    if len(b) !=4:
        mesg.showinfo("エラー","４桁の数字を入力してください")
    else:
        numberjudgment = True
        for i in range(4):
            if (b[i] < "0") or (b[i] > "9"):
                mesg.showerror("エラー","数字ではありません")
                numberjudgment = False
                break
            if numberjudgment:
                isok = True
    if isok :
        hit = 0
        for i in range(4):
          if a[i] == int(b[i]):
            hit = hit + 1

    blow = 0
    for j in range(4):
        for i in range(4):
            if(int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                blow = blow + 1
                break
    if hit == 4:
        mesg.showinfo("アタリ","おめでとうございます。アタリです")
        root.destroy()
    else:
        rirekibox.insert(tk.END, b + " /H:" + str(hit) + " B:" + str(blow) + "\n")

a = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

root = tk.Tk()
root.geometry("600x400")
root.title("数字当てゲーム")

rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x=400, y=0, width=200, height=400)

label1 =  tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x =120, y = 60)

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
button1.place(x = 220,y = 60)

root.mainloop()