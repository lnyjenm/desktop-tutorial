from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#1.開啟網頁duckduckgo並搜尋selenium
'''
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com")
time.sleep(5)
# 搜尋
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium python")
search_box.send_keys(Keys.RETURN)
# 等待結果載入
time.sleep(5)
# 驗證搜尋結果中包含 "selenium"
assert "selenium" in driver.page_source.lower()
driver.quit()
'''
#2.回傳最多出現的一個字元與次數
def most_frequent_char(s):
   from collections import Counter
   counter = Counter(s)
   return counter.most_common(1)[0]
# 測試
#print(most_frequent_char("hello world"))  # 可能輸出: ('l', 3)


#3.列出陣列中的質數
def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False
   return True
def get_primes(nums):
   return [num for num in nums if is_prime(num)]
# 測試
#print(get_primes([2, 3, 4, 5, 10, 11, 13]))  # 輸出: [2, 3, 5, 11, 13]

'''
#4.打開google搜尋python
# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome()
# 打開 Google 網站
driver.get("https://www.google.com")
time.sleep(5)
# 找到搜尋框並輸入關鍵字 "Python"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)
time.sleep(10)
# 驗證結果頁中是否包含 "Python"
assert "Python" in driver.page_source
if "Python" in driver.page_source:
    print("搜尋結果包含 'Python'")
else:
    print("搜尋結果不包含 'Python'")
# 關閉瀏覽器
driver.quit()
'''
#找到陣列中第二大元素
def second_largest(nums):
   if len(nums) < 2:
       return None
   unique_nums = list(set(nums))  # 去除重複元素
   unique_nums.sort(reverse=True)  # 由大到小排序
   return unique_nums[1] if len(unique_nums) > 1 else None
# 測試
#print(second_largest([3, 1, 4, 5, 5]))  # 輸出: 4


import cv2

# 讀取圖片
img = cv2.imread('meme.jpg')# 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
#img = cv2.imread('meme.jpg', cv2.IMREAD_GRAYSCALE)# 使用 cv2.IMREAD_GRAYSCALE 模式
#img = cv2.imread('meme.jpg', 2)# 也可使用數字代表模式
# 檢查圖片是否成功加載
if img is None:
    print("圖片加載失敗，請檢查檔案路徑或檔案是否存在。")
else:
    cv2.imshow('oxxostudio', img) # 使用名為 oxxostudio 的視窗開啟圖片
    #cv2.waitKey(0)  # 等待按鍵
    cv2.waitKey(2000) # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗
    cv2.destroyAllWindows()  # 關閉所有視窗