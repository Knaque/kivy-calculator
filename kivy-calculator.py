"""A little calculator app built in Python & Kivy."""

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class CalculatorScreen(Screen):
    """Main screen for calculator."""

    pass


class CalculatorApp(App):
    """Main app."""

    current_equation = StringProperty()

    def build(self):
        """Build app."""
        # Set window icon
        self.icon = 'graphics/window_icon.png'
        # Set window title
        self.title = 'Kivy Calculator'

        return CalculatorScreen()


if __name__ == '__main__':
    CalculatorApp().run()
