import random
import time

def displayIntro():
    print('''你來到了一個充滿龍的國度。你面前有兩個洞穴。
在其中一個洞穴中，住著一隻友善的龍，牠願意與你分享牠的財寶。
另一個洞穴中，住著一隻貪婪又飢餓的龍，牠會一見到你就把你吃掉。''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('你想進入哪個洞穴？（1 或 2）')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('你慢慢地走向洞穴...')
    time.sleep(2)
    print('裡面又黑又陰森...')
    time.sleep(2)
    print('一隻巨大的龍突然跳了出來！牠張開大嘴，然後...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('牠把財寶送給了你！')
    else:
        print('牠一口就把你吞下去了！')
