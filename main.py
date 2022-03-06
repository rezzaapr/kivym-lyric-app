from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
Window.size=(300,600)

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


BoxLayout:
    HotReloadViewer:
        size_hint_x: .3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 1, 0, 1
        errors_background_color: app.theme_cls.bg_dark
'''


class Example(MDApp):
    path_to_kv_file = "main.kv"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    def getlirik(self):
        lirik = "Underneath the bridge\nTarp has sprung a leak\nAnd the animals I've trapped\nHave all become my pets\nAnd I'm living off of grass\nAnd the drippings from my ceiling\nIt's okay to eat fish\nCause they don't have any feelings\n\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmmUnderneath the bridge\nTarp has sprung a leak\nAnd the animals I've trapped\nHave all become my pets\nAnd I'm living off of grass\nAnd the drippings from my ceiling\nIt's okay to eat fish\nCause they don't have any feelings\n\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\n\nUnderneath the bridge\nTarp has sprung a leak\nAnd the animals I've trapped\nHave all become my pets\nAnd I'm living off of grass\nAnd the drippings from the ceiling\nIt's okay to eat fish\nCause they don't have any feelings\n\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\nSomething in the way\nMmm-mmm\nSomething in the way, yeah\nMmm-mmm\n\n\n"
        self.help_str.get_screen('lirik').ids.lirik.text = lirik

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


Example().run()