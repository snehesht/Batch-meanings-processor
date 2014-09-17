import requests
from lxml import html
import xlsxwriter
import time
# Create a workbook and add a worksheet.
data = [['Word','Meaning'],['','']]
URLS = []

defxpath = '//*[@id="headword"]/div/p/text()'
url = 'http://www.merriam-webster.com/dictionary/'
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}


def getData(word):
    try:
        res = requests.get(url+word, headers=header)
        raw_data = html.fromstring(res.text)
        rawmeaning = raw_data.xpath(defxpath)
        meaning = rawmeaning[0].strip().replace(':','')
        print(meaning)
        return meaning
    except:
        pass

def writexlsx(data):
    row = 0
    col = 0
    workbook = xlsxwriter.Workbook('GRE 333 Wordlist'+str(int(time.time()))+'.xlsx')
    worksheet = workbook.add_worksheet()
    print('Saving the data to the excel sheet ...')
    for word,meaning in (data):
        worksheet.write(row, col,     word)
        worksheet.write(row, col + 1, meaning)
        row += 1
    workbook.close()


def updateList(word,meaning):
    nlist=[]
    nlist.append(word)
    nlist.append(meaning)
    data.append(nlist)

def buildUrls(word):
    builturl = url+word
    print(builturl)
    URLS.append(builturl)


def main():
    #getCurrRow('Start')
    greword = open('GRE 333.txt','r')
    while(1):
        word = greword.readline()
        if word == '':
            writexlsx(data)
            break
#        buildUrls(word.strip('\n'))
        meaning = getData(word)
        updateList(word,meaning)



if __name__=='__main__':
    main()