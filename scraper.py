import csv

import requests
import json
urls = [
    'https://brnsk.lenta.com/special-nye-predlozheniya/',
    'https://brnsk.lenta.com/ovoschi-frukty/',
    'https://brnsk.lenta.com/myaso-vypechka-kulinariya/',
    'https://brnsk.lenta.com/gastronom/',
    'https://brnsk.lenta.com/moreprodukty/',
    'https://brnsk.lenta.com/molochnye-produkty-zamorozhennye-produkty/',
    'https://brnsk.lenta.com/konditerskie-izdeliya-7th-june/',
    'https://brnsk.lenta.com/chay-kofe-torty-hleb/',
    'https://brnsk.lenta.com/bakaleya-7th-june-1/',
    'https://brnsk.lenta.com/napitki-7th-june/'

]
type = ['Специальные предложения','Овощи. Фрукты','Мясо. Выпечка. Кулинария','Гастроном','Морепродукты','Молочные продукты.Замороженные продукты', 'Кондитерские изделия','Чай, Кофе, Торты, Хлеб',
        'Бакалея','Напитки']
with open('/tmp/data.csv', 'w') as csvfile:
    fieldnames = ['Название', 'Цена для покупателей без карты', 'Цена для покупателей с картой', 'Описание','Дата обновления']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i,url in enumerate(urls):
        print(url)

        writer.writerow({}
        )
        writer.writerow(
            {}
        )
        writer.writerow(
            {
                'Название':type[i]
            }
        )
        resp = requests.get(url)
        items = resp.text.split('myTovarList.items=')[1].split('myTovarList.order')[0].replace(';','')


        items = json.loads(items)
        for item in items:
            writer.writerow({
                'Название': item.get('name'),
                'Цена для покупателей без карты': item.get('old_price'),
                'Цена для покупателей с картой': item.get('new_price'),
                'Описание': item.get('short_text1'),
                'Дата обновления': item.get('updated_at')

            })
