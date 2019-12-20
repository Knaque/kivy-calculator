"""A little calculator app built in Python & Kivy."""

try:
    from kivy.app import App
    from kivy.uix.screenmanager import Screen
    from kivy.properties import StringProperty
except ModuleNotFoundError:
    print("Kivy is not installed. Please run the following command:")
    print("sudo python3.7 -m pip install kivy")
    quit()


class CalculatorScreen(Screen):
    """Main screen for calculator."""

    def calculate(self):
        """Calculate the result."""
        try:
            self.app = App.get_running_app()
            self.app.current_equation = str(eval(self.app.current_equation))
        except SyntaxError:
            self.app = App.get_running_app()
            self.app.current_equation = "Error"
        except NameError:
            self.app = App.get_running_app()
            self.app.current_equation = "Error"
        except ZeroDivisionError:
            self.app = App.get_running_app()
            self.app.current_equation = "Error"


class CalculatorApp(App):
    """Main app."""

    current_equation = StringProperty("")

    def build(self):
        """Build app."""
        # Set window icon
        self.icon = 'graphics/window_icon.png'
        # Set window title
        self.title = 'Kivy Calculator'

        return CalculatorScreen()


if __name__ == '__main__':
    CalculatorApp().run()
