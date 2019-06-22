import prefabs.prefabs as prefabs
import pygame as pg
import wingbase.scene as scene
import random

#왼쪽 위 부터 넘버링
building_flag = [ [False,[440, 270]], [False,[520,300]] ]
patrol_points = [ [250,200], [520,70], [670,80], [750,350], [620, 450]]
building_dict = {
  'Education Building': [False, [373,416]],
  'Library': [False, [455,445]],
  'Hanyang History Building': [False, [446,585]],
  'Dorm1': [False, [460,230]],
  'Lion Statue': [False, [460,623]],
  'Main Building': [False, [400,550]],
  'IT/BT': [False, [820,360]],
  'Engineering Building 1': [False, [490,500]],
  'Engineering Building 2': [False, [580,550]],
  'HIT': [False, [620,230]],
  'Nature': [False, [280,410]],
  'Music': [False, [610,450]],
  'Music2': [False, [630,410]],
  'Plaza': [False, [390,600]],
  'Rotc': [False, [580,500]],
}
def turn_flag(x,y):
  for i in building_flag:
    if (abs(i[1][0] - x) < 40 and abs(i[1][1] - y) < 40 )  : 
      i[0] = True
      return [True,[i[1][0], i[1][0]]]

class Bar(pg.sprite.Sprite):
  def __init__(self, SCENE, rect, image, edge, overlay, animation, speed, max_val):
    pg.sprite.Sprite.__init__(self)
    self.SCENE=SCENE
    self.original_image = image.copy()
    self.edge = edge
    self.animation_images = animation
    self.speed = speed
    self.overlay = overlay
    self.rect = rect
    self.image = image.copy()
    self.max_val = max_val
    self.val = max_val
  def update_value(self,value):
    self.val = value
    self.image.fill((0,0,0,0))
    image_rect = self.original_image.get_rect()
    image_rect.x -= int(image_rect.width*self.val/self.max_val)
    self.image.blit(self.original_image,image_rect)
    self.image.blit(self.edge, self.edge.get_rect())
    self.image.blit(self.overlay,self.overlay.get_rect(),special_flags = pg.BLEND_RGBA_MULT)
    second_passed = pg.time.get_ticks()/1000
    for i in range(len(self.animation_images)):
      image_rect = self.animation_images[i].get_rect()
      image_rect.x = (second_passed*self.speed[i])%image_rect.width
      self.image.blit(self.animation_images[i],image_rect,special_flags = pg.BLEND_RGBA_MULT)
      image_rect.x -= image_rect.width
      self.image.blit(self.animation_images[i],image_rect,special_flags = pg.BLEND_RGBA_MULT)

class Background(pg.sprite.Sprite):
  def __init__(self, SCENE):
    pg.sprite.Sprite.__init__(self)
    self.SCENE = SCENE
    self.image = pg.image.load('./assets/background_ing.png')
    self.rect = self.image.get_rect()
    self.rect.x = 70
    self.rect.y = -150

class BCGMask(pg.sprite.Sprite):
  def __init__(self, SCENE, IMAGE, NAME):
    pg.sprite.Sprite.__init__(self)
    self.SCENE = SCENE
    self.image = pg.image.load(IMAGE)
    self.rect = self.image.get_rect()
    self.rect.x = 70
    self.rect.y = -150
    self.mask = pg.mask.from_surface(self.image)
    self.name = NAME

class Building(pg.sprite.Sprite):
  def __init__(self, SCENE, x, y):
    pg.sprite.Sprite.__init__(self)
    self.SCENE = SCENE
    self.image = pg.image.load('./assets/building.png')
    self.rect = self.image.get_rect()
    self.rect.x = 70 + x
    self.rect.y = -150 + y

class Flag(pg.sprite.Sprite):
  def __init__(self,SCENE,x,y):
    pg.sprite.Sprite.__init__(self)
    self.SCENE = SCENE
    self.image = pg.image.load('./assets/flag.png')
    self.rect = self.image.get_rect()
    self.rect.center = [x,y]

#class Coffee(pg.sprite.Sprite)

class Scene_TestStage(scene.Scene):
  def __init__(self, WINDOW, CLOCK, FPS = 30, GROUPS = []):
    super().__init__(WINDOW, CLOCK, FPS=30, GROUPS=[])

    self.score = 0
    self.game_font = pg.font.Font('./assets/NotoSans-BoldItalic.ttf',24)
    self.edgemask = BCGMask(self,'./assets/edgemask.png', 'Edge')
    self.group_bcgmask = pg.sprite.Group()
    self.group_bcgmask.add(self.edgemask)
    self.group_buildings = pg.sprite.Group()
<<<<<<< HEAD
    #self.group_buildings.add(Building(self, 370, 420) )
=======
<<<<<<< HEAD
    self.group_buildings.add(BCGMask(self,'assets/bcg_edu.png','Education Building'))
    self.group_buildings.add(BCGMask(self,'assets/bcg_library.png','Library'))
=======
>>>>>>> c5522c277f6f6728cb0762c583b3accceb81dffb
    self.group_buildings.add(BCGMask(self,'./assets/bcg_edu.png','Education Building'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_library.png','Library'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_historic.png','Hanyang History Building'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_dorm1.png','Dorm1'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_lion.png','Lion Statue'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_mainbdg.png','Main Building'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_itbt.png','IT/BT'))
<<<<<<< HEAD
    self.group_buildings.add(BCGMask(self,'./assets/bcg_engi1.png','Engineering Building 1'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_engi2.png','Engineering Building 2'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_business.png','HIT'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_nature.png','Nature'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_paiknammusic.png','Music'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_music2.png','Music2'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_plaza.png','Plaza'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_rotc.png','Rotc'))
=======
    self.group_buildings.add(BCGMask(self,'./assets/bcg_engi2.png','Engineering Building 1'))
    self.group_buildings.add(BCGMask(self,'./assets/bcg_engi1.png','Engineering Building 2'))
>>>>>>> fdcf29b1633c37f5d1e8c8043f1bba3d98721bed
>>>>>>> c5522c277f6f6728cb0762c583b3accceb81dffb
    self.group_enemy = pg.sprite.Group() # 적 그룹!
    self.group_enemybullets = pg.sprite.Group() # 적 총알 그룹!
    self.group_playerbullets = pg.sprite.Group() # 총알 그룹!
    self.group_player = pg.sprite.Group()
    self.group_overlay = pg.sprite.Group()
    self.background = Background(self)
    self.group_background = pg.sprite.Group()
    self.group_background.add(self.background)
    self.group_flag = pg.sprite.Group()
    self.groups.append(self.group_buildings)
    self.groups.append(self.group_bcgmask)
    self.groups.append(self.group_background)
    self.groups.append(self.group_enemy)
    self.groups.append(self.group_enemybullets)
    self.groups.append(self.group_playerbullets)
    self.groups.append(self.group_player)
    self.groups.append(self.group_flag)
    self.groups.append(self.group_overlay)
    self.player = prefabs.Player(self,180,240)
    bar_image = pg.image.load('./assets/bar.png')
    bar2_image = pg.image.load('./assets/bar2.png')
    overlay_image = pg.image.load('./assets/overlay.png')
    overlay2_image = pg.image.load('./assets/overlay2.png')
    edge_image = pg.image.load('./assets/bar_edge.png')
    edge2_image = pg.image.load('./assets/bar2_edge.png')
    animation_image = []
    animation_image.append(pg.image.load('./assets/bar_anim_1.png'))
    animation_image.append(pg.image.load('./assets/bar_anim_2.png'))
    animation_image.append(pg.image.load('./assets/bar_anim_3.png'))
    bar_rect = bar_image.get_rect()
    bar_rect.x = 52
    bar_rect.y = 16
    self.bar_health = Bar(self,bar_rect,bar_image,edge_image,overlay_image,animation_image,[40,80,-30],1000)
    bar2_rect = bar2_image.get_rect()
    bar2_rect.x = 52
    bar2_rect.y = 64
    self.bar_time = Bar(self,bar2_rect,bar2_image,edge2_image,overlay2_image,animation_image,[40,80,-30],60000)
    self.group_overlay.add(self.bar_health)
    self.group_overlay.add(self.bar_time)
    self.group_player.add(self.player)
    self.enemy_timer = pg.time.get_ticks()
    self.finish_timer = pg.time.get_ticks()
    self.death_time = -1
    self.spawn_enemy()

    pg.mixer.music.load('./assets/sound/HYU_schoolsong_mr_16bit.wav')
    pg.mixer.music.play(-1)

  def spawn_enemy(self):
    char_selector = random.randint(0,1)
    pos = [0,0]
    if char_selector == 0:
      pos = [505, 500]
    elif char_selector == 1:
      pos = [790,130]
    self.group_enemy.add(prefabs.Enemy(self,pos[0],
      pos[1],self.player,patrol_points[random.randint(0,4)],0))
  def loop(self):
    self.bar_health.update_value(1000-self.player.health)
    self.bar_time.update_value(pg.time.get_ticks()-self.finish_timer)
    time_left = 60000-(pg.time.get_ticks()-self.finish_timer)
    if pg.time.get_ticks() - self.enemy_timer > 20000:
      self.enemy_timer = pg.time.get_ticks()
      self.spawn_enemy()
    collision = pg.sprite.groupcollide(self.group_player,self.group_buildings,False,False,pg.sprite.collide_mask)
    for player in collision:
      for building in collision[player]:
<<<<<<< HEAD
        index = building_dict[building.name]
        if index[0] == False:
          index[0] = True
          flag = Flag(self, index[1][0] + 85, index[1][1] - 180)
          self.group_flag.add(flag)
          self.groups.append(self.group_flag)
=======
        flag = Flag(self, self.player.x, self.player.y)
        self.group_flag.add(flag)
        self.groups.append(self.group_flag)
>>>>>>> c5522c277f6f6728cb0762c583b3accceb81dffb
    collision = pg.sprite.groupcollide(self.group_enemy,self.group_playerbullets,False,True)
    for enemy in collision:
      for bullet in collision[enemy]:
        bullet.destroy()
        enemy.hit(10)
    collision = pg.sprite.groupcollide(self.group_player,self.group_enemy,False,True)
    for player in collision:
      for enemy in collision[player]:
        enemy.destroy()
        self.player.hit(50)
    collision = pg.sprite.groupcollide(self.group_enemybullets,self.group_playerbullets,True,True)
    for bullet in collision:
      for enemybullet in collision[bullet]:
        enemybullet.destroy()
      bullet.destroy()
    if not self.player.alive() and pg.time.get_ticks()-self.death_time > 2000: return 2
    if time_left < 0: return 1
    return 0
  def event_handle(self, event):
    if event.type == pg.MOUSEBUTTONDOWN:
      self.player.launch()
    super().event_handle(event)

if __name__ == "__main__":
  pg.init()
  pg.font.init()
  SCREEN = (1080, 720)
  WINDOW = pg.display.set_mode(SCREEN)
  FPS = 60
  CLOCK = pg.time.Clock()
  SCENE = Scene_TestStage(WINDOW, CLOCK, 60, [])

  while True:
    SCENE.loop_begin()
    SCENE.loop()
    SCENE.loop_tick()
