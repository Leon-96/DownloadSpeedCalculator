from tkinter import *

import webbrowser

from tkinter import ttk

new = 1
url = "https://www.fast.com"


def fastspeed():
    webbrowser.open(url, new=new)


root = Tk()
root.title("Download Time Calculator by leon")
root['bg'] = "lightgreen"
ico = PhotoImage(file="C:\\Users\\GoodBoy69\\Desktop\everything\\dtc v0.1 stuff\\dtcico.png")
root.iconphoto(False, ico)
root.resizable(width=False, height=False)

filename1 = PhotoImage(file="C:\\Users\\GoodBoy69\\Desktop\\everything\\dtc v0.1 stuff\\backgrd.gif")
background_label = Label(root, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.minsize(1366, 768)

Title = Label(root, text="DownloadTimeCalculator", font=("Allessa Personal Use", 40), bg="white", width=15,
              bd=10, relief=RAISED, )
Title.pack()

speedtest = Button(root, text="Click to Check Your Download Speed", bg="orchid", bd=8, width=40, height=1,
                   relief=RAISED,
                   fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=fastspeed)
speedtest.place(x=430, y=150)

a = DoubleVar()
a.set("")
b = DoubleVar()
b.set("")

ds1 = Label(text="Enter Your Download Speed: ", bg="cyan", bd=8, width=30, height=1, relief=RIDGE, fg="Black",
            font=("Bitter", 15, "bold"), anchor="w", justify=LEFT)
ds1.place(x=0, y=250)

ds2 = Entry(root, textvariable=a, bg="salmon", bd=8, width=20, relief=RIDGE, fg="Black",highlightcolor="khaki",
            font=("Bitter", 15, "bold"), justify=CENTER)
ds2.place(x=300, y=250)

ds3 = ttk.Combobox(root, width=25, font=("Helvetica", 22,))
ds3.place(x=580, y=250)
ds3['values'] = ['Kbps (Kilobits per second)', 'Mbps (Megabits per second)', 'Gbps (Gigabits per second)']
ds3.current(1)
ds3['state'] = 'readonly'

ds4 = Label(text="Enter File Size: ", bg="cyan", bd=8, width=30, height=1, relief=RIDGE, fg="Black",
            font=("Bitter", 15, "bold"), anchor="w", justify=LEFT)
ds4.place(x=0, y=320)

ds5 = Entry(root, textvariable=b, bg="salmon", bd=8, width=20, relief=RIDGE, fg="Black",
            font=("Bitter", 15, "bold"), justify=CENTER,highlightcolor="khaki",)
ds5.place(x=300, y=320)

ds6 = ttk.Combobox(root, font=("Helvetica", 22,))
ds6.place(x=580, y=320)
ds6['values'] = ['KB (Kilobyte)', 'MB (Megabyte)', 'GB (Gigabyte)']
ds6.current(2)
ds6['state'] = 'readonly'

c = DoubleVar()
d = DoubleVar()

d.set("")
bruh = "error"


def time_conversion():
    x = float(c.get())
    time = x
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    d.set((round(day), "Days", round(hour), "Hours", round(minutes), "Minutes", round(seconds), "Seconds"))

    if seconds < 0.1:
        d.set("Less Than A Second\ndamn its fast!!!!!!!!")


def downloadtimecalculation():
    if ds3.get() == "Kbps (Kilobits per second)":
        if ds6.get() == 'MB (Megabyte)':
            c.set((b.get() * 1024) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Kbps (Kilobits per second)":
        if ds6.get() == 'KB (Kilobyte)':
            c.set(b.get() / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Kbps (Kilobits per second)":
        if ds6.get() == "GB (Gigabyte)":
            c.set((b.get() * 1024) / (a.get() * 0.000125))
            time_conversion()

    if ds3.get() == "Mbps (Megabits per second)":
        if ds6.get() == "KB (Kilobyte)":
            c.set((b.get() * 1024) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Mbps (Megabits per second)":
        if ds6.get() == "GB (Gigabyte)":
            c.set((b.get() * 1024) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Mbps (Megabits per second)":
        if ds6.get() == "MB (Megabyte)":
            c.set((b.get()) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Gbps (Gigabits per second)":
        if ds6.get() == "MB (Megabyte)":
            c.set((b.get() * 0.001) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Gbps (Gigabits per second)":
        if ds6.get() == "KB (Kilobyte)":
            c.set((b.get() * 0.000001) / (a.get() * 0.125))
            time_conversion()

    if ds3.get() == "Gbps (Gigabits per second)":
        if ds6.get() == "GB (Gigabyte)":
            c.set((b.get()) / (a.get() * 0.125))
            time_conversion()

    ds8.place(x=155, y=500)


time_check = Button(root, text="Calculate Time", bg="orchid", bd=8, width=30, height=1, relief=RAISED,
                    fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                    command=downloadtimecalculation)

time_check.place(x=475, y=380)

ds7 = Label(text="The file will approximately take the following amount of time to download : ", bg="cyan", bd=8,
            height=1, relief=RAISED, fg="Black",
            font=("Bitter", 20), anchor="w", justify=LEFT)
ds7.place(x=155, y=450)

ds8 = Label(root, textvariable=d, font=("Exan", 20, "bold"), bg="salmon", fg="black", bd=8, anchor='w', relief=RAISED)

ds8.pack_forget()


ds9 = Label(root, text="Made by Leon (*^▽^*) ", font=("Book Antiqua", 15, "bold"), bg="black", fg="white", width=18)
ds9.place(x=580, y=740)


root.mainloop()
