from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = Label(text="0", font_size=40, size_hint_y=0.3, halign='right')
        main_layout.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for button_text in row:
                button = Button(text=button_text, font_size=30)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        return main_layout
    
    def on_button_press(self, instance):
        text = instance.text
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif text == 'C':
            self.expression = ""
        else:
            if self.expression == "0" or self.expression == "Error":
                self.expression = ""
            self.expression += text
        self.display.text = self.expression if self.expression else "0"

if __name__ == '__main__':
    CalculatorApp().run()