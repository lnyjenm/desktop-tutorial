import requests
import pytest

# API URL
BASE_URL = "https://api.practicesoftwaretesting.com/products"

# 測試案例
def test_product_price_and_page():
    params = {
        "sort": "name,asc",
        "between": "price,1,50",
        "page": 2
    }
    
    # 發送 GET 請求
    response = requests.get(BASE_URL, params=params)
    
    # 確認狀態碼為 200
    assert response.status_code == 200
    
    # 解析 JSON 數據
    json_data = response.json()
    
    # 確認當前頁碼為 2
    assert json_data['current_page'] == 2
    
    # 確認所有產品價格在 1 到 50 的範圍內
    for product in json_data['data']:
        assert 1 <= product['price'] < 51  # 價格在 1 到 50 之間

if __name__ == "__main__":
    pytest.main()
