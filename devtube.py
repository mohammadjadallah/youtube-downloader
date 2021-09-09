# call tkinter and install pytube then call it too
# go to terminal and write --> pip install pytube

from tkinter import *
from tkinter import ttk
from pytube import *

# make window and what is the size you want and title, icon
root = Tk()
root.geometry("800x600")
root.resizable(0, 0)
root.title('                                                                                                      '
'DevTube downloader')

icon = PhotoImage(file=r'C:\Users\mhmdj\PycharmProjects\youtubeDownloader\devtube1.png')
root.iconphoto(False, icon)
root.configure(bg='#462c5a')


# Here function to bring information about the video

def infoVideo():
    link = str(entry.get())
    tit = YouTube(link).title
    vi = YouTube(link).views
    Len = YouTube(link).length
    rt = YouTube(link).rating


    Title = Label(root, text=' title: ' + tit, font=('PGothic', 18, 'bold'), fg='#c9c5c0', bg='#462c5a')
    Title.place(x=83, y=420)
    views = Label(root, text=' views: ' + str(vi), font=('PGothic', 18, 'bold'), fg='#c9c5c0', bg='#462c5a')
    views.place(x=83, y=450)
    length = Label(root, text=' length: ' + str(Len) + ' sec', font=('PGothic', 18, 'bold'), fg='#c9c5c0', bg='#462c5a')
    length.place(x=83, y=480)
    rate = Label(root, text=' rating: ' + str(rt), font=('PGothic', 18, 'bold'), fg='#c9c5c0', bg='#462c5a')
    rate.place(x=83, y=510)

# and this function to check if the quality equivalent what the user choose

def choose():
    Get = typeOfQuality.get()
    link = str(entry.get())

    if Get == '1080p':
        video = YouTube(link).streams.get_highest_resolution()
        video.download(r'C:\Users\mhmdj\Downloads')
    elif Get == '720p':
        video = YouTube(link).streams.filter(file_extension='mp4').get_by_itag('22')  # 22 = 720p
        video.download(r'C:\Users\mhmdj\Downloads')  # https://youtu.be/AkbdjoBa9bQ
    elif Get == '480p':
        video = YouTube(link).streams.filter(file_extension='mp4').get_by_itag('135')  # 135 = 480p
        video.download(r'C:\Users\mhmdj\Downloads')
    elif Get == '360p':
        video = YouTube(link).streams.filter(file_extension='mp4').get_by_itag('18')  # 18 = 360p
        video.download(r'C:\Users\mhmdj\Downloads')
    elif Get == 'get audio only':
        video = YouTube(link).streams.get_audio_only()
        video.download(r'C:\Users\mhmdj\Downloads')


# the function here to make text inside entry and when press on entry the text will gone
def placeholder(event):
    if entry.get() == '                          أدخـــــــــــل    الــــــرابــــط':
        entry.delete(0, END)
        usercheck = True


STR = StringVar()
usercheck = False


# make label to show text in window

label = Label(root,
              text='DevTube الآن يمكنك تنزيل وحفظ الفيديوهات وبأعلى جودة مع ',
              font=('PGothic', 23, 'bold'), fg='#c9c5c0', bg='#462c5a')
label.place(x=83, y=100)

# make entry until the user input the link

entry = Entry(root, bg='#2c2f30', font=('normal', 18), fg='#c9c5c0', relief=FLAT, textvariable=STR)
entry.place(width=665, height=70, x=85, y=160)
entry.insert(0, '                          أدخـــــــــــل    الــــــرابــــط')

# make button when user press it the video will download

btn = Button(root, text='تنزيل', font=('normal', 30), bg='#d1480d', fg='#c9c5c0', relief=FLAT)
btn.place(width=100, height=60, x=648, y=165)

btn2 = Button(root, text='عرض معلومات الفيديو', font=('normal', 18), bg='#d1480d', fg='#c9c5c0', relief=FLAT)
btn2.place(width=190, height=60, x=555, y=340)

typeOfQuality = ttk.Combobox(root, font=('normal', 20), values=('1080p', '720p',
                                                                    '480p', '360p',
                                                                    'get audio only'))
typeOfQuality.place(width=660, height=60, x=85, y=250)

btn.configure(command=lambda: root.after(2000, choose))
btn2.configure(command=lambda: root.after(2000, infoVideo))
entry.bind('<Button>', placeholder)



root.mainloop()
