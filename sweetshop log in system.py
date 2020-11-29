from tkinter import*
import random
import time
import datetime
import tkinter.messagebox

def Ref():
    x = random.randint(1234, 434354)
    randomRef = str(x)
    rand.set(randomRef)

    CoG = float(galaxy.get())
    CoK = float(kinder.get())
    CoB = float(bounty.get())
    CoT = float(twix.get())

    Cost_Galaxy = CoG * 1.99
    Cost_Kinder = CoK * 1.49
    Cost_Bounty = CoB * 1.29
    Cost_Twix = CoT * 0.99

    cost_subtotal = "£", str('%.2f' % (Cost_Bounty + Cost_Galaxy + Cost_Kinder + Cost_Twix))
    cost_tax = "£", str('%.2f' % ((Cost_Bounty + Cost_Galaxy + Cost_Kinder + Cost_Twix) * 0.2))
    cost_total = "£", str('%.2f' % ((Cost_Bounty + Cost_Galaxy + Cost_Kinder + Cost_Twix) * 1.2))
   
    subtotal.set(cost_subtotal)
    vat.set(cost_tax)
    total.set(cost_total)

def Quit():
    root.destroy()

def Reset():
    rand.set("")
    galaxy.set("")
    kinder.set("")
    bounty.set("")
    twix.set("")
    total.set("")
    subtotal.set("")
    vat.set("")

root = Tk()
root.geometry("1600x800+0+0")
root.title("Sea Front Sweet & Candy Shop System")

Tops = Frame(root, width = 1600, height = 50, relief=SUNKEN)
Tops.pack(side=TOP)

Frame_1 = Frame(root, width = 800, height = 700, relief=SUNKEN)
Frame_1.pack(side=LEFT)

Frame_2 = Frame(root, width = 800, height = 700, relief=SUNKEN)
Frame_2.pack(side=RIGHT)

#---------------------------Time---------------------------

now = datetime.datetime.now()
localtime = time.asctime(time.localtime(time.time()))

#---------------------------Info---------------------------

lblInfo = Label(Tops, font = ('arial', 50, 'bold'), text = 'Sea Front Sweet & Candy Shop System', fg = 'navy', bd = 10, anchor = 'w')
lblInfo.grid(row = 0, column = 0)
lblInfo = Label(Tops, font = ('arial', 20, 'bold'), text = localtime, fg = 'navy', bd = 10, anchor = 'w')
lblInfo.grid(row = 1, column = 0)

#---------------------------Sweets---------------------------

rand = StringVar()
galaxy = StringVar()
kinder = StringVar()
bounty = StringVar()
twix = StringVar()
total = StringVar()
subtotal = StringVar()
vat = StringVar()

lblReference = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Reference', bd = 10, anchor = 'w')
lblReference.grid(row = 0, column = 0)
txtReference = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = rand, bd = 10, bg = 'light blue', justify = 'right')
txtReference.grid(row = 0, column = 1)

lblGalaxy = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Galaxy', bd = 10, anchor = 'w')
lblGalaxy.grid(row = 1, column = 0)
txtGalaxy = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = galaxy, bd = 10, bg = 'light blue', justify = 'right')
txtGalaxy.grid(row = 1, column = 1)

lblKinder = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Kinder', bd = 10, anchor = 'w')
lblKinder.grid(row = 2, column = 0)
txtKinder = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = kinder, bd = 10, bg = 'light blue', justify = 'right')
txtKinder.grid(row = 2, column = 1)

lblBounty = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Bounty', bd = 10, anchor = 'w')
lblBounty.grid(row = 4, column = 0)
txtBounty = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = bounty, bd = 10, bg = 'light blue', justify = 'right')
txtBounty.grid(row = 4, column = 1)

lblTwix = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Twix', bd = 10, anchor = 'w')
lblTwix.grid(row = 5, column = 0)
txtTwix = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = twix, bd = 10, bg = 'light blue', justify = 'right')
txtTwix.grid(row = 5, column = 1)

#--------------------Pricing------------------

lblSubtotal = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Subtotal', bd = 10, anchor = 'w')
lblSubtotal.grid(row = 1, column = 2)
txtSubtotal = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = subtotal, bd = 10, bg = '#ffffff', justify = 'right')
txtSubtotal.grid(row = 1, column = 3)

lblVat = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'VAT', bd = 10, anchor = 'w')
lblVat.grid(row = 2, column = 2)
txtVat = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = vat, bd = 10, bg = '#ffffff', justify = 'right')
txtVat.grid(row = 2, column = 3)

lblTotal = Label(Frame_1, font = ('arial', 16, 'bold'), text = 'Total', bd = 10, anchor = 'w')
lblTotal.grid(row = 4, column = 2)
txtTotal = Entry(Frame_1, font = ('arial', 16, 'bold'), textvariable = total, bd = 10, bg = '#ffffff', justify = 'right')
txtTotal.grid(row = 4, column = 3)

#-------------------Buttons------------------


btnTotal = Button(Frame_1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), text = 'Total', 
bg = 'light blue', command = Ref).grid(row = 8, column = 1)

btnReceipt = Button(Frame_1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), text = 'Receipt', 
bg = 'light blue').grid(row = 8, column = 2)

btnReset = Button(Frame_1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), text = 'Reset', 
bg = 'light blue', command = Reset).grid(row = 8, column = 3)

btnQuit = Button(Frame_1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), text = 'Quit', 
bg = 'light blue', command = Quit).grid(row = 8, column = 4)

#------------------------Receipt--------------------

txtReceipt_print = Text(Frame_2, bd = 7, bg = 'light blue', width = 50, font = ('arial', 16, 'bold'))
txtReceipt_print.place(width=1000, height=420)





root.mainloop()
