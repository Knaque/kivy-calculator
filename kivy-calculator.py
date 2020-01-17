#!/usr/bin/env python3.7
"""A little calculator app built in Python & Kivy."""

try:
    from kivy import Config
    Config.set('graphics', 'minimum_width', '250')
    Config.set('graphics', 'minimum_height', '350')

    from kivy.app import App
    from kivy.uix.screenmanager import Screen
    from kivy.properties import StringProperty
except ModuleNotFoundError:
    print("Kivy is not installed. Please run the following command:")
    print("sudo python3.7 -m pip install kivy")
    quit()


class CalculatorScreen(Screen):
    """Main screen for calculator."""

    def type_check(self):
        """Check the current string when adding a new character."""
        self.app = App.get_running_app()

        if self.app.current_equation == "Error":
            self.app.current_equation = self.app.last_character
        else:
            self.app.current_equation = (self.app.current_equation
                                         + self.app.last_character)

    def calculate(self):
        """Calculate the result."""
        self.app = App.get_running_app()
        try:
            self.app.current_equation = str(eval(self.app.current_equation))
        except SyntaxError:
            self.app.current_equation = "Error"
        except NameError:
            self.app.current_equation = "Error"
        except ZeroDivisionError:
            self.app.current_equation = "Error"


class CalculatorApp(App):
    """Main app."""

    last_character = StringProperty("")
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
