
import pymysql
import requests
import re
 

def resp(listURL):
    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'zhao153195',  
        database = 'oa', 
        charset = 'utf8'
    )
 
    cursor = conn.cursor()

    cursor.execute('create table t_movieTOP250(id INT PRIMARY KEY 												auto_increment NOT NULL ,movieName VARCHAR(20) NOT NULL 									,pictrue_address VARCHAR(100))')
 
    try:
   
        for urlPath in listURL:
 
            response = requests.get(urlPath)
            html = response.text
 
            namePat = r'alt="(.*?)" src='
            imgPat = r'src="(.*?)" class='
 
            res2 = re.compile(namePat)
            res3 = re.compile(imgPat)
            textList2 = res2.findall(html)
            textList3 = res3.findall(html)
 
            for i in range(len(textList3)):
                cursor.execute('insert into t_movieTOP250(movieName,pictrue_address) 									VALUES("%s","%s")' % (textList2[i],textList3[i]))
 
        cursor.fetchall()
        conn.commit()
        print("结果已提交")
 
    except Exception as e:
        conn.rollback()
        print("数据已回滚")
    conn.close()
def page(url):
    urlList = []
    for i in range(10):
        num = str(25*i)
        pagePat = r'?start=' + num + '&filter='
        urL = url+pagePat
        urlList.append(urL)
    return urlList
if __name__ == '__main__':
    url = r"https://movie.douban.com/top250"
    listURL = page(url)
    resp(listURL)
