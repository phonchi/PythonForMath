import random
import time
_____________ # 載入遊戲模組

playAgain = 'yes'

while playAgain == 'yes':
    # 使用遊戲模組中的 displayIntro() 顯示遊戲資訊
    ______________
    # 讀取使用者輸入並通過調用遊戲模組中的 chooseCave() 函數返回洞穴號碼
    caveNumber = ________________
    # 通過調用遊戲模組中的 checkCave() 函數並提供適當的引數檢查洞穴是否安全
    ______(_____)

    print('你想再玩一次嗎？（是或否）')
    playAgain = input()
