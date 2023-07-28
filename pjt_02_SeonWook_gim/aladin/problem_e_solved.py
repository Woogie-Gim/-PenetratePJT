import requests
from pprint import pprint

ttbkey = 'ttbkct72621114001'
query_type = 'Keyword'
max_results = 20
start = 1
search_target = 'eBook'
output = 'js'
version = 20131101

def ebook_list(title):
    try:
        URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&query={title}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

        response = requests.get(URL)
        response_json = response.json()

        book_list = {}

        a = response_json['item'][0]['isbn']
        b = response_json['item'][0]['itemId']
        c = response_json['item'][0]['link']
        d = response_json['item'][0]['priceSales']

        book_list = {'isbn' : a, 'itemId' : b, 'link' : c, 'priceSales' : d}
        
        my_ebook_list = []
        my_ebook_list.append(book_list)

        return my_ebook_list
    except:
        return None    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
