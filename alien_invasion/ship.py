#coding=gbk
import pygame
class Ship():
	#后者指定了将飞船绘制到什么地方
	def __init__(self,ai_settings,screen):
		#初始化飞船并设置其初始位置
		self.screen=screen
		self.ai_settings=ai_settings
		
		#加载飞船图像并获取其外接矩形
		#为了加载图像，调用pygame.image.load()
		self.image=pygame.image.load('images/ship.bmp')
		
		#加载图像之后，使用get_rect()获取相应surface属性rect
		#像处理矩形一样处理游戏元素
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#将新飞船放在屏幕中间,可用top，bottom，left，right
		#飞船中心的x坐标centerx，飞船下边缘y坐标bottom
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		#在pygame中，原点（0,0）位于屏幕左上角
		
		#在飞船的属性center中存储小数值
		self.center=float(self.rect.centerx)
		
		#移动标志
		self.moving_right=False
		self.moving_left=False
	
	#管理飞船位置
	def update(self):
		#根据移动标志调整飞船的位置
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# 根据self.center更新rect对象
		self.rect.centerx = self.center
	def blitme(self):
		#在指定位置画飞船
		self.screen.blit(self.image,self.rect)
