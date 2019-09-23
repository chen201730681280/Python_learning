#coding=gbk
import pygame
class Ship():
	#����ָ���˽��ɴ����Ƶ�ʲô�ط�
	def __init__(self,ai_settings,screen):
		#��ʼ���ɴ����������ʼλ��
		self.screen=screen
		self.ai_settings=ai_settings
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		#Ϊ�˼���ͼ�񣬵���pygame.image.load()
		self.image=pygame.image.load('images/ship.bmp')
		
		#����ͼ��֮��ʹ��get_rect()��ȡ��Ӧsurface����rect
		#�������һ��������ϷԪ��
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		#���·ɴ�������Ļ�м�,����top��bottom��left��right
		#�ɴ����ĵ�x����centerx���ɴ��±�Եy����bottom
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		#��pygame�У�ԭ�㣨0,0��λ����Ļ���Ͻ�
		
		#�ڷɴ�������center�д洢С��ֵ
		self.center=float(self.rect.centerx)
		
		#�ƶ���־
		self.moving_right=False
		self.moving_left=False
	
	#����ɴ�λ��
	def update(self):
		#�����ƶ���־�����ɴ���λ��
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# ����self.center����rect����
		self.rect.centerx = self.center
	def blitme(self):
		#��ָ��λ�û��ɴ�
		self.screen.blit(self.image,self.rect)
