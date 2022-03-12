
import tkinter


class Matrix:
    def __init__(self,width:int=100,height:int=100,tile_size=50,user_x:int=0,user_y:int=0):
        self.create_zero_world(width,height)
        self.view_width:int=width
        self.view_height:int=height
        self.tile_size:int=tile_size
        self.user_x:int=user_x
        self.user_y:int=user_y
        self.speed_x:int=10
        self.speed_y:int=10
    #世界生成系統
    def create_zero_world(self,width:int,height:int):
        """
        全ての要素が0の世界を生成
        """
        self.world:list[list]=[[0 for j in range(width)] for i in range(height)]
    def create_n_world(self,width:int,height:int,n=0):
        """
        全ての要素がn（任意）の世界を生成
        """
        self.world:list[list]=[[n for j in range(width)] for i in range(height)]
    def user_tile_position(self)->tuple[int,int]:
        """
        userのtile上での位置
        """
        return int(self.user_x/self.tile_size),int(self.user_y/self.tile_size)
    def mouse_tile_position(self,x:int,y:int):
        """
        viewスペースにおけるmouse座標を入力
        
        """
        return int((self.user_x+x)/self.tile_size),int((self.user_y+y)/self.tile_size)
    def get_world_element(self,tile_x:int,tile_y:int):
        return self.world[tile_y][tile_x]
    def draw_start_position(self):
        """
        guiのキャンバスなどで描画を開始する際の一番左上に来るtileの描画すべき座標位置
        """
        return -(self.user_x%self.tile_size),-(self.user_y%self.tile_size)
    

class AppSys(tkinter.Canvas):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
    def loop(self):
        pass