#coding=gbk
#导入模块sys，玩家退出时将使用模块sys来退出
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
	#按q可以退出游戏
	elif ecent.key==pygame.K_q:
			sys.exit()
				
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed: 
		# 创建一颗子弹，并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings, screen, ship) 
		bullets.add(new_bullet)
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False	
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False	

#监视键盘和鼠标事件
#pygame.event.get()所有键盘和鼠标事件都将促使for循环
def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		#按键按下去
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		#按键松开
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
		'''
		每当用户按键时，都将在pygame中注册一个事件。
		事件都是通过方法pygame.event.get()获取的，因此在check中国
		我们需要指定要检查哪些类型的事件
		每次按键都被注册为一个KEYDOWN事件
		检测到keydown事件时，我们需要检查按下的是否是特定的键
		按下的是右键时就增大rect.centerx值
		'''
		
	
def update_screen(ai_settings,screen,ship,bullets):
	#每次循环时都重绘屏幕,用背景色填充屏幕
	screen.fill(ai_settings.bg_color)
	
	#确保飞机出现在背景之前
	ship.blitme()
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites(): 
		bullet.draw_bullet()	
	#让最近绘制的屏幕可见
	#每次执行while循环时都绘制一个空屏幕，以显示元素的新位置，
	#并在原来的位置隐藏元素，从而营造平滑移动的效果
	pygame.display.flip()	

def update_bullets(bullets):
	#更新子弹的位置，删除消失的子弹
	bullets.update()
		
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
			print(len(bullets))
