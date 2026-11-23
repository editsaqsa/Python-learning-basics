import requests
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("status code:", response.status_code)

    data = response.json()
    print("Data type:",type(data))
    print("title:", data.get("title"))
    print("Completed:",data.get("completed"))

except requests.exceptions.timeout:
   print("Request time out ho gya-internet connection slow ya unstable ho skta hai")
except requests.exceptions.RequestException as e:
    print("Request mein msla aaya:",e)