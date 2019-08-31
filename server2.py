from tkinter import *
import socket
class Gui:
    def __init__(self,master):
        self.f1 = Frame(master)
        self.t1 = Text(self.f1,font=("times new roman",13,"bold"),width=73,height=20,borderwidth=6,relief=GROOVE)
        self.t1.grid(row=0,column=0)
        self.f1.grid(row=0,column=0,padx=10,pady=6)
        self.f2 = Frame(master)
        self.l1 = Label(self.f2, text="Message",bg="lightblue",font="Arial 10 bold")
        self.l1.grid(row=0,column=0)
        self.msg=StringVar()
        self.e1 = Entry(self.f2,textvariable=self.msg)
        self.e1.grid(row=0,column=1,ipadx=100,ipady=10,padx=9,pady=9)
        self.b1 = Button(self.f2, text="Send",width=8,padx=8,pady=5,bg="blue",fg="white",font=("Arial",10,"bold"),command=self.message)
        self.b2 = Button(self.f2, text="Receive",width=8,padx=8,pady=5,bg="blue",fg="white",font=("Arial",10,"bold"),command=self.receive)
        self.b2.grid(row=1,column=2)
        master.bind("<Return>",self.message)
        self.b1.grid(row=0,column=2,sticky=W)
        self.f2.config(bg="lightblue")
        self.f2.grid(row=1,column=0)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host= socket.gethostbyname(socket.gethostname())
        port = 9999
        self.server_socket.bind((host,port))
        self.server_socket.listen()
        self.client_socket, client_addr = self.server_socket.accept()
    def receive(self,event=None):
        cmsg = self.client_socket.recv(1024)
        self.t1.insert(END, "Client : {} \n".format(cmsg.decode()))
    def message(self,event=None):
        smsg = self.e1.get()
        self.client_socket.send(smsg.encode())
        self.t1.insert(END, "You : {} \n".format(smsg))
        self.msg.set("")
root = Tk()
b1 = Gui(root)
root.title("Server")
root.iconbitmap("msg.ico")
root.config(bg="lightblue")
root.resizable(0,0)
root.mainloop()
