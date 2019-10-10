from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    no = models.CharField(max_length=20,verbose_name='编号')   # 长度最大20
    classes_begin_date = models.DateField(default="2019-09-01",verbose_name="开班时间",null=True,blank=True)
    name = models.CharField(max_length=30,verbose_name="姓名")
    gender = models.CharField(max_length=1,choices=(("0","女"),("1","男")),verbose_name="性别")
    age = models.PositiveSmallIntegerField(default=20,verbose_name="年龄") # 无符号比较小的类型
    city = models.CharField(max_length=30,verbose_name="城市")
    native_place = models.CharField(max_length=30,verbose_name="籍贯",null=True,blank=True) # 可为空
    phone = models.CharField(max_length=11,verbose_name="电话")
    qq = models.CharField(max_length=15,verbose_name="QQ",blank=True,null=True)
    business_type = models.CharField(max_length=30,verbose_name="业务类型",blank=True,null=True)
    agent = models.CharField(max_length=30,verbose_name="代理商",blank=True,null=True)
    to_b_type = models.CharField(max_length=30,verbose_name="TP-B类型",blank=True,null=True)
    school_name = models.CharField(max_length=30,verbose_name="学校名称",blank=True,null=True)
    major = models.CharField(max_length=30,verbose_name="专业",blank=True,null=True)
    stu_no = models.CharField(max_length=20,verbose_name="学号",blank=True,null=True)
    other = models.TextField(verbose_name="其他",blank=True,null=True)
    is_delete = models.BooleanField(default=False,verbose_name="是否删除",null=True,blank=True)  # 默认不删除