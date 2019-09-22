#coding=gbk

#pygame包含开发游戏所需要的功能
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象,初始化背景设置
	pygame.init()
	ai_settings=Settings()
	#创建一个名为screen的显示窗口，数字是尺寸，前为宽，后为高
	#screen是一个surface,用于显示游戏元素，在此游戏中，每个飞机等等都是一个surface
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船
	ship=Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组,以便于管理发射出去的所有子弹
	bullets=Group()
	
	
	#开始游戏的主循环，其中包含一个事件循环以及管理屏幕更新的代码
	#事件是用户玩游戏时执行的操作
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
