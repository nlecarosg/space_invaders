# Definir la nave del jugador como una clase
class nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 10
        self.speed = 5                                  # Velocidad de la nave, inicial 5
        self.kills = 0                                  # Contador de enemigos cazados

    def update(self):
        # Capturar las teclas izquierda y derecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Disparar
        if keys[pygame.K_SPACE]:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    def draw_kills(self):
        font = pygame.font.SysFont(None, 30)
        text = font.render("Kills: " + str(self.kills), True, white)
        screen.blit(text, (10, 10))