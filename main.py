from hero import Hero

dragon_text = '\nПройдя много препятствий, Ричард встречает спящего дракона в свой пещере, на которого давно жаловались жители королевства.\nГерой пытается осторожно пройти мимо, но дракон замечает его, и начинается схватка.\n'
dragon_defeat = '\nДракон побеждён, но нашего героя ещё ждут множество других приключений впереди, так что оставайтесь с нами и с этой игрой на связи!\n'
buff = '\nНашему герою удалось остаться в живых, и он стал сильнее. Он получает новые характеристики!\n'
knight = Hero('Ричард',50,25,20,'меч')
knight.print_info()
rascal = Hero('Хелен',20,5,5,'лук')
rascal.print_info()
knight.fight(rascal)
print(buff)
if knight.health > 0:
    knight.health = 50 
    knight.armor = 25 * 2
    knight.power = 20 * 2
    knight.weapon = 'двуручный меч'
    print('\n')
    knight.print_info()

dragon = Hero('Дракон',120,20,20,'Когти, хвост')
print(dragon_text)

knight.fight(dragon)
print(dragon_defeat)
