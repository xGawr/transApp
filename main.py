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


def trans():
    tr = Translator()
    result = tr.translate(txt.get(), src="ja", dest="en").text

    global test
    test.set(result)


trans_btn = tk.Button(text="翻訳", command=trans)
trans_btn.pack(side="top")

root.mainloop()
