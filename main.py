from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

LOT_LIST = [0.01, 0.01, 0.02, 0.02, 0.04, 0.04, 0.08, 0.08, 0.16, 0.16, 0.32, 0.32, 0.64, 0.64, 1.28, 2.56, 5.12]

class GridTradingAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        self.is_running = False

        self.add_widget(Label(text="Grid Trading Bot", font_size=26, bold=True, size_hint_y=0.12))

        self.add_widget(Label(text="Symbol Name:", font_size=16, size_hint_y=0.06))
        self.inp_symbol = TextInput(text="USTEC", multiline=False, font_size=20, size_hint_y=0.1, halign='center')
        self.add_widget(self.inp_symbol)

        self.add_widget(Label(text="Target Profit ($):", font_size=16, size_hint_y=0.06))
        self.inp_profit = TextInput(text="15.0", multiline=False, font_size=20, size_hint_y=0.1, halign='center')
        self.add_widget(self.inp_profit)

        self.lbl_status = Label(text="Status: STOPPED", font_size=20, bold=True, color=(1, 0, 0, 1), size_hint_y=0.12)
        self.add_widget(self.lbl_status)

        self.btn_start = Button(text="START TRADING", background_color=(0, 0.8, 0, 1), font_size=20, bold=True, size_hint_y=0.22)
        self.btn_start.bind(on_press=self.start_bot)
        self.add_widget(self.btn_start)

        self.btn_stop = Button(text="STOP & CLOSE ALL", background_color=(0.8, 0, 0, 1), font_size=20, bold=True, size_hint_y=0.22)
        self.btn_stop.bind(on_press=self.stop_bot)
        self.add_widget(self.btn_stop)

    def start_bot(self, instance):
        self.is_running = True
        self.lbl_status.text = "Status: RUNNING..."
        self.lbl_status.color = (0, 1, 0, 1)

    def stop_bot(self, instance):
        self.is_running = False
        self.lbl_status.text = "Status: STOPPED"
        self.lbl_status.color = (1, 0, 0, 1)

class GridTradingApp(App):
    def build(self):
        return GridTradingAppLayout()

if __name__ == '__main__':
    GridTradingApp().run()
