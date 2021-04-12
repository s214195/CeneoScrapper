import requests
from bs4 import BeautifulSoup
import json

extracted_opinions = []

product_id = input("Podaj kod produktu: ")
next_page = "https://www.ceneo.pl/{}#tab=reviews".format(product_id)

while next_page:

    respons = requests.get(next_page)

    page_dom = BeautifulSoup(respons.text, "html.parser")

    opinions = page_dom.select("div.js_product-review")
    for opinion in opinions:

        opinion_id = opinion["data-entry-id"]
        author = opinion.select("span.user-post__author-name").pop(0).get_text().strip()
        try:
            recommendation = opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
            recommendation = recommendation=="Polecam"
        except IndexError:
            recommendation = None
        stars = opinion.select("span.user-post__score-count").pop(0).get_text().strip()
        stars = float(stars.split("/")[0].replace(",","."))
        content = opinion.select("div.user-post__text").pop(0).get_text().strip()
        try:
            pros = opinion.select(
            "div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item")
            pros = [x.get_text().strip() for x in pros]
        except IndexError:
            pros = None
        try:
            cons = opinion.select(
            "div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item")
            cons = [x.get_text().strip() for x in cons]
        except IndexError:
            cons = None
        try:
            purchased = bool(opinion.select("div.review-pz").pop(0).get_text().strip())
        except IndexError:
            purchased = False
        submit_date = opinion.select(
            "span.user-post__published > time:nth-child(1)").pop(0)["datetime"].strip()
        try:
            purchase_date = opinion.select(
            "span.user-post__published > time:nth-child(2)").pop(0)["datetime"].strip()
        except IndexError:
            purchase_date = None
        useful = int(opinion.select("span[id^='votes-yes']").pop(0).get_text().strip())
        useless = int(opinion.select("span[id^='votes-no']").pop(0).get_text().strip())

        opinion_elements = {
            "opinion_id": opinion_id,
            "author": author,
            "recommendation": recommendation,
            "stars": stars,
            "content": content,
            "pros": pros,
            "cons": cons,
            "purchased": purchased,
            "submit_date": submit_date,
            "purchase_date": purchase_date,
            "useful": useful,
            "useless": useless
        }

        extracted_opinions.append(opinion_elements)
    try:
        next_page = "https://www.ceneo.pl" + \
        page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        next_page = None
    print(next_page)

with open(f".//opinions/{product_id}.json", "w", encoding="UTF-8") as fp:
    json.dump(extracted_opinions, fp, indent=4, ensure_ascii=False)

