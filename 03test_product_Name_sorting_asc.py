import requests
import pytest

def test_product_Name_sorting():
    # 發送 GET 請求
    url = "https://api.practicesoftwaretesting.com/products?sort=name,asc&between=price,1,30&page=0"
    response = requests.get(url)

    # 確認狀態碼為 200
    assert response.status_code == 200

    # 解析 JSON 數據
    json_data = response.json()

    # 確認當前頁碼為 1
    assert json_data['current_page'] == 1

    # 確認所有產品價格在 1 到 30 的範圍內
    for product in json_data['data']:
        assert 1 < product['price'] < 30

    # 確認產品名稱按照正序排列
    product_names = [product['name'] for product in json_data['data']]
    sorted_names = sorted(product_names)
    assert product_names == sorted_names

if __name__ == "__main__":
    pytest.main()
