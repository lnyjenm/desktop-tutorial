import requests
import pytest

# 測試的 API URL
url = "https://api.practicesoftwaretesting.com/123"

def test_resource_not_found():
    # 發送 GET 請求
    response = requests.get(url)

    # 驗證響應狀態碼
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"

    # 驗證響應內容
    json_response = response.json()
    assert json_response['message'] == "Resource not found", "Message does not match"
if __name__ == "__main__":
    pytest.main()