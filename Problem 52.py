#https://newsapi.org/v2/everything?q=tesla&from=2023-05-08&sortBy=publishedAt&apiKey=5011f16d870e4d9283917dc862c65318
import requests
import pyttsx3
def News():
    a = {"Name: ": "Top 100 News",
         "Sort by: ": "Top"}
    url = "Here Fill Your API"

    b = requests.get(url)
    news = b.json()
    article = news["articles"]
    result = []
    for i in article:
        result.append(i["title"])
    for j in range(len(result)):
        print(j, result[j])
    speak = pyttsx3.speak(result)
    print(speak)

if __name__ == '__main__':
    News()
