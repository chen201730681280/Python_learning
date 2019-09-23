#coding=gbk
#����ģ��sys������˳�ʱ��ʹ��ģ��sys���˳�
import sys
import pygame
from bullet import Bullet	
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key == pygame.K_LEFT:
		ship.moving_left=True		
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	#��q�����˳���Ϸ
	elif ecent.key==pygame.K_q:
			sys.exit()
				
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed: 
		# ����һ���ӵ�����������뵽����bullets��
		new_bullet = Bullet(ai_settings, screen, ship) 
		bullets.add(new_bullet)
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False	
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False	

#���Ӽ��̺�����¼�
#pygame.event.get()���м��̺�����¼�������ʹforѭ��
def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		#��������ȥ
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		#�����ɿ�
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
		'''
		ÿ���û�����ʱ��������pygame��ע��һ���¼���
		�¼�����ͨ������pygame.event.get()��ȡ�ģ������check�й�
		������Ҫָ��Ҫ�����Щ���͵��¼�
		ÿ�ΰ�������ע��Ϊһ��KEYDOWN�¼�
		��⵽keydown�¼�ʱ��������Ҫ��鰴�µ��Ƿ����ض��ļ�
		���µ����Ҽ�ʱ������rect.centerxֵ
		'''
		
	
def update_screen(ai_settings,screen,ship,bullets):
	#ÿ��ѭ��ʱ���ػ���Ļ,�ñ���ɫ�����Ļ
	screen.fill(ai_settings.bg_color)
	
	#ȷ���ɻ������ڱ���֮ǰ
	ship.blitme()
	# �ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites(): 
		bullet.draw_bullet()	
	#��������Ƶ���Ļ�ɼ�
	#ÿ��ִ��whileѭ��ʱ������һ������Ļ������ʾԪ�ص���λ�ã�
	#����ԭ����λ������Ԫ�أ��Ӷ�Ӫ��ƽ���ƶ���Ч��
	pygame.display.flip()	

def update_bullets(bullets):
	#�����ӵ���λ�ã�ɾ����ʧ���ӵ�
	bullets.update()
		
	#ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
			print(len(bullets))
