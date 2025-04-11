import requests
import pytest

def test_product_prices_within_range():
    # 發送 GET 請求
    API_URL = "https://api.practicesoftwaretesting.com/products?between=price,1,78"
    response = requests.get(API_URL)
    # 確認狀態碼為 200
    assert response.status_code == 200
    # 解析 JSON 數據
    json_data = response.json()
    # 設定期望的價格範圍
    expected_min_price = 1
    expected_max_price = 78
    # 檢查所有產品價格是否在範圍內
    for product in json_data['data']:
        price = product['price']
        assert price >= expected_min_price, f"價格 {price} 未達到最小值 {expected_min_price}"
        assert price < expected_max_price + 1, f"價格 {price} 超過最大值 {expected_max_price}"
if __name__ == "__main__":
    pytest.main()