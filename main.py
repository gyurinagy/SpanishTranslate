import urllib.request
import bs4 as bs

# READING THE WORDS AND CREATING A LIST FOR THEM
def readingEnglist():
    list=[]
    file = open("englishWords.txt","r")
    for word in file:
        list.append(str(word).strip())
    file.close()
    return list

# CREATING DICTIONARY
def spanishTranslate(list):
    spanish_list=[]
    for item in list:
        base_url = "https://www.spanishdict.com/translate/"
        base_url += item

        source = urllib.request.urlopen(base_url)
        client = source.read()
        soup = bs.BeautifulSoup(client, 'html.parser')
        source.close()

        translates = soup.findAll("div",{"class":"_2u6CgGQs"})

    
        spanish_container = []
        for container in translates:
            spanish_container.append(container.a.text)
        spanish_list.append(spanish_container)
    return spanish_list

    #     # WE ONLY WANT TO READ THE ENGLISH - SPANISH

    #     if len(spanish)==1:
    #         containers = spanish[0].findAll("div", {"id": "quickdef1-en"})
    #     else:
    #         containers = soup.findAll("div", {"class": "quickdefWrapper--HELyO"})     



def main():
    english_list = readingEnglist()
    spanish_list = spanishTranslate(english_list)

    for a in spanish_list:
        print(a)

main()