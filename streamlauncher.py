# import the library
from appJar import gui
import webbrowser

class streamlauncher():

    def press(self, button):
        if button == "Cancel":
            self.app.infoBox("No cancel", "Nope, you're gonna watch James stream no matter what.")
            webbrowser.open('https://www.twitch.tv/jamesharris9119/')
        else:
            webbrowser.open('https://www.twitch.tv/jamesharris9119/')


    def Prepare(self, app):
        app.setTitle("James' Stream Launcer Console")
        app.addLabel("title", "Welcome to James' Stream Launcher Console")
        app.setLabelBg("title", "white")
        app.addButtons(["Launch Stream!", "Cancel"], self.press)
        app.addLabel("18", "James for GDC!")

        #app.startLabelFrame("James for GDC!", 0, 20)
        #app.addImage("James for GDC!", "gamerjames-burned.gif")
        #app.stopLabelFrame()

        return app

    def Start(self):
        app = gui()

        app = self.Prepare(app)

        self.app = app

        app.go()


if __name__ == '__main__':

    App = streamlauncher()

    App.Start()