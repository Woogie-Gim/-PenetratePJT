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
sort = 'CustomRating'

URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}&sort={sort}"

#request 보내기
response = requests.get(URL)

#받은 response를 json 타입으로 바뀌주기
response_json = response.json()


def best_review_books():
    author_list = []
    for i in range(20):
        if response_json['item'][i]['customerReviewRank'] >= 9:
            temp = response_json['item'][i]
            author_list.append(temp)
    
    return author_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
