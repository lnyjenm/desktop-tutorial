import requests
import pytest

# API URL
url = "https://api.practicesoftwaretesting.com/products?sort=price,desc"

def test_product_api():
    # 發送 GET 請求
    response = requests.get(url)
    
    # 確認狀態碼為 200
    assert response.status_code == 200
    
    # 解析 JSON 數據
    json_data = response.json()
    
    # 確認當前頁碼為 1
    assert json_data['current_page'] == 1
    
    # 確認價格按照高到低排序
    prices = [product['price'] for product in json_data['data']]
    sorted_prices = sorted(prices, reverse=True)  # 降序排序
    assert prices == sorted_prices

if __name__ == "__main__":
    pytest.main()
