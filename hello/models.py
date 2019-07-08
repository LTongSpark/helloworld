from django.db import models

# Create your models here.




class text(models.Model):
    name = models.CharField(max_length=20)

class per(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    data = models.DateField(blank=True ,null=True)
    title = models.CharField(max_length=20 ,default="")
    common = models.IntegerField(default=0)

    def __str__(self):
        return self.name

#用户表
class User(models.Model):
    user_name = models.CharField(max_length=30 ,primary_key=True)
    pword = models.CharField(max_length=30)
    emil = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name

class Book(models.Model):
    title = models.CharField(max_length=20 ,verbose_name="标题")
    body =models.TextField(verbose_name="文章")
    auth =models.CharField(max_length=20,verbose_name="作者" ,blank=True ,null=True)

    #创建时间
    create_date = models.DateTimeField(auto_now_add=True ,verbose_name="创建时间")

    #更新 时间
    update_date = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    def __str__(self):
       return self.title

    class Meta:
        verbose_name_plural = "书名"

class Bank(models.Model):
    '''银行信息'''
    bank_name = models.CharField(max_length=50, verbose_name="银行名称")
    city = models.CharField(max_length=30, verbose_name="城市")
    point = models.CharField(max_length=60, verbose_name="网点")

    class Meta:
       verbose_name_plural = '银行卡'

    def __str__(self):
        return self.bank_name

class CardInfo(models.Model):
    '''卡信息'''
    card_id = models.CharField(max_length=30, verbose_name="卡号")
    card_name = models.CharField(max_length=10, verbose_name="姓名")
    info = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="选择银行")
    class Meta:
       verbose_name_plural = '卡号信息'

    def __str__(self):
        return self.card_id


class Auther(models.Model):
    '''作者'''
    name = models.CharField(max_length=10, verbose_name="作者")
    mail = models.CharField(max_length=30, verbose_name="邮箱")
    city = models.CharField(max_length=10, verbose_name="城市")
    class Meta:
       verbose_name_plural = '作者'

    def __str__(self):
        return self.name

class Book1(models.Model):
    '''书籍详情'''
    book_name = models.CharField(max_length=50, verbose_name="书名")
    auth = models.ManyToManyField(Auther, verbose_name="作者")
    class Meta:
       verbose_name_plural = '书籍详情'

    def __str__(self):
        return self.book_name


class Card(models.Model):
    '''银行卡 基本信息'''
    card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
    card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")
    class Meta:
        verbose_name_plural = '银行卡账户'
        verbose_name = "银行卡账户_基本信息"
    def __str__(self):
        return self.card_id

class CardDetail(models.Model):
    '''银行卡 详情信息'''
    card = models.OneToOneField(Card,
                               on_delete=models.CASCADE,
                               verbose_name="卡号"
                                )
    tel = models.CharField(max_length=30, verbose_name="电话", default="")
    mail = models.CharField(max_length=30, verbose_name="邮箱", default="")
    city = models.CharField(max_length=10, verbose_name="城市", default="")
    address = models.CharField(max_length=30, verbose_name="详细地址", default="")

    class Meta:
        verbose_name_plural = '个人资料'
        verbose_name = "账户_个人资料"

    def __str__(self):
        return self.card.card_user

class Student(models.Model):
    '''学生成绩'''
    student_id = models.CharField(max_length=30, verbose_name="学号")
    name = models.CharField(max_length=30, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    score = models.IntegerField(verbose_name="分数")

    class Meta:
        verbose_name = "学生成绩"
        verbose_name_plural = verbose_name

class ArticleClassify(models.Model):
    '''文章分类'''
    n = models.CharField(max_length=30, verbose_name="分类", default="")
    def __str__(self):
        return  self.n

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


class ArticleDetail(models.Model):
    '''文章'''
    title = models.CharField(max_length=30, verbose_name="标题", default="输入你的标题")  # 标题
    classify = models.ForeignKey(ArticleClassify,
                                on_delete=models.CASCADE,
                                related_name="classify_name",
                                verbose_name="文章分类",
                                )

    body = models.TextField(verbose_name="正文", default="输入正文")                # 正文
    auth = models.CharField(max_length=10, verbose_name="作者", default="admin" ,blank=True)   # 作者

    detail = models.TextField(verbose_name="备注", default="添加备注")

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章列表"
        verbose_name_plural = '文章列表'


class Student1(models.Model):
    '''学生表'''
    student_id = models.CharField(max_length=30, verbose_name="学号", default="")
    name = models.CharField(max_length=30, verbose_name="姓名", default="")
    gender_choices = (
        (u'M', u'男'),
        (u'F', u'女'),
    )
    gender = models.CharField(max_length=10,
                              choices=gender_choices,  # 设置性别选项
                              verbose_name="性别",
                              default="")

    age = models.IntegerField(verbose_name="年龄", default="")

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FileImage(models.Model):
    '''上传文件和图片'''
    title = models.CharField(max_length=30, verbose_name="名称", default="")  # 标题
    image = models.ImageField(verbose_name="上传图片", upload_to="up_image", blank=True)
    fiels = models.FileField(verbose_name="上传文件", upload_to="up_file", blank=True)
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "上传文件和图片"
        verbose_name_plural = verbose_name

