# ui.py
import pygame

class GameUI:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
    
    def draw_stats(self, screen, lives, kill_count):
        # Create the text surfaces
        lives_text = self.font.render(f"Lives: {lives}", True, (255, 255, 255))
        kills_text = self.font.render(f"Kills: {kill_count}", True, (255, 255, 255))
        
        # Get screen dimensions
        screen_width = screen.get_width()
        
        # Position at top center
        lives_rect = lives_text.get_rect()
        lives_rect.centerx = screen_width // 2 - 100
        lives_rect.y = 20
        
        kills_rect = kills_text.get_rect()
        kills_rect.centerx = screen_width // 2 + 100
        kills_rect.y = 20
        
        # Draw the text
        screen.blit(lives_text, lives_rect)
        screen.blit(kills_text, kills_rect)