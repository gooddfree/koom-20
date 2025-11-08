from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TriangleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title Label
        title_label = Label(text="حساب مساحة المثلث", font_size='24sp')
        layout.add_widget(title_label)

        # Base Input
        self.base_input = TextInput(hint_text="أدخل طول القاعدة", input_type='number', multiline=False)
        layout.add_widget(self.base_input)

        # Height Input
        self.height_input = TextInput(hint_text="أدخل الارتفاع", input_type='number', multiline=False)
        layout.add_widget(self.height_input)

        # Calculate Button
        calculate_button = Button(text="احسب المساحة")
        calculate_button.bind(on_press=self.calculate_area)
        layout.add_widget(calculate_button)

        # Result Label
        self.result_label = Label(text="", font_size='20sp')
        layout.add_widget(self.result_label)

        return layout

    def calculate_area(self, instance):
        try:
            base = float(self.base_input.text)
            height = float(self.height_input.text)
            area = 0.5 * base * height
            self.result_label.text = f"مساحة المثلث: {area}"
        except ValueError:
            self.result_label.text = "الرجاء إدخال أرقام صحيحة!"


if __name__ == "__main__":
    TriangleApp().run()
