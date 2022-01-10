from googletrans import Translator
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("翻訳")

txt = tk.Entry(root, width=45)
txt.pack(side="top")

test = tk.StringVar()
btn = tk.Label(root, text="", textvariable=test)
btn.pack(side="top")

entojp = tk.StringVar()
btn = tk.Label(root, text="", textvariable=entojp)
btn.pack(side="top")


def trans():
    tr = Translator()
    result = tr.translate(txt.get(), src="ja", dest="en").text

    global test
    test.set(result)


def trans_entojp():
    tr = Translator()
    result = tr.translate(txt.get(), src="en", dest="ja").text

    global entojp
    entojp.set(result)


trans_btn = tk.Button(text="日本語>英語", command=trans)
trans_btn.pack(side="left")
en_btn = tk.Button(text="英語>日本語", command=trans_entojp)
en_btn.pack(side="right")
root.mainloop()
