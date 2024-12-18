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
    BPoppins = "app\poppins_bold.ttf"
    IPoppins = "app\Poppins-Italic.ttf"

    logo_image = "app\PickFlick.png"  
    face_icon = "app\iface.png"
    insta_icon = "app\insta.png"
    google_icon =  "app\google.png"
       
    def build(self):
        Builder.load_file("login.kv") 


        sm= ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.current = 'login'
        return sm


if __name__ =="__main__":
    Slope().run()
    
