#coding=gbk
import pygame
#ͨ��ʹ�þ��飬�ɽ���Ϸ����ص�Ԫ�ر��飬ͬʱ���������е�����Ԫ��
from pygame.sprite import Sprite

#���ڹ���ɴ�������ӵ�
class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		#�ڷɴ���λ�ô���һ���ӵ�����
		super(Bullet,self).__init__()
		self.screen=screen

		#��0��0������һ�ݱ�ʾ�ӵ��ľ��Σ���������ȷ��λ��
		#�������ӵ�������rect��pygame��rect�ӿհ״���ʼ����һ������
		#����������ʵ�����������ṩ�������Ͻǵ�x����y����
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		#���ӵ���x��Ϊ�ɴ���x���ӵ��ӷɴ�������������ӵ���rect��Ϊ�ɴ���top
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
	
		#�洢��С����ʾ���ӵ�λ��,����΢���ӵ��ٶ�
		self.y=float(self.rect.y)
	
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
	
	#�����ӵ���λ�ã��ӵ�������y���ϼ���
	def update(self):
		self.y -=self.speed_factor
		#���±�ʾ�ӵ��� rect��λ��
		self.rect.y=self.y
	
	#����Ļ�ϻ滭�ӵ�
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
