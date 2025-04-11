import requests
import pytest

# API URL
url = "https://api.practicesoftwaretesting.com/messages"

# 測試數據
data = {
    "name": "Lynn",
    "subject": "return",
    "message": "Quality is not an act, it is a habit. Strive for excellence every day!",
    "email": "lnyjenm@gmail.com",
    "status": "NEW",
    "id": "01jrhsphg3ty5hgr2fqmgf9kpt",
    "created_at": "2025-04-11 06:48:20"
}

def test_post_message():
    # 發送 POST 請求
    response = requests.post(url, json=data)

    # 驗證響應狀態碼
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # 驗證響應格式，忽略大小寫和空格
    assert response.headers['Content-Type'].lower().strip() == 'application/json;charset=utf-8', "Response is not in JSON format"

    # 驗證響應內容
    json_response = response.json()
    assert json_response['name'] == data['name'], "Name does not match"
    assert json_response['subject'] == data['subject'], "Subject does not match"
    assert json_response['message'] == data['message'], "Message does not match"
    assert json_response['email'] == data['email'], "Email does not match"
if __name__ == "__main__":
    pytest.main()