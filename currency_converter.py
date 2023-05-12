import requests
import json


def main():
    cur1 = input('CUR1: ')
    cur2 = input('CUR2: ')
    p_cur1 = cur1.lower()
    p_cur2 = cur2.lower()
    result = requests.get(
        f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{p_cur1}/{p_cur2}.json')


    if result.status_code == 200:
        text_result = json.loads(result.text)
        print(f"As of date: {text_result['date']}\nConversion Rate: {text_result[p_cur2]}")
    else:
        print(f'Didn\'t work. Status code: {result.status_code}')
