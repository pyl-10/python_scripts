import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射的子弹类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船的当前位置，创建一个子弹类"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在矩形（0，0）创建项目符号，然后设置正确的位置。
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储子弹位置的十进制值
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """在屏幕上移动子弹"""
        # 更新项目符号的小数位
        self.y -= self.speed_factor
        # 更新矩形位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
