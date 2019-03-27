import tkinter
from tkinter import *
from tkinter import filedialog as fd


def quit(ev):
    global root
    root.destroy()


def encode_vienera(ev):
    text = textbox.get(1.0, END).lower()
    key = entry_key.get().lower()

    key_len = len(key)
    if len(key) < len(text):
        for i in range(key_len, len(text) - 1):
            key += key[i - key_len]

    result = ''
    for i in range(0, len(text) - 1):
        old_ord = ord(text[i])

        if old_ord == ord(' '):
            result += ' '
            continue

        old_ord -= 97
        key_ord = ord(key[i])
        key_ord -= 97
        if 0 <= old_ord <= 25 and 0 <= key_ord <= 25:
            encoded_ord = (old_ord + key_ord) % 26

            result += chr(encoded_ord + 97)

    textbox.delete(1.0, END)
    textbox.insert(1.0, result.upper())


def encode_caesar(ev):
    text = textbox.get(1.0, END).lower()
    offset = int(spinbox_offset.get())
    result = ''
    for char in text:
        old_ord = ord(char)

        if old_ord == ord(' '):
            result += ' '
            continue

        old_ord -= 97
        if 0 <= old_ord <= 25:
            encoded_ord = (old_ord + offset) % 26

            result += chr(encoded_ord + 97)

    textbox.delete(1.0, END)
    textbox.insert(1.0, result.upper())


def open_from_file():
    file_name = fd.askopenfilename()
    if file_name == '':
        return
    f = open(file_name)
    s = f.read()
    textbox.delete(1.0, END)
    textbox.insert(1.0, s)
    f.close()


def save_to_file():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    if file_name == '':
        return
    f = open(file_name, 'w')
    s = textbox.get(1.0, END)
    f.write(s)
    f.close()


root = tkinter.Tk()
root.title('Caesar and Vienera encrypter (only English)')

panelFrame = Frame(root, height=60, bg='lightgray')
textFrame = Frame(root, height=100, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word', highlightthickness=0)
scrollbar = Scrollbar(textFrame)

textbox.pack(side='left', fill='both', expand=1, padx=10, pady=10)
scrollbar.pack(side='right', fill='y')

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

# panel elements

label_offset = Label(panelFrame, text="Offset:", bg='lightgray')
label_offset.place(x=10, y=10, width=45, height=40)
spinbox_offset = Spinbox(panelFrame, from_=-20, to=20)
spinbox_offset.delete(0, END)
spinbox_offset.insert(0, 0)
spinbox_offset.place(x=65, y=10, width=55, height=40)

button_encrypt_caesar = Button(panelFrame, text='Encrypt Caesar')
button_encrypt_caesar.place(x=130, y=10, width=110, height=40)

label_key = Label(panelFrame, text="Key:", bg='lightgray')
label_key.place(x=250, y=10, width=30, height=40)
entry_key = Entry(panelFrame)
entry_key.place(x=280, y=10, width=110, height=40)

button_encrypt_vienera = Button(panelFrame, text='Encrypt Vienera')
button_encrypt_vienera.place(x=340, y=10, width=55, height=40)
quit_btn = Button(panelFrame, text='Quit')

button_encrypt_vienera.place(x=405, y=10, width=110, height=40)
quit_btn.place(x=600, y=10, width=40, height=40)

button_encrypt_caesar.bind("<Button-1>", encode_caesar)
button_encrypt_vienera.bind("<Button-1>", encode_vienera)
quit_btn.bind("<Button-1>", quit)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_from_file)
file_menu.add_command(label="Save", command=save_to_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
