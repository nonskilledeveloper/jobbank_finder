import requests
import lxml.html as html

link_base = 'https://www.jobbank.gc.ca'
link_cookies = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?page=1&sort=D&fsrc=32&fskl=101020'
target = 'https://www.jobbank.gc.ca/jobsearch/job_search_loader.xhtml'

temp_list = []
session = requests.Session()
response = session.get(link_cookies)

def get_urls(target_loads):
    global target
    global temp_list

    temp_num = 0 # << Se inicializa una variable temporal que se utilizará posteriormente
    
    try:
        global response

        for i in range(target_loads):
            response = session.get(target)

        if response.status_code == 200:

            d_code = response.content.decode('utf-8')
            parsed = html.fromstring(d_code)
            parsed = parsed.xpath('//article/a/@href')
            for i in parsed: # << i se vuelve un elemento no iterable al realizar esta acción
                temp_list.append(link_base+parsed[temp_num]) # << Es por ello que se utiliza una variable temporal
                temp_num = temp_num+1
            temp_num = 0
            #print(temp_list)

            return temp_list

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    pass