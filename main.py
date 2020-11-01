
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import os

def writeToDB(a):
    global root, about1, about2, about3, budget, startDate, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButtonImg, section2Img, section2Label
    mydb = mysql.connector.connect(host='localhost',database='expenses',user='root',password='2000-2000')
    print(budgetText.get(), startDateText.get(), endDateText.get())

    mycursor = mydb.cursor()

    sql = "INSERT INTO account (amount, startDate, endDate) VALUES (%s, %s, %s)"
    val = (int(budgetText.get()), startDateText.get(), endDateText.get())
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    budgetText.delete(0, END)
    startDateText.delete(0, END)
    endDateText.delete(0, END)


def addExpense(a):
    global flag, root, about1, about2, about3, aboutSection3, budget, commentLabel, startDate, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButton2, confirmButtonImg, confirmButtonImg2, section2Img, section2Label
    mydb = mysql.connector.connect(host='localhost', database='expenses', user='root', password='2000-2000')
    print(budgetText.get(), startDateText.get(), endDateText.get("1.0"))

    mycursor = mydb.cursor()

    sql = "INSERT INTO new_table (amount, date, comment, clientID) VALUES (%s, %s, %s, %s)"
    val = (int(budgetText.get()), startDateText.get(), endDateText.get("1.0",END), 10)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    budgetText.delete(0, END)
    startDateText.delete(0, END)
    endDateText.delete("1.0",END)




def section2():
    # systemTransparent

    global flag, root, about1, about2, about3,imgBG, confirmButton2,  budget, startDate, commentLabel, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButtonImg, section2Img, section2Label

    about1.destroy()
    about2.destroy()
    pgName.destroy()


    entry = Label(root, text="Новый бюджет", foreground='#FAEBEF', background="#333D79", font=('Lobster', 48))
    entry.place(x=80, y=10, width=400, height=60)
    img5Label.destroy()

    menuItem1.config(state='normal')
    menuItem1.configure(highlightbackground='#ffcfdc')
    menuItem3.config(state='normal')
    menuItem3.configure(highlightbackground='#ffcfdc')
    menuItem4.config(state='normal')
    menuItem4.configure(highlightbackground='#ffcfdc')
    menuItem5.config(state='normal')
    menuItem5.configure(highlightbackground='#ffcfdc')

    menuItem2.config(state='disabled')
    menuItem2.configure(highlightbackground='#FF7B9E')

    about3 = Label(root, text="- Ну что, Босс, готовы изменить свой кошелек, не дожидаясь понедельника?", wraplength=530, bg="#333D79",anchor='n', foreground='#ffffff',  font=('Georgia', 22))
    about3.place(x=5, y = menuItemY + 95, width=530, height=60)


    section2Img = ImageTk.PhotoImage(Image.open("images/section-img-2.png"))
    section2Label = Label(root, image=section2Img, bg="#333D79")
    section2Label.bind("<Button-1>", hello)
    section2Label.place(x=270, y=menuItemY + 95 + 90 )



    budget = Label(root, text="Размер бюджета", wraplength=530, bg="#333D79",anchor='center', foreground='#ffffff',  font=('Lato', 16))
    budget.place(x=5, y = menuItemY + 95 + 100, width=230, height=35)

    startDate = Label(root, text="Дата начала отслеживания расходов", wraplength=220, bg="#333D79",anchor='center', foreground='#ffffff',  font=('Lato', 16))
    startDate.place(x=5, y = menuItemY + 95 + 170, width=230, height=35)

    endDate = Label(root, text="Дата окончания отслеживания расходов", wraplength=220, bg="#333D79",anchor='center', foreground='#ffffff',  font=('Lato', 16))
    endDate.place(x=5, y = menuItemY + 95 + 240, width=230, height=35)

    budgetText = Entry(root)
    budgetText.place(x=250, y = menuItemY + 95 + 100)

    startDateText = Entry(root)
    startDateText.place(x=250, y = menuItemY + 95 + 170)

    endDateText = Entry(root)
    endDateText.place(x=250, y=menuItemY + 95 + 240)


    confirmButtonImg = ImageTk.PhotoImage(Image.open("images/button1.png"))
    confirmButton = Label(root, image=confirmButtonImg, bg="systemTransparent")
    confirmButton.bind("<Button-1>", writeToDB)
    confirmButton.place(x=50, y=menuItemY + 95 + 305, )

    footer3 = Label(root, text="Сделано c заботой о Вас и вашем благополучии", wraplength=240, foreground='#FAEBEF',
                    anchor='nw', background="#333D79", font=('Lato', 18))
    footer3.place(x=300, y=620, width=250, height=60)

    root.mainloop()


def section3():
    global flag, root, about1, about2,commentLabel, about3, imgBG, budget, confirmButton2, startDate, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButtonImg, section2Img, section2Label


    pgName.destroy()

    entry = Label(root, text="Опять расходы ?", foreground='#FAEBEF', wraplength=370,background="#333D79", font=('Lobster', 48))
    entry.place(x=80, y=10, width=400, height=60)
    img5Label.destroy()
    about3.destroy()
    endDate.destroy()
    confirmButton.destroy()

    menuItem1.config(state='normal')
    menuItem1.configure(highlightbackground='#ffcfdc')
    menuItem2.config(state='normal')
    menuItem2.configure(highlightbackground='#ffcfdc')
    menuItem4.config(state='normal')
    menuItem4.configure(highlightbackground='#ffcfdc')
    menuItem5.config(state='normal')
    menuItem5.configure(highlightbackground='#ffcfdc')

    menuItem3.config(state='disabled')
    menuItem3.configure(highlightbackground='#FF7B9E')

    aboutSection3 = Label(root, text="- Кошелёк или жизнь? Жизнь! ( и полный кошелёк, конечно же!)",
                   wraplength=360, bg="#333D79", anchor='n', foreground='#ffffff', font=('Georgia', 22))
    aboutSection3.place(x=5, y=menuItemY + 95, width=360, height=60)

    section2Img = ImageTk.PhotoImage(Image.open("images/section-img-3.png"))
    section2Label = Label(root, image=section2Img, bg="#333D79")
    section2Label.bind("<Button-1>", hello)
    section2Label.place(x=350, y=menuItemY + 95 + 200)

    budget = Label(root, text="Сумма расходов", wraplength=530, bg="#333D79", anchor='center', foreground='#ffffff',
                   font=('Lato', 16))
    budget.place(x=5, y=menuItemY + 95 + 100, width=230, height=35)

    startDate = Label(root, text="Дата совершения покупки", wraplength=220, bg="#333D79", anchor='center',
                      foreground='#ffffff', font=('Lato', 16))
    startDate.place(x=5, y=menuItemY + 95 + 170, width=230, height=20)

    commentLabel = Label(root, text="Краткий комментарий о событии, побудившем растраты", wraplength=220, bg="#333D79", anchor='center',
                    foreground='#ffffff', font=('Lato', 16))
    commentLabel.place(x=5, y=menuItemY + 95 + 280, width=230, height=56)

    budgetText = Entry(root, font=('Lato', 14))
    budgetText.place(x=250, y=menuItemY + 95 + 100)

    startDateText = Entry(root, font=('Lato', 14))
    startDateText.place(x=250, y=menuItemY + 95 + 170)

    endDateText = Text(root,width=20, height=6, font=('Lato', 14))
    endDateText.place(x=250, y=menuItemY + 95 + 240)

    confirmButtonImg = ImageTk.PhotoImage(Image.open("images/button2.png"))
    confirmButton = Label(root, image=confirmButtonImg, bg="#333D79")
    confirmButton.bind("<Button-1>", addExpense)
    confirmButton.place(x=17, y=menuItemY + 95 + 360, )

    footer3 = Label(root, text="Сделано c заботой о Вас и вашем благополучии", wraplength=240, foreground='#FAEBEF',
                    anchor='nw', background="#333D79", font=('Lato', 18))
    footer3.place(x=300, y=620, width=250, height=60)

    root.mainloop()


def section4():
    global eflag, field3, root, about1, about2,commentLabel, about3, imgBG, budget, expense1, expense2, confirmButton2, startDate, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButtonImg, section2Img, section2Label
    pgName.destroy()

    entry = Label(root, text="История - это наше всё", foreground='#FAEBEF', wraplength=530,background="#333D79", anchor="nw", font=('Lobster', 48))
    entry.place(x=40, y=10, width=530, height=60)
    img5Label.destroy()
    about3.destroy()
    endDate.destroy()
    confirmButton.destroy()
    budgetText.destroy()
    startDateText.destroy()
    endDateText.destroy()

    menuItem1.config(state='normal')
    menuItem1.configure(highlightbackground='#ffcfdc')
    menuItem2.config(state='normal')
    menuItem2.configure(highlightbackground='#ffcfdc')
    menuItem3.config(state='normal')
    menuItem3.configure(highlightbackground='#ffcfdc')
    menuItem5.config(state='normal')
    menuItem5.configure(highlightbackground='#ffcfdc')

    menuItem4.config(state='disabled')
    menuItem4.configure(highlightbackground='#FF7B9E')

    aboutSection3 = Label(root, text="- Не говорите мне, каковы ваши жизненные приоритеты. Покажите, на что вы тратите деньги, и я сам расскажу вам о них",
                   wraplength=520, bg="#333D79", anchor='n', foreground='#ffffff', font=('Georgia', 22))
    aboutSection3.place(x=5, y=menuItemY + 95, width=520, height=85)

    section2Img = ImageTk.PhotoImage(Image.open("images/section-img-4.png"))
    section2Label = Label(root, image=section2Img, bg="#333D79")
    section2Label.bind("<Button-1>", hello)
    section2Label.place(x=360, y= 286)

    mydb = mysql.connector.connect(host='localhost', database='expenses', user='root', password='2000-2000')
    mycursor = mydb.cursor()


    sql = "select * from new_table where clientID=10"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(mycursor.rowcount, "record inserted.")
    print('RESULT',result)
    for i in result:
        print(i[0])
        print(i[1])
        print(i[2])
    print('rrrrrrrrr', result[1][2])

    budget = Label(root, text="• " + result[0][2].strftime("%Y/%m/%d") + " Вы потратили " + str(result[0][1]) +" руб. с формулировкой " + result[0][3] + "", wraplength=360, bg="#333D79", anchor='w', foreground='#ffffff',
                   font=('Lato', 18))
    budget.place(x=5, y=menuItemY + 95 + 100, width=360, height=60)

    startDate = Label(root, text="• " + result[1][2].strftime("%Y/%m/%d") + " Вы потратили " + str(result[1][1]) +" руб. с формулировкой " + result[1][3] + "", wraplength=360, bg="#333D79", anchor='w',
                      foreground='#ffffff', font=('Lato', 18))
    startDate.place(x=5, y=menuItemY + 95 + 170, width=360, height=80)




    endDate = Label(root, text="", wraplength=360, bg="#333D79", anchor='w',
                      foreground='#ffffff', font=('Lato', 18))
    endDate.place(x=5, y=menuItemY + 95 + 240, width=360, height=170)


    confirmButtonImg = ImageTk.PhotoImage(Image.open("images/button5.png"))
    confirmButton = Label(root, image=confirmButtonImg, bg="#333D79")


    confirmButton.place(x=17, y=menuItemY + 95 + 260, )

    footer3 = Label(root, text="Сделано c заботой о Вас и вашем благополучии", wraplength=240, foreground='#FAEBEF',
                    anchor='nw', background="#333D79", font=('Lato', 18))
    footer3.place(x=300, y=620, width=250, height=60)

    root.mainloop()


def section5():
    global eflag,  root, about1, about2,commentLabel, about3, imgBG, budget, expense1, expense2, confirmButton2, startDate, endDate, budgetText, startDateText, endDateText, confirmButton, confirmButtonImg, section2Img, section2Label
    pgName.destroy()

    entry = Label(root, text="“И” значит ИТОГИ", foreground='#FAEBEF', wraplength=530,background="#333D79", anchor="center", font=('Lobster', 48))
    entry.place(x=10, y=10, width=530, height=60)
    img5Label.destroy()
    about3.destroy()
    endDate.destroy()
    confirmButton.destroy()
    budgetText.destroy()
    startDateText.destroy()
    endDateText.destroy()
    budget.destroy()
    startDate.destroy()

    menuItem1.config(state='normal')
    menuItem1.configure(highlightbackground='#ffcfdc')
    menuItem2.config(state='normal')
    menuItem2.configure(highlightbackground='#ffcfdc')
    menuItem3.config(state='normal')
    menuItem3.configure(highlightbackground='#ffcfdc')
    menuItem4.config(state='normal')
    menuItem4.configure(highlightbackground='#ffcfdc')

    menuItem5.config(state='disabled')
    menuItem5.configure(highlightbackground='#FF7B9E')

    aboutSection3 = Label(root, text="- Неужели ничего не изменилось? Или нет, не так. Неужели мы так ничего и не изменили? Изменили! Посмотрите сами, Босс!",
                   wraplength=520, bg="#333D79", anchor='n', foreground='#ffffff', font=('Georgia', 22))
    aboutSection3.place(x=5, y=menuItemY + 95, width=520, height=85)

    section2Img = ImageTk.PhotoImage(Image.open("images/section-img-5.png"))
    section2Label = Label(root, image=section2Img, bg="#333D79")
    section2Label.bind("<Button-1>", hello)
    section2Label.place(x=360, y= 286)

    mydb = mysql.connector.connect(host='localhost', database='expenses', user='root', password='2000-2000')
    mycursor = mydb.cursor()

    sql = "select * from new_table where clientID=10"
    mycursor.execute(sql)
    result2 = mycursor.fetchall()
    print(mycursor.rowcount, "record inserted.")
    print(result2)
    totalExpenses = 0
    for i in result2:
        totalExpenses += i[1]
    print('rrrrrrrrr', result2[1][2])

    mydb = mysql.connector.connect(host='localhost', database='expenses', user='root', password='2000-2000')
    mycursor = mydb.cursor()

    sql = "select * from account where id='10'"

    mycursor.execute(sql)
    result = mycursor.fetchall()


    total1 = Label(root, text="• В период с " + result[0][2] + " по " + result[0][3] +" Вы совершили " + str(len(result2)) + " покупки", wraplength=360, bg="#333D79", anchor='w', foreground='#ffffff',
                   font=('Lato', 18))
    total1.place(x=5, y=menuItemY + 95 + 100, width=360, height=60)

    total2 = Label(root, text="• Стоимость всех покупок равна " + str(totalExpenses) + " рублей", wraplength=360, bg="#333D79", anchor='w',
                      foreground='#ffffff', font=('Lato', 18))
    total2.place(x=5, y=menuItemY + 95 + 170, width=360, height=60)

    total3 = Label(root, text="• В среднем Вы тратили " + str(round(totalExpenses/len(result2), 2)) + " рублей", wraplength=360, bg="#333D79", anchor='w',
                   foreground='#ffffff', font=('Lato', 18))
    total3.place(x=5, y=menuItemY + 95 + 225, width=360, height=60)

    total4 = Label(root, text="• У вас осталось " + str(result[0][1]) + " - " + str(totalExpenses) + " = " + str(result[0][1] -  totalExpenses) + " рублей" , wraplength=360, bg="#333D79", anchor='w',
                   foreground='#ffffff', font=('Lato', 18))
    total4.place(x=5, y=menuItemY + 95 + 285, width=360, height=60)

    total5 = Label(root, text="• Оставшийся процент денег равен " + str(round(((result[0][1] -  totalExpenses) * 100) / result[0][1], 2)) + "%" , wraplength=360, bg="#333D79", anchor='w',
                   foreground='#ffffff', font=('Lato', 18))
    total5.place(x=5, y=menuItemY + 95 + 345, width=360, height=60)

    footer = Label(root, text="© Finance Saver 2020", foreground='#FAEBEF', background="#333D79",
                   font=('Lobster 1.4', 24))
    footer.place(x=-5, y=620, width=240, height=30)

    footer3 = Label(root, text="Сделано c заботой о Вас и вашем благополучии", wraplength=240, foreground='#FAEBEF',
                    anchor='nw', background="#333D79", font=('Lato', 18))
    footer3.place(x=300, y=620, width=250, height=60)

    root.mainloop()

def hello(a):
    print("hello")



global totalExpenses, field3, total1, total2,total3,total4,total5, flag, root, about1, about2, about3, aboutSection3, budget, commentLabel, startDate, endDate,  budgetText,   startDateText,  endDateText, confirmButton, confirmButton2, confirmButtonImg, confirmButtonImg2, section2Img, section2Label
menuItemX = 0
menuItemY = 100
iconGap = 35
iconY = 100
flag = False

root = Tk()
root.configure(background="#333D79")
root.geometry("550x700+565+125")
root.title("Finance Saver")

entry = Label(root, text="Добро пожаловать в", foreground='#ffffff',background="#333D79",  font=('Lato', 36))
entry.place(x=80, y = 10, width=400, height=40)


pgName =  Label(root, text="Finance Saver", foreground='#FAEBEF', background="#333D79", font=('Lobster 1.4', 36))
pgName.place(x=80, y=50, width=400, height=40)

img1 = ImageTk.PhotoImage(Image.open("images/menu-icon-1.png"))
img2 = ImageTk.PhotoImage(Image.open("images/menu-icon-2.png"))
img3 = ImageTk.PhotoImage(Image.open("images/menu-icon-3.png"))
img4 = ImageTk.PhotoImage(Image.open("images/menu-icon-4.png"))
img5 = ImageTk.PhotoImage(Image.open("images/menu-icon-5.png"))

menuItem1 = Button(root, state='disabled', text='Главная\nформа', image=img1 , compound=TOP, bg='#000000', width='10', height='0', anchor='center', font=('Lato', 14), )
menuItem1.configure(highlightbackground='#FF7B9E')
menuItem1.place(x=menuItemX, y=menuItemY, width=110, height=70)
menuItemX += 110


menuItem2 = Button(root , text='Новый\nбюджет',image=img2 , compound=TOP, bg='#000000', width='10', height='0', anchor='center', font=('Lato', 14), command=section2)
menuItem2.configure(highlightbackground='#ffcfdc')
menuItem2.place(x=menuItemX, y=menuItemY, width=110, height=70)
menuItemX += 110

menuItem3 = Button(root, text='Новые\nрасходы',image=img3 , compound=TOP, bg='#000000', width='10', height='0', anchor='center', font=('Lato', 14), command=section3)
menuItem3.configure(highlightbackground='#ffcfdc')
menuItem3.place(x=menuItemX, y=menuItemY, width=110, height=70)
menuItemX += 110

menuItem4 = Button(root, text='История\nопераций',image=img4 , compound=TOP, bg='#000000', width='10', height='0', anchor='center', font=('Lato', 14), command=section4)
menuItem4.configure(highlightbackground='#ffcfdc')
menuItem4.place(x=menuItemX, y=menuItemY, width=110, height=70)
menuItemX += 110

menuItem5 = Button(root, text='Итоги',image=img5 , compound=TOP, bg='#000000', width='10', height='0', anchor=N, font=('Lato', 14), command=section5)
menuItem5.configure(highlightbackground='#ffcfdc')
menuItem5.place(x=menuItemX, y=menuItemY, width=110, height=70)
menuItemX += 110

about1 = Label(root, text="Finance Saver - тот самый инструмент, который поможет спасти Ваш кошелёк от трат на безделушки, а Вас - от головной боли при попытке подсчёта расходов.", wraplength=530, bg="#333D79",anchor='nw', foreground='#ffffff',  font=('Lato', 20))
about1.place(x=5, y = menuItemY + 95, width=530, height=70)

about2 = Label(root, text="Начните следить за своими расходами прямо сейчас, и уже завтра вы увидите: сколько лишних денег вы можете сэкономить и направить в лучшее русло", wraplength=240, bg="#333D79",anchor='w', foreground='#ffffff',  font=('Lato', 20))
about2.place(x=5, y = menuItemY + 95 + 100, width=240, height=200)


imgBG = ImageTk.PhotoImage(Image.open("images/section-img-1.png"))
img5Label = Label(root, image=imgBG, bg="#333D79")
img5Label.bind("<Button-1>", hello)
img5Label.place(x=260, y=menuItemY + 95 + 80, )



footer = Label(root, text="© Finance Saver 2020", foreground='#FAEBEF',background="#333D79",  font=('Lobster 1.4', 24))
footer.place(x=-5, y =  620, width=240, height=30)

footer2 = Label(root, text="Designed by Alexander Zharkov", foreground='#FAEBEF',background="#333D79",  font=('Lato', 18))
footer2.place(x=0, y = 650, width=280, height=40)

footer3 = Label(root, text="Сделано c заботой о Вас и вашем благополучии", wraplength=240, foreground='#FAEBEF', anchor='nw',background="#333D79",  font=('Lato', 18))
footer3.place(x=300, y = 620, width=250, height=60)

root.mainloop()
