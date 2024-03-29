# Generated by Django 2.0.6 on 2019-06-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jd_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_name', models.CharField(db_column='nickname', max_length=255, verbose_name='昵称')),
                ('j_user', models.CharField(db_column='userLevelName', max_length=255, verbose_name='用户等级')),
                ('j_color', models.CharField(db_column='productColor', max_length=255, verbose_name='产品颜色')),
                ('j_size', models.CharField(db_column='productSize', max_length=255, verbose_name='手机版本')),
                ('j_saleValue', models.CharField(db_column='saleValue', max_length=255, verbose_name='手机容量')),
                ('j_createiontime', models.CharField(db_column='creationTime', max_length=255, verbose_name='出厂时间')),
                ('j_content', models.CharField(db_column='content', max_length=255, verbose_name='用户评价')),
                ('j_usercontent', models.CharField(db_column='usefulVoteCount', max_length=255, verbose_name='销售数量')),
                ('j_replycontent', models.CharField(db_column='replyCount', max_length=255, verbose_name='评论数量')),
            ],
            options={
                'db_table': 'tb_jd_content',
            },
        ),
        migrations.CreateModel(
            name='t_movietop25',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(db_column='movieName', max_length=50, verbose_name='电影名称')),
                ('m_picture', models.CharField(db_column='picture_address', max_length=100, verbose_name='电影图片地址')),
            ],
            options={
                'db_table': 'tb_t_movietop25',
            },
        ),
    ]
