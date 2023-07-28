import requests
from pprint import pprint

ttbkey = 'ttbkct72621114001'
query_type = 'Keyword'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

def author_other_works(title):
    try:
        URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&query={title}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

        # request 보내기
        response = requests.get(URL)

        # 받은 response를 json 타입으로 바꾸기
        response_json = response.json()

        author = response_json['item'][0]['author'].split('(지은이)')
        my_author = author[0]

        query_type2 = 'Title'
        URL2 = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&query={my_author}&QueryType={query_type2}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
        
        response2 = requests.get(URL2)

        response_json2 = response2.json()
        

        book_list = []

        for i in range(5):
            temp = response_json2['item'][i]['title']
            book_list.append(temp)

        return book_list

    except:
        return None
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
