import requests
from bs4 import BeautifulSoup
import os
import sys



def crawl_question(url,qfile):
    source_code = requests.get(url).text
    htmltree = BeautifulSoup(source_code, 'lxml')
    
    for quesdiv in htmltree.find_all('div',{'class':'post-text'}):

        question=quesdiv.find_all('p')
        for qn in question:
            qtext=qn.text
            
            qtext=qtext+'\n'
            #print(qtemp)
            qfile.write(qtext)



def crawl_question_link(base_url, end_url, page_limit,qfile):
    page_no = 1
    while page_no <= page_limit:
        page_url = base_url + str(page_no) + end_url
        source_code = requests.get(page_url).text
        #print(source_code)
        soup = BeautifulSoup(source_code, 'html.parser')
        if page_no is 1:
            os.system('clear')
        print('crawling page ' + str(page_no) + ': [', end='')
        prev_len = 0
        q_no = 1
        for ques_link in soup.find_all('a', {'class': 'question-hyperlink'}):
            url = 'http://stackoverflow.com/' + ques_link.get('href')
            crawl_question(url,qfile)
            for _ in range(prev_len):
                print('\b', end='')
            print('#', end='')
            p_cent = q_no*2
            percent = '] (' + str(p_cent) + '%)'
            prev_len = len(percent)
            print(percent, end='')
            sys.stdout.flush()
            q_no += 1
        page_no += 1


def main():
    page_limit = int(input('Enter no. of pages to crawl : '))
    #os.system('clear')
    print('starting crawling...')
    qfile=open('questions_file.txt','w')
    crawl_question_link('http://stackoverflow.com/questions?page=', '&sort=newest', page_limit,qfile)
    

main()