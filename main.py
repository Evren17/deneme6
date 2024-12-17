from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
class LoginScreen(Screen):
    pass
class IconButton(ButtonBehavior, Image):
    pass    



class Slope(MDApp):
    BPoppins = "app\ifont\poppins_bold.ttf"
    IPoppins = "app\ifont\Poppins-Italic.ttf"

    logo_image = "app\image\PickFlick.png"  
    face_icon = "app\image\iface.png"
    insta_icon = "app\image\insta.png"
    google_icon =  "app\image\google.png"
       
    def build(self):
        Builder.load_file("app\iscreen\login.kv") 


        sm= ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.current = 'login'
        return sm


if __name__ =="__main__":
    Slope().run()
    