import pypboy
import pygame
import game
import config

class Module(pypboy.SubModule):

	label = " Weapons "

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		handlers = []
		item_names = []
		INVENTORY = [
			Weapon('Chinese Assault Rifle','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Combat Shotgun','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Deathclaw Gauntlet','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Flamer','images/inventory/flamer.png',20,10,250,100,''),
			Weapon('Hunting Rifle','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Minigun','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Missile Launcher','images/inventory/flamer.png',0,0,0,0,''),
			Weapon('Pulse Grenade (2)','images/inventory/flamer.png',0,0,0,0,'')
		]
		selected = 3
		for i in INVENTORY:
			print "%s" % (i.name)
			handlers.append(self.change_items)
			item_names.append(i.name)
		self.menu = pypboy.ui.Menu(200, item_names, handlers, selected, 15)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		#show weapon image
		weapon_to_display = INVENTORY[selected]
		weapon_to_display.rect = weapon_to_display.image.get_rect()
		weapon_to_display.image = weapon_to_display.image.convert()
		weapon_to_display.rect[0] = 200
		weapon_to_display.rect[1] = 40	
		self.add(weapon_to_display)		
		#Show Weapon stats - Value
		text = config.FONTS[14].render(weapon_to_display.value, True, (95, 255, 177), (0, 0, 0))
		pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.rect[3] + 5 ), (config.WIDTH - 13, weapon_to_display.rect[1] + weapon_to_display.rect[3] + 25), 2)	#End of title Verticle bar
		self.image.blit(text, (config.WIDTH - (text.get_width() + 5), 19))
		pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 50, 15), (config.WIDTH - 13, 15), 2) # Horizontal Bar
		
		
	def change_items(self):
		print "Changing"
		
class Weapon(game.Entity):
	def __init__(self, name, imageloc, damage, weight, value, condition, notes): 
		super(Weapon, self).__init__()
		self.name = name
		self.imageloc = imageloc
		self.image = pygame.image.load(self.imageloc)
		self.damage = damage
		self.weight= weight
		self.value = value
		self.condition = condition
		self.notes = notes