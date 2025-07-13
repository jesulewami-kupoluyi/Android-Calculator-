from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from math import sqrt

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Display label
        self.label = Label(text='Welcome! Click buttons to start calculating.', font_size=30, size_hint=(1, 0.2))
        self.add_widget(self.label)

        # History list
        self.history = []

        # Button grid
        button_layout = GridLayout(cols=4, size_hint=(1, 0.8))
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            '√', '%', '⌫', 'H',
            'C'
        ]
        
        for text in buttons:
            btn = Button(
                text=text,
                font_size=50,
                background_color=(0, 0, 1, 1),  # Blue background
                color=(1, 1, 1, 1)              # White text
            )
            btn.bind(on_press=self.on_button_press)
            button_layout.add_widget(btn)

        self.add_widget(button_layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == '=':
            try:
                expression = self.label.text
                result = str(eval(expression))
                self.history.append(f"{expression} = {result}")
                self.label.text = result
            except:
                self.label.text = 'Error'
        elif text == '⌫':
            self.label.text = self.label.text[:-1]
        elif text == 'C':
            self.label.text = ''
        elif text == 'H':
            self.label.text = '\n'.join(self.history[-3:]) if self.history else 'No history'
        elif text == '√':
            try:
                value = float(self.label.text)
                result = str(sqrt(value))
                self.history.append(f"√({value}) = {result}")
                self.label.text = result
            except:
                self.label.text = 'Error'
        elif text == '%':
            try:
                value = float(self.label.text)
                result = str(value / 100)
                self.history.append(f"{value}% = {result}")
                self.label.text = result
            except:
                self.label.text = 'Error'
        else:
            # Append number or operator to current text
            if self.label.text in ['Welcome! Click buttons to start calculating.', 'Error', 'No history']:
                self.label.text = text
            else:
                self.label.text += text

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
