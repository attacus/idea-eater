"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os
import pathlib

class IdeaEater(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        idea_label = toga.Label(
            'Thought goes here: ',
            style=Pack(padding=(0, 5))
        )
        self.idea_input = toga.TextInput(style=Pack(flex=1))

        idea_box = toga.Box(style=Pack(direction=ROW, padding=5))
        idea_box.add(idea_label)
        idea_box.add(self.idea_input)

        button = toga.Button(
            'Nom',
            on_press=self.eat_idea,
            style=Pack(padding=5)
        )

        self.last_idea_label = toga.Label(
            'Last idea eaten: NONE',
            style=Pack(padding=(0, 5))
        )

        monster_image = toga.images.Image("resources/idea_monster_frand.png")
        monster_image_view = toga.ImageView(id='monster_image', image=monster_image)

        main_box.add(idea_box)
        main_box.add(button)
        main_box.add(self.last_idea_label)
        main_box.add(monster_image_view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def eat_idea(self, widget):
        with open(os.path.join(pathlib.Path.home(), 'ideas.txt'), 'a') as f:
            f.write(self.idea_input.value + '\n')

        self.last_idea_label.text = 'Last idea eaten: ' + self.idea_input.value

        self.idea_input.clear()
        self.idea_input.focus()

def main():
    return IdeaEater()
