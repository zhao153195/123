from django.db import models

# Create your models here.
class t_movietop25(models.Model):
    m_name = models.CharField( max_length=50 ,db_column='movieName',verbose_name='电影名称')
    m_picture = models.CharField(max_length=100,db_column='picture_address',verbose_name='电影图片地址')
    
    class Meta:
        db_table ='tb_t_movietop25'
class jd_content(models.Model):
    
    j_name = models.CharField( max_length=255 ,db_column='nickname',verbose_name='昵称')
    j_user = models.CharField(max_length=255,db_column='userLevelName',verbose_name='用户等级')
    j_color = models.CharField( max_length=255 ,db_column='productColor',verbose_name='产品颜色')
    j_size = models.CharField( max_length=255,db_column='productSize',verbose_name='手机版本')
    j_saleValue = models.CharField( max_length=255 ,db_column='saleValue',verbose_name='手机容量')
    j_createiontime = models.CharField( max_length=255 ,db_column='creationTime',verbose_name='出厂时间')
    j_content= models.CharField( max_length=255 ,db_column='content',verbose_name='用户评价')
    j_usercontent = models.CharField( max_length=255 ,db_column='usefulVoteCount',verbose_name='销售数量')
    j_replycontent = models.CharField( max_length=255 ,db_column='replyCount',verbose_name='评论数量')
    
    class Meta:
        db_table ='tb_jd_content'
        
    