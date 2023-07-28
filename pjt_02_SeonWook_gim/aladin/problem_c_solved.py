import requests
from pprint import pprint

ttbkey = 'ttbkct72621114001'
query = '파울로 코엘료'
query_type = 'Author'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101
Sort = 'SalesPoint'

URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}&Sort={Sort}"

#request 보내기
response = requests.get(URL)

#받은 response를 json 타입으로 바뀌주기
response_json = response.json()

def bestseller_book():
    author_list = []
    for i in range(5):
        temp = response_json['item'][i]['title']
        author_list.append(temp)
    
    return author_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

