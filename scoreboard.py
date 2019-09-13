import pygame.font


class ScoreBoard(object):
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分射击的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.pre_score()

    def pre_score(self):
        """将得分转换为一幅渲染的图像"""
        score = str(self.stats.score)
        self.score_img = self.font.render(score, True, self.text_color, self.ai_settings.bg_color)
        self.score_img_rect = self.score_img.get_rect()

        # 将得分放在屏幕右上角
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def draw_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)