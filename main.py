from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()

'''

def askFor():
	typeDen = ["Billete","Billete","Billete","Billete","Billete","Billete","Moneda","Moneda","Moneda","Moneda","Moneda","Moneda","Moneda","Moneda"]
	den = [1000,500,200,100,50,20,20,10,5,2,1,0.5,0.2,0.1]
	cuant=[]
	multi=[]
	for t,d in zip(typeDen,den):
		num = raw_input ("{0}s de {1}: ".format(t,d))
		if num=="":
			num = 0
		else:
			num = int(num)
		cuant.append(num)
		multi.append(num*d)

	for c,m,l,d in zip(cuant,multi,den,typeDen):
		print ("Hay {0}  {3}s de {2}, sumando {1}: ".format(c,m,l,d))

askFor()
'''