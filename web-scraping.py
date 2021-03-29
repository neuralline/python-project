import requests
from bs4 import BeautifulSoup
import pandas as pd


print("Python web scraping")

questionList = []


def getQuestions(tag, page):
    url = f"https://stackoverflow.com/questions/tagged/{tag}?tab=active&page={page}&pagesize=50"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    questions = soup.find_all("div", {"class": "question-summary"})

    for item in questions:
        question = {
            "title": item.find("a", {"class": "question-hyperlink"}).text,
            "link": "https://stackoverflow.com"
            + item.find("a", {"class": "question-hyperlink"})["href"],
            "votes": int(item.find("span", {"class": "vote-count-post"}).text),
            "date": item.find("span", {"class", "relativetime"})["title"],
        }
        questionList.append(question)
    return


for x in range(1, 3):
    getQuestions("python", x)

dataFrame = pd.DataFrame(questionList)

print(dataFrame.head())