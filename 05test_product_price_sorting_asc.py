import requests
import pytest

# API URL
url = "https://api.practicesoftwaretesting.com/products?sort=price,asc"

def test_product_price_sorting_asc():
    # 發送 GET 請求
    response = requests.get(url)
    
    # 確認狀態碼為 200
    assert response.status_code == 200
    
    # 解析 JSON 數據
    json_data = response.json()
    
    # 確認當前頁碼為 1
    assert json_data['current_page'] == 1
    
    # 確認價格按照低到高排序
    prices = [product['price'] for product in json_data['data']]
    sorted_prices = sorted(prices)
    assert prices == sorted_prices

if __name__ == "__main__":
    pytest.main()
