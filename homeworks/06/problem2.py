from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def on_down(self):
        pass

    @abstractmethod
    def on_up(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def on_change(self):
        pass


class WinButton(Button):

    def on_down(self):
        return 'Win button is pressed'

    def on_up(self):
        return 'Win button is pressed'

    def draw(self):
        return 'Win button drawing...'


class MacButton(Button):

    def on_down(self):
        return 'Mac button is pressed'

    def on_up(self):
        return 'Mac button is pressed'

    def draw(self):
        return 'Mac button drawing...'


class WinCheckbox(Checkbox):

    def on_change(self):
        return 'Win checkbox changed'


class MacCheckbox(Checkbox):

    def on_change(self):
        return 'Mac checkbox changed'


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):

    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:

    def __init__(self, f):
        self.factory = f

    def createUI(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        draw1 = self.button.draw()
        change = self.checkbox.on_change()
        draw2 = self.button.draw()

        return [draw1, change, draw2]


winApp = Application(WinFactory())
winApp.createUI()

macApp = Application(MacFactory())
macApp.createUI()

print(winApp.paint())
print(macApp.paint())
