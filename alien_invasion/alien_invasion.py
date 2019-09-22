#coding=gbk

#pygame����������Ϸ����Ҫ�Ĺ���
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#��ʼ����Ϸ������һ����Ļ����,��ʼ����������
	pygame.init()
	ai_settings=Settings()
	#����һ����Ϊscreen����ʾ���ڣ������ǳߴ磬ǰΪ����Ϊ��
	#screen��һ��surface,������ʾ��ϷԪ�أ��ڴ���Ϸ�У�ÿ���ɻ��ȵȶ���һ��surface
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#����һ�ҷɴ�
	ship=Ship(ai_settings,screen)
	#����һ�����ڴ洢�ӵ��ı���,�Ա��ڹ������ȥ�������ӵ�
	bullets=Group()
	
	
	#��ʼ��Ϸ����ѭ�������а���һ���¼�ѭ���Լ�������Ļ���µĴ���
	#�¼����û�����Ϸʱִ�еĲ���
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
