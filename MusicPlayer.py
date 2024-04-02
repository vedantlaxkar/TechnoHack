from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

# Initializing the mixer
mixer.init()

# Function to check if a file is a music file
def is_music_file(filename):
    music_extensions = ['.mp3', '.wav', '.ogg', '.flac']
    return any(filename.endswith(ext) for ext in music_extensions)

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    folder_path = filedialog.askdirectory(title='Open a songs directory')

    if folder_path:
        os.chdir(folder_path)

        tracks = [track for track in os.listdir() if is_music_file(track)]

        for track in tracks:
            listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

def play_next(song_name: StringVar, songs_list: Listbox, status: StringVar):
    next_index = (songs_list.curselection()[0] + 1) % songs_list.size()
    songs_list.select_clear(0, END)
    songs_list.activate(next_index)
    songs_list.selection_set(next_index)
    play_song(song_name, songs_list, status)

def play_previous(song_name: StringVar, songs_list: Listbox, status: StringVar):
    previous_index = (songs_list.curselection()[0] - 1) % songs_list.size()
    songs_list.select_clear(0, END)
    songs_list.activate(previous_index)
    songs_list.selection_set(previous_index)
    play_song(song_name, songs_list, status)

# Creating the master GUI
root = Tk()
root.geometry('800x600')    
root.title('Music Player')
root.configure(background="gray15")
root.resizable(0, 0)

# All the frames
button_frame = Frame(root, bg='gray30', width=600, height=100)
button_frame.place(y=500, x=100)

listbox_frame = Frame(root, bg='gray30')
listbox_frame.place(x=10, y=50, height=400, width=780)

# All StringVar variables
current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

# Playlist ListBox
playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='gray50', bg='gray15', fg='white')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5, expand=True)

# SongFrame Labels
Label(root, text='CURRENTLY PLAYING:', bg='gray15', font=('Times', 10, 'bold'), fg='white').place(x=10, y=10)

song_lbl = Label(root, textvariable=current_song, bg='gray15', font=("Times", 12), width=50, fg='white')
song_lbl.place(x=150, y=10)

# Buttons in the main screen
pause_btn = Button(button_frame, text='⏸', bg='red3', font=("Georgia", 13), width=7,
                    command=lambda: pause_song(song_status), fg='white')
pause_btn.place(x=50, y=10)

play_btn = Button(button_frame, text='▶', bg='green3', font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, song_status), fg='white')
play_btn.place(x=150, y=10)

resume_btn = Button(button_frame, text='⏵', bg='blue3', font=("Georgia", 13), width=7,
                    command=lambda: resume_song(song_status), fg='white')
resume_btn.place(x=250,y=10)

previous_btn = Button(button_frame, text='⏮', bg='gray', font=("Georgia", 13), width=7,
                      command=lambda: play_previous(current_song, playlist, song_status), fg='white')
previous_btn.place(x=350, y=10)

next_btn = Button(button_frame, text='⏭', bg='gray', font=("Georgia", 13), width=7,
                  command=lambda: play_next(current_song, playlist, song_status), fg='white')
next_btn.place(x=450, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='gold3', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist), fg='black')
load_btn.place(x=125, y=48)

# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg='gray15', font=('Times', 9), justify=LEFT, fg='white').pack(side=BOTTOM, fill=X)

# Finalizing the GUI
root.update()
root.mainloop()
