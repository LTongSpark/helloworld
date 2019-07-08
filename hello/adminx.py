# -*- coding: utf-8 -*-
import xadmin
from .models import Student, Card, CardDetail,ArticleDetail ,Student1,FileImage
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from xadmin import views


class ControlStudent(object):
    # 显示的字段
    list_display = ('student_id', 'name', 'age', 'score')
    # 搜索条件
    search_fields = ('name',)

    # 每页显示10条
    list_per_page = 10

class MoreInfo(object):
    model = CardDetail

class ControlCard(object):
    list_display = ["card_id", "card_user",'电话','城市', "add_time"]

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]

    def 电话(self,obj):
        return obj.carddetail.tel

    def 城市(self, obj):
        return obj.carddetail.city

# 注册Student表
xadmin.site.register(Student, ControlStudent)

# 注册card表，关联CardDetail
xadmin.site.register(Card, ControlCard)


class ControlActicl(object):
    list_display = ['title', 'body', 'auth']

    #readonly_fields = ['detail']  # 只读字段

    #exclude = ['auth']  # 不显示某个字段

    form_layout =[
        Fieldset('主要信息' ,
                 Row('title' ,'auth'),
                 Row('classify'),
                 css_class ='unsort'),
        Fieldset(('正文内容'),  # Fieldset第一个参数表示区块名称
                 'body',
                 css_class='unsort'
                 ),

        Fieldset(('备注'),
                 Row('detail'),
                 css_class='unsort no_title'  # no_title是不显示区块的title名称
                 ),
        TabHolder(
            Tab('body-raw',
                Field('title', css_class="extra"),
                Field('body'),
                css_class='unsort'
                ),
            Tab('body-json',
                Field('body', )
                ),
            css_class='unsort',
        )
    ]

class StudentAdmin(object):
    list_display = ('student_id', 'name', 'age',)

xadmin.site.register(Student1, StudentAdmin)


xadmin.site.register(ArticleDetail, ControlActicl)


# 全局设置，最好放到adminx.py开头位置
class GlobalSettings(object):
    site_title = "开发平台"         # title内容
    site_footer = "liutongspark@163.com"            # 底部@后面
    # menu_style = "accordion"      # 菜单折叠

    # 自定义菜单
    def get_site_menu(self):
        return [
            {
                'title': '自定义菜单',
                'icon': 'fa fa-bars',       # Font Awesome图标
                'menus':(
                    {
                        'title': 'Card表',
                        'icon': 'fa fa-bug',
                        'url': self.get_model_url(Card, 'changelist')

                    },
                    {
                        'title': 'a发邮件',
                        'icon': 'fa fa-envelope-o',
                        'url': self.get_model_url(Student, 'changelist'),
                    }
                )
            },
            {
                'title': 'Bug统计',
                'icon': 'fa fa-bug',
                'menus':(
                    {
                        'title': 'Bug表',
                        'icon': 'fa fa-bug',
                        'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表

                    },)
            }

        ]


xadmin.site.register(views.CommAdminView, GlobalSettings)

class ThemeSetting(object):
    '''主题设置'''
    enable_themes = True    # 使用主题
    use_bootswatch = True   # bootswatch是一款基于bootstrap的汇集了多种风格的前端UI解决方案

xadmin.site.register(views.BaseAdminView, ThemeSetting)


class ControlFiles(object):
    list_display = ['title', "add_time"]


xadmin.site.register(FileImage, ControlFiles)