from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label


class MixinMenu(object):
    
    def to_cadastrar(self):
        self.parent.parent.current = 'cadastrar'
        self.parent.parent.transition.direction = 'up'
    
    def to_buscar(self):
        self.parent.parent.current = 'buscar'
        self.parent.parent.transition.direction = 'left'
    
    def to_devedores(self):
        self.parent.parent.current = 'todos_devedores'
        self.parent.parent.transition.direction = 'down'
    
    def to_dividas(self):
        self.parent.parent.current = 'total_dividas'
        self.parent.parent.transition.direction = 'right'
    
    def to_diminuir(self):
        self.parent.parent.current = 'diminuir_divida'
        self.parent.parent.transition.direction = 'down'
    
    def to_excluir(self):
        self.parent.parent.current = 'excluir_dados'
        self.parent.parent.transition.direction = 'left'
    

class Menu(BoxLayout, MixinMenu):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        self.label_menu = Label(text = 'Menu', font_size = 40)
        
        self.bt_cadastrar = Button(text = 'Cadastrar dívida')
        self.bt_cadastrar.on_press = self.to_cadastrar
        self.bt_buscar = Button(text = 'Buscar dívida')
        self.bt_buscar.on_press = self.to_buscar
        self.bt_devedores = Button(text = 'Todos os devedores')
        self.bt_devedores.on_press = self.to_devedores
        self.bt_total_dividas = Button(text = 'Total de dívidas')
        self.bt_total_dividas.on_press = self.to_dividas
        self.bt_diminuir_divida = Button(text = 'Diminuir uma dívida')
        self.bt_diminuir_divida.on_press = self.to_diminuir
        self.bt_excluir_dados = Button(text = 'Excluir dados')
        self.bt_excluir_dados.on_press = self.to_excluir
        
        self.add_widget(self.label_menu)
        self.add_widget(self.bt_cadastrar)
        self.add_widget(self.bt_buscar)
        self.add_widget(self.bt_devedores)
        self.add_widget(self.bt_total_dividas)
        self.add_widget(self.bt_diminuir_divida)
        self.add_widget(self.bt_excluir_dados)

class MixinComum(object):
    def ir_para_menu(self):
        self.parent.parent.current = 'menu'
        self.parent.parent.transition.direction = 'up'


class Cadastrar(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(Cadastrar, self).__init__(**kwargs)
        
        self.box_cadastrar = BoxLayout(orientation = 'vertical')
        
        self.label_cadastrar = Label(text = 'Cadastrar', font_size = 40)
        
        self.bt_voltar_de_cadastrar = Button(text = 'Voltar para menu')
        self.bt_voltar_de_cadastrar.on_press = self.ir_para_menu
        
        self.box_cadastrar.add_widget(self.label_cadastrar)
        self.box_cadastrar.add_widget(self.bt_voltar_de_cadastrar)
        
        self.add_widget(self.box_cadastrar)


class Buscar(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(Buscar, self).__init__(**kwargs)
        
        self.box_buscar = BoxLayout(orientation = 'vertical')
        self.label_buscar = Label(text = 'Buscar', font_size = 40)
        self.bt_voltar_de_buscar = Button(text = 'Voltar para menu')
        self.bt_voltar_de_buscar.on_press = self.ir_para_menu
        
        self.box_buscar.add_widget(self.label_buscar)
        self.box_buscar.add_widget(self.bt_voltar_de_buscar)
        
        self.add_widget(self.box_buscar)


class TodosDevedores(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(TodosDevedores, self).__init__(**kwargs)
        
        self.box_devedores= BoxLayout(orientation = 'vertical')
        self.label_devedores = Label(text = 'Devedores', font_size = 40)
        self.bt_voltar_de_devedores = Button(text = 'Voltar para menu')
        self.bt_voltar_de_devedores.on_press = self.ir_para_menu
        
        self.box_devedores.add_widget(self.label_devedores)
        self.box_devedores.add_widget(self.bt_voltar_de_devedores)
        
        self.add_widget(self.box_devedores)


class TotalDividas(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(TotalDividas, self).__init__(**kwargs)
        
        self.box_dividas = BoxLayout(orientation = 'vertical')
        self.label_dividas = Label(text = 'Total de dívidas', font_size = 40)
        self.bt_voltar_de_dividas = Button(text = 'Voltar para menu')
        self.bt_voltar_de_dividas.on_press = self.ir_para_menu
        
        self.box_dividas.add_widget(self.label_dividas)
        self.box_dividas.add_widget(self.bt_voltar_de_dividas)
        
        self.add_widget(self.box_dividas)


class DiminuirDivida(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(DiminuirDivida, self).__init__(**kwargs)
        
        self.box_diminuir = BoxLayout(orientation = 'vertical')
        self.label_diminuir = Label(text = 'Diminuir dívida', font_size = 40)
        self.bt_voltar_de_diminuir = Button(text = 'Voltar para menu')
        self.bt_voltar_de_diminuir.on_press = self.ir_para_menu
        
        self.box_diminuir.add_widget(self.label_diminuir)
        self.box_diminuir.add_widget(self.bt_voltar_de_diminuir)
        
        self.add_widget(self.box_diminuir)


class ExcluirDados(Screen, MixinComum):
    def __init__(self, **kwargs):
        super(ExcluirDados, self).__init__(**kwargs)
        
        self.box_excluir = BoxLayout(orientation = 'vertical')
        self.label_excluir= Label(text = 'Excluir dados', font_size = 40)
        self.bt_voltar_de_excluir= Button(text = 'Voltar para menu')
        self.bt_voltar_de_excluir.on_press = self.ir_para_menu
        
        self.box_excluir.add_widget(self.label_excluir)
        self.box_excluir.add_widget(self.bt_voltar_de_excluir)
        
        self.add_widget(self.box_excluir)


class RootWidget(ScreenManager):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        
        self.screen_0 = Screen(name = 'menu')
        self.screen_0.add_widget(Menu())
        
        self.screen_1 = Screen(name = 'cadastrar')
        self.screen_1.add_widget(Cadastrar())

        self.screen_2 = Screen(name='buscar')
        self.screen_2.add_widget(Buscar())
        
        self.screen_3 = Screen(name='todos_devedores')
        self.screen_3.add_widget(TodosDevedores())
        
        self.screen_4 = Screen(name='total_dividas')
        self.screen_4.add_widget(TotalDividas())
        
        self.screen_5 = Screen(name='diminuir_divida')
        self.screen_5.add_widget(DiminuirDivida())
        
        self.screen_6 = Screen(name='excluir_dados')
        self.screen_6.add_widget(ExcluirDados())

        self.add_widget(self.screen_0)
        self.add_widget(self.screen_1)
        self.add_widget(self.screen_2)
        self.add_widget(self.screen_3)
        self.add_widget(self.screen_4)
        self.add_widget(self.screen_5)
        self.add_widget(self.screen_6)
        
        self.current = 'menu'
        

class TestApp(App):
    kv_directory = 'template_0'
    
    title = "Teste de Screen Manager"

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()
