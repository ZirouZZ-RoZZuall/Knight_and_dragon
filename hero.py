from time import *
time_out = 2
class Hero():
    def __init__(self,name,health,armor,power,weapon): # тут значения
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self): #тут печатать
        print('Поприветствуйте Героя --',self.name)
        print('Здоровье:',self.health)
        print('Броня:',self.armor)
        print('Сила удара:',self.power)
        print('Оружие:',self.weapon,'\n')

    def strike(self,enemy): #тут анализировать бой
        print(f'\nУдар! {self.name} атакует {enemy.name} с силой {self.power}, используя {self.weapon}\n')
        sleep(time_out)
        
        enemy.armor -= self.power
        if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0     


        print(f'{enemy.name} покачнулся.\nПоказатель его брони упал до {enemy.armor}.\nА показатель здоровья до {enemy.health}.')

    def fight(self,enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health < 0:
                print(f'{enemy.name} пал в этом нелёгком бою...')
                break
            sleep(time_out)
            enemy.strike(self)
            if self.health < 0:
                print(f'{self.name} пал в этом нелёгком бою...')
                break
            sleep(time_out)
