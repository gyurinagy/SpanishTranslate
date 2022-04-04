from bs4 import BeautifulSoup
import requests

# READING THE WORDS AND CREATING A LIST FOR THEM
def readEnglishWords():
    list = []
    with open("englishWords.txt","r") as file:
        for word in file:
            list.append(str(word).strip())
    
    return list

def souping(doc = "index.html"):
    return BeautifulSoup(doc,"html.parser")

# CREATING DICTIONARY
def translateToSpanish(list):
    spanishList = []
    baseUrl = "https://www.spanishdict.com/translate/"

    for item in list:
        url = baseUrl + item + "?langFrom=en"

        result = requests.get(url)
        doc = souping(result.text)

        translatedWords = doc.findAll("div", {"class":"_2qDMaLCj"})
    
        spanishContainer = []
        for container in translatedWords:
            spanishContainer.append(container.a.text)

        spanishList.append(spanishContainer)
    return spanishList

def main():
    englishWords = readEnglishWords()
    spanishWords = translateToSpanish(englishWords)

    for engWords, esWords in zip(englishWords,spanishWords):
       print(engWords,"\t - ",", ".join(esWords))

main()