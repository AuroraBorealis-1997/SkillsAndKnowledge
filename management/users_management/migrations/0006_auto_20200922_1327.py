# Generated by Django 3.1.1 on 2020-09-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0005_auto_20200922_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(max_length=30, null=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.CharField(max_length=30, null=True, verbose_name='反馈时间'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='time',
            field=models.CharField(max_length=30, null=True, verbose_name='关注时间'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.CharField(max_length=30, null=True, verbose_name='点赞时间'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.CharField(max_length=128, null=True, verbose_name='发布内容'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='location',
            field=models.CharField(max_length=128, null=True, verbose_name='定位'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='picture_path',
            field=models.CharField(max_length=128, null=True, verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='post_time',
            field=models.CharField(max_length=30, null=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='moment',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='话题/标签'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='住址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.CharField(max_length=20, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='annual_survey_date',
            field=models.CharField(max_length=30, null=True, verbose_name='年检日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='assessment',
            field=models.CharField(max_length=30, null=True, verbose_name='评定成绩'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='certificate_date',
            field=models.CharField(max_length=20, null=True, verbose_name='发证日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='certificate_num',
            field=models.CharField(max_length=50, null=True, verbose_name='证书编号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=20, null=True, verbose_name='市级区划'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='district',
            field=models.CharField(max_length=20, null=True, verbose_name='县级区划'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='edu_background',
            field=models.CharField(max_length=20, null=True, verbose_name='文化程度'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gym',
            field=models.CharField(max_length=50, null=True, verbose_name='健身地点'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.CharField(max_length=20, null=True, verbose_name='身高/cm'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id_number',
            field=models.CharField(max_length=30, null=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='instructor_class',
            field=models.CharField(max_length=20, null=True, verbose_name='指导员等级'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='instructor_type',
            field=models.CharField(max_length=40, null=True, verbose_name='指导类型'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_instructor',
            field=models.BooleanField(null=True, verbose_name='是否指导员'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='用户名称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(max_length=20, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(max_length=20, null=True, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upload_time',
            field=models.CharField(max_length=30, null=True, verbose_name='上传日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ver_status',
            field=models.CharField(max_length=20, null=True, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='village',
            field=models.CharField(max_length=20, null=True, verbose_name='乡镇'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.CharField(max_length=20, null=True, verbose_name='体重'),
        ),
    ]
