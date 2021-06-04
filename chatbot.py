import time
import tkinter
from tkinter import *
c1 = '#263238'
c2 = '#faa21f'
c3 = '#1e282d'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'
root=Tk()
root.title("Chat Bot")
root.geometry("400x500")

root.resizable(width=False,height=False)


def submit(ii):
    """
function for producing response of
        request of user

    """


    global chat_raw
    chat_raw = messageWindow.get('1.0', 'end-1c')

    messageWindow.delete('1.0', END)

    global top
    top = "C:\\Users\\vanas\\PycharmProjects\\mini\\sss.txt"
    a = open(top, 'r')

    global doc
    doc = a.readlines()
    chat = chat_raw.lower()
    chat = chat.replace(' ', '')
    chat_raw="YOU  ---->"+chat_raw
    listbox.insert(ii,chat_raw)
    ii+=1


    global answer



    if chat=='hii':
        answer = "BOT--->  Hii !!, Hloo !! .... How can i help you ??"
    elif chat == "group":
        answer = "BOT--->  SAIKIRAN"
    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "what is my name?" or chat == "whatsmyname" or chat == 'myname?' or chat == 'myname':
        answer = "BOT--->  You are a User!!"

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat == 'yourname':
        answer = "BOT--->  COVID BOT"
    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end':
        answer = 'BOT--->  Bye'

    else:
        i = 0
        j = 0
        for lines in doc:
            stats = lines[:-1]
            stats = stats.lower()
            stat = stats.replace(' ', '')
            i += 1
            if stat == chat:
                answer = "BOT-->"+doc[i]
                break
            else:
                j += 1

        if i == j:
            answer = "BOT--->  I don't understand.........please teach me ! "


    get_response(ii)


def get_response(ii):

    listbox.insert(ii,answer)
    ii+=1

    listbox.itemconfig(ii-1, {'fg': 'green'})

    if answer == 'Bye':
        root.destroy()



# Add commands to submenu


chatWindow = Text(root, bd=1, bg="white", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=2,y=2, height=385, width=370)
messageWindow = Text(root, bd=0, bg=c3,width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)
listbox=Listbox(root,width=66,height=20,font=20)
scrollbar = Scrollbar(listbox, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=3, height=385)
ii=0
Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12),command=lambda :submit(listbox.size()))
Button.place(x=6, y=400, height=88)
listbox.pack()
root.mainloop()