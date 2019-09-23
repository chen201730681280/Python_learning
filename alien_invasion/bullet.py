#coding=gbk
import pygame
#通过使用精灵，可将游戏中相关的元素编组，同时操作编组中的所有元素
from pygame.sprite import Sprite

#用于管理飞船发射的子弹
class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		#在飞船的位置创造一个子弹对象
		super(Bullet,self).__init__()
		self.screen=screen

		#在0，0处创建一份表示子弹的矩形，在设置正确的位置
		#创建了子弹的属性rect，pygame。rect从空白处开始创建一个矩形
		#创建这个类的实例，，必须提供矩形左上角的x坐标y坐标
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		#将子弹的x设为飞船的x，子弹从飞船顶部射出，则子弹的rect设为飞船的top
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
	
		#存储用小数表示的子弹位置,便于微调子弹速度
		self.y=float(self.rect.y)
	
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
	
	#管理子弹的位置，子弹发出，y不断减少
	def update(self):
		self.y -=self.speed_factor
		#更新表示子弹的 rect的位置
		self.rect.y=self.y
	
	#在屏幕上绘画子弹
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
