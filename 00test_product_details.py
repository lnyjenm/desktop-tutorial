import requests
import pytest

def test_product_details():
    url = "https://api.practicesoftwaretesting.com/products/01JRHG2XV96ZSJM3XV7K2H66ZV"
    expected_product_id = "01JRHG2XV96ZSJM3XV7K2H66ZV"
    expected_name = "Combination Pliers"
    expected_price = 14.15
    expected_in_stock = True
    expected_description_keyword = "Lorem ipsum"
    # 發送 GET 請求
    response = requests.get(url)
    # 確認回應狀態碼為 200 OK
    assert response.status_code == 200
    # 獲取 JSON 數據
    response_data = response.json()
    # 驗證產品 ID
    assert response_data['id'] == expected_product_id, f"Expected product ID {expected_product_id}, but got {response_data['id']}"
    # 驗證產品名稱
    assert response_data['name'] == expected_name, f"Expected product name {expected_name}, but got {response_data['name']}"
    # 驗證產品價格
    assert response_data['price'] == expected_price, f"Expected product price {expected_price}, but got {response_data['price']}"
    # 驗證庫存狀態
    assert response_data['in_stock'] == expected_in_stock, f"Expected in stock status {expected_in_stock}, but got {response_data['in_stock']}"
    # 驗證產品描述是否包含特定關鍵字
    assert expected_description_keyword in response_data['description'], f"Expected description to contain '{expected_description_keyword}'"
if __name__ == "__main__":
    pytest.main()
