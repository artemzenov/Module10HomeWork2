from threading import Thread
from time import sleep


class Knight(Thread):
    
    enemy = 100
    
    def __init__(self, name, power):
        
        Thread.__init__(self)
        self.name = name
        self.power = power
    
    def fight(self):
        
        count_day = 0
        
        while self.enemy:
            
            self.enemy -= self.power
            sleep(1)
            count_day += 1
            print(f'{self.name} сражается {count_day}..., ' 
                  f'осталось {self.enemy} воинов')
        
        print(f'{self.name} одержал победу спустя '
              f'{count_day} дней(дня)!')
    
    def run(self):
      
        print(f'{self.name}, на нас напали!')
        self.fight()



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
sleep(0.01) #чтобы не слипались строки при выводе
second_knight.start()

while first_knight.is_alive() or second_knight.is_alive():
      pass
else:
      print('Все битвы закончились!')
