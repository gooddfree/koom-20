from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcLayout(BoxLayout):
    def press(self, key):
        display = self.ids.display
        if key == 'C':
            display.text = ''
        elif key == '=':
            try:
                # احسب التعبير باستخدام eval بعد تنظيفه
                expr = display.text
                # حماية بسيطة: اسمح فقط للأرقام والعمليات الشائعة
                allowed = "0123456789+-*/(). "
                if all(ch in allowed for ch in expr):
                    result = str(eval(expr))
                else:
                    result = "ERROR"
                display.text = result
            except Exception:
                display.text = "ERROR"
        else:
            display.text += key

class CalcApp(App):
    def build(self):
        return CalcLayout()

if __name__ == '__main__':
    CalcApp().run()
