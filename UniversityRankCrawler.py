import requests
from bs4 import BeautifulSoup
import json

def text_output(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

def get_qs_uni_rank_data():
    # html = requests.get("https://www.topuniversities.com/university-rankings/university-subject-rankings/2017/computer-science-information-systems")
    # soup = BeautifulSoup(html.text)
    # print(soup.prettify())
    try:
        response = requests.get(
            "https://www.topuniversities.com/sites/default/files/qs-rankings-data/335202.txt?_=1498202742952")
        # print(response.json())
        data = response.json()['data']
        return data
    except response.raise_for_status():
        print(response.reason)

def qs_uni_rank_us(data, location = 'World'):

    if location == 'World':
        l = [x['title'] for x in data]
    else:
        l = [x['title'] for x in data if x['country'] == location]

    print(l)
    print("".join(str(x) + '\n' for x in l))

    # for i, obj in enumerate(data):
    #     if obj['country'] == 'United States':
    #         line = str(i+1) + ' ' + obj['title'] + '\n'
    #         print(line)
    #         data += line
            # index += 1

    return "".join(str(x) + '\n' for x in l)

def main():
    data = get_qs_uni_rank_data()
    us_list = qs_uni_rank_us(data)
    text_output('./data/qs_uni_rank_world.txt', us_list)

if __name__ == "__main__": main()