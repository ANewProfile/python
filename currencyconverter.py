import requests
import json

cur1 = input('CUR1: ')
cur2 = input('CUR2: ')
result = requests.get(
    f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cur1}/{cur2}.json')


if result.status_code == 200:
    text_result = json.loads(result.text)
    print(f"As of date: {text_result['date']}\nConversion Rate: {text_result[cur2]}")
else:
    print(f'Didn\'t work. Status code: {result.status_code}')