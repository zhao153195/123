import requests
import json
import pymysql


comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

def jd(page):
    params = {
        'productId': 100000287113,  # 商品id。先写死 苹果手机。
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': 10,}

    headers = {
        'cookie': '__jdu=441250461; shshshfpa=61e55552-648f-19b3-f94e-74af56c80577-1540868662; shshshfpb=14cffa664eb9f4dcdb094ae8124b18c67f05706449652a93c5bd7ca366; unpl=V2_ZzNtbUYFRB10DkdSfUpUBmJQEVQRABdBIltPBygYWQc0UEcKclRCFXwURldnGlsUZwoZWUtcRxxFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2UX4ZXwFmBhVdcmdEJUU4QVBzH1wHVwIiXHIVF0l3CUVccxsRAGIDEVlDUkQVRQl2Vw%3d%3d; user-key=19f517d4-e5b9-4050-973b-282cce5bded7; cn=0; PCSYCityID=412; pinId=4_yKQzpUlXqM2lDl2pm8BbV9-x-f3wj7; pin=jd_4cc39be9ba1d3; unick=%E6%B3%AA%E4%B8%8E%E5%8D%83%E5%B9%B4qw; _tp=yHY%2FDbFEWXtWZug5IdeQVzG%2FTYEzt0y05e835F9W%2Bvc%3D; _pst=jd_4cc39be9ba1d3; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5c6907077b924b28bfeefb8bb043bbdf|1545822683377; 3AB9D23F7A4B3C9B=ONUXFVMELCFAT7S5L3XFFX6K4AWTPC2MEWJD7T5YP4G2Z536N6FSAM5RJL7T5D5QGKKWZOOM3JFUDZIIAIQORWUQKI; shshshfp=f6f66b7252d2ff2e57b3342ca8e42931; _gcl_au=1.1.252681836.1545966102; __jdc=122270672; __jda=122270672.441250461.1540868654.1545966102.1545981780.6; wlfstk_smdl=5b735rpz8djcb2brwxx6kxs7xt37lqnr; TrackID=1AiTfnDoDxNO7qM13mm_YHzwJo-gMD6TE6yJm2FB6JXLycoyhzy0ra_N2N8RjoetxN6qSg8c0iDPyWBGXNoKTH1LztGZIVFBIhvBRZWLLshU; thor=2E52F8EEC3E4E823A830758D619F3B7F5B3626F79FDAEC421FF56F474F35C74F328331A461149D1807B99B88F0D3D98C71AD840B9786F682E1BCE84D33421004888F934A262D0942C72089396BADCCF90E541A1BCB2428B76C6D1FE3FE5461389F79690BD288E6FD252DDAA1C257B626F70DC0D70B4BD06072317F21F0F63711ECF7626C7655AD7C2050561ABE5C80B07F6D0B7D64BF160AB5ED6CD690E13573; ceshi3.com=103; shshshsID=bba5e89c5d1f8a1bf4d068a71e63094b_4_1545982229264; __jdb=122270672.10.441250461|6.1545981780',
        'referer': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fitem.jd.com%2F100000287113.html%23comment',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    comment_resp = requests.get(url=comment_url, params=params,headers=headers)
    comment_str = comment_resp.text
    comment_dict = json.loads(comment_str)
    comments = comment_dict['comments']
    return comments

def jd_sql(page):
    #保存内容到mysql库里
    db = pymysql.connect(host='localhost',user='root',password='zhao153195',db='oa',charset='utf8')
    cursor = db.cursor()
    sql_table = """CREATE TABLE if not exists  jd_content(
                     id  CHAR(20) NOT NULL,
                     nickname  CHAR(20),
                     userLevelName CHAR(20),  
                     productColor CHAR(10),
                     productSize CHAR(10),
                     saleValue CHAR(10),
                     creationTime CHAR(30),
                     content text,
                     usefulVoteCount CHAR(10),
                     replyCount CHAR(10)  
                      )"""
    cursor.execute(sql_table)
    db.commit()
    if page==0:
        delete_table = """DELETE FROM jd_content"""
        cursor.execute(delete_table)
        db.commit()
    #传入值
    comments = jd(page)

    for comment in comments:
        value = (
        comment['id'], comment['nickname'], comment['userLevelName'], comment['productColor'], comment['productSize'],
        comment['productSales'][0]['saleValue'], comment['creationTime'], comment['content'],
        comment['usefulVoteCount'], comment['replyCount'])
        # print(value)
        sql_insert = """INSERT INTO jd_content VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (value)
        try:
            # 执行sql语句
            cursor.execute(sql_insert)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
    cursor.close()
    db.close()


for page in range(30):
    print(f'正在爬取第{page+1}页···')

    jd_sql(page)
    print(f'爬取第{page+1}页成功···')

