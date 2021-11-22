from typing import Mapping
import requests
from bs4 import BeautifulSoup

def get_citations_needed_report(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.content,"html.parser")

    body_content = soup.find('div' ,id = "bodyContent")
    p_list = body_content.find_all('p')

    # print(p_list)

    need_citation = []

    for p in p_list :
        sup = p.find("sup", class_ = "noprint" )
        if sup :
            span = sup.find("span")
            if span != None :
                if span.get_text() == "citation needed":
                    need_citation.append(p.get_text())

    return "".join(need_citation)

def get_citations_needed_count(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.content,"html.parser")

    body_content = soup.find('div' ,id = "bodyContent")
    p_list = body_content.find_all('p')

    # print(p_list)

    counter = 0

    for p in p_list :
        sup = p.find_all("sup", class_ = "noprint" )
        # counter += len(sup)
        if sup :
            for i in sup :
                span = i.find("span")
                if span != None :
                    if span.get_text() == "citation needed":
                        counter +=1 

    return counter

if __name__ == "__main__":
    result = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
    print(result)
    count = get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    print(count)