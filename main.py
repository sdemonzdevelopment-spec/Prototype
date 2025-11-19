from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

# ---------------------------------------------------------
# 1. THE SCRIPT (Your Game Data)
# ---------------------------------------------------------
# This replaces your old 'script.rpy' file.
# We use "cmd" to tell the engine what to do.
SCRIPT = [
    # Scene 1: Intro
    {"cmd": "scene", "src": "images/ruinedcity.png"},
    {"cmd": "music", "src": "audio/ambience.ogg"},
    {"cmd": "show", "src": "images/jackneutral.png", "pos": "center"},
    
    {"cmd": "say", "who": "Jack", "text": "Welcome to the DemonZ Prototype."},
    {"cmd": "show", "src": "images/jacksmirk.png", "pos": "center"},
    {"cmd": "say", "who": "Jack", "text": "If you are seeing this, the Kivy Engine is working."},
    
    {"cmd": "hide"},
    {"cmd": "show", "src": "images/eveneutral.png", "pos": "center"},
    {"cmd": "say", "who": "Eve", "text": "Are we running on Android right now?"},
    
    # Choice Menu
    {"cmd": "choice", "options": [
        {"text": "Yes, this is an APK.", "jump": 11}, # Jumps to index 11
        {"text": "No, this is a PC test.", "jump": 13} # Jumps to index 13
    ]},

    # Path A (Index 11)
    {"cmd": "show", "src": "images/evesmirk.png", "pos": "center"},
    {"cmd": "say", "who": "Eve", "text": "Excellent. The extraction can begin."},
    {"cmd": "end", "text": "ENDING A: Mobile Success"},

    # Path B (Index 13)
    {"cmd": "show", "src": "images/eveneutral.png", "pos": "center"},
    {"cmd": "say", "who": "Eve", "text": "Oh... well, upload it to GitHub soon."},
    {"cmd": "end", "text": "ENDING B: PC Testing"}
]

# ---------------------------------------------------------
# 2. THE ENGINE (The Kivy Code)
# ---------------------------------------------------------
class DemonZGame(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.typing_event = None
        self.display_text = ""
        self.target_text = ""
        self.current_music = None

        # -- LAYER 1: Background --
        self.bg = Image(source='', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        # -- LAYER 2: Character Sprite --
        # We center it horizontally (x=0.3 means start at 30%, width is 40%)
        self.sprite = Image(source='', size_hint=(0.4, 0.85), pos_hint={'x': 0.3, 'y': 0})
        self.sprite.opacity = 0
        self.add_widget(self.sprite)

        # -- LAYER 3: Text Box --
        # We use your custom textbox.png
        self.textbox = Image(
            source='images/textbox.png',
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(1, 0.35),
            allow_stretch=True, keep_ratio=False
        )
        self.add_widget(self.textbox)

        # Invisible button to handle clicking "Next"
        self.click_area = Button(
            background_color=(0,0,0,0),
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(1, 0.35),
            on_press=self.on_tap
        )
        self.add_widget(self.click_area)

        # -- LAYER 4: UI Text --
        self.name_lbl = Label(
            text="", font_size='24sp', bold=True,
            pos_hint={'x': 0.15, 'y': 0.24}, size_hint=(0.3, 0.05),
            color=(1, 0.2, 0.2, 1), halign='left' # Demon Red Color
        )
        self.add_widget(self.name_lbl)

        self.text_lbl = Label(
            text="Tap to start...", font_size='20sp',
            pos_hint={'x': 0.18, 'y': 0.08}, size_hint=(0.64, 0.15),
            halign='left', valign='top'
        )
        self.text_lbl.bind(size=self.text_lbl.setter('text_size'))
        self.add_widget(self.text_lbl)

        # -- LAYER 5: Choices --
        self.choice_layout = FloatLayout()
        self.add_widget(self.choice_layout)

        # Start the Engine
        self.process()

    def process(self):
        """Reads the current line of SCRIPT and executes it"""
        if self.index >= len(SCRIPT): return
        line = SCRIPT[self.index]
        cmd = line['cmd']

        if cmd == "scene":
            self.bg.source = line['src']
            self.next_line()

        elif cmd == "music":
            if self.current_music: self.current_music.stop()
            try:
                self.current_music = SoundLoader.load(line['src'])
                if self.current_music:
                    self.current_music.loop = True
                    self.current_music.play()
            except: print("Audio Error")
            self.next_line()

        elif cmd == "show":
            self.sprite.source = line['src']
            self.sprite.opacity = 1
            self.next_line()

        elif cmd == "hide":
            self.sprite.opacity = 0
            self.next_line()

        elif cmd == "say":
            self.name_lbl.text = line['who']
            self.target_text = line['text']
            self.display_text = ""
            self.typing_event = Clock.schedule_interval(self.type_text, 0.03)

        elif cmd == "choice":
            self.click_area.disabled = True
            self.show_choices(line['options'])

        elif cmd == "end":
            self.text_lbl.text = line['text']
            self.click_area.disabled = True

    def next_line(self):
        self.index += 1
        self.process()

    def type_text(self, dt):
        if len(self.display_text) < len(self.target_text):
            self.display_text += self.target_text[len(self.display_text)]
            self.text_lbl.text = self.display_text
        else:
            Clock.unschedule(self.typing_event)
            self.typing_event = None

    def on_tap(self, instance):
        if self.typing_event:
            Clock.unschedule(self.typing_event)
            self.typing_event = None
            self.text_lbl.text = self.target_text
        else:
            self.next_line()

    def show_choices(self, options):
        y = 0.6
        for opt in options:
            btn = Button(
                text=opt['text'],
                size_hint=(0.6, 0.12),
                pos_hint={'center_x': 0.5, 'center_y': y},
                background_color=(0.3, 0, 0, 1), font_size='20sp'
            )
            btn.bind(on_release=lambda x, j=opt['jump']: self.make_choice(j))
            self.choice_layout.add_widget(btn)
            y -= 0.14

    def make_choice(self, jump_index):
        self.choice_layout.clear_widgets()
        self.click_area.disabled = False
        self.index = jump_index
        self.process()

class DemonZApp(App):
    def build(self):
        return DemonZGame()

if __name__ == '__main__':
    DemonZApp().run()