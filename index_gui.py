
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

import os.path as op
import argparse
import ujson
# import catconv.operations as co
# import catconv.stabi as sb

parser = argparse.ArgumentParser()
parser.add_argument("json_path")
args = parser.parse_args()


with open(args.json_path, 'rb') as jfile:
    catalog = ujson.load(jfile)

page_dict = { page['path']: page for page in catalog['pages'] }

class CardWidget(Widget):
    def test():
        return 'test'

class Indexer(App):
    def build(self):
        parent = Widget()
        self.painter = CardWidget()
        parent.add_widget(self.painter)
        return parent


if __name__ == '__main__':
    Indexer().run()

from tkinter import *
from PIL import ImageTk, Image
import os


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

for page in catalog['pages'][0:1]:
    path = op.join(catalog['path'], page['path'])
    for line in page['lines']:
        line_path = op.join(path, line['name'] + '.bin.png')

        img = ImageTk.PhotoImage(Image.open(line_path))

panel = Label(root, image =img)
panel.pack(side = "bottom", fill ="both", expand ="yes")
