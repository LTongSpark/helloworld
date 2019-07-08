from django.contrib import admin
from hello.models import User,per,Book ,Bank ,CardInfo ,Book1 ,Auther ,Card,CardDetail


# admin.py
admin.site.site_header = 'xx 项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name','pword','emil']
    search_fields = ['user_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'auth','create_date','update_date']
    search_fields = ['title']
    #按字段排序
    ordering = ['-create_date']
    #可编辑的字段
    list_editable = ['auth']
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ['title', 'body']

    # 过滤器
    list_filter = ['auth', 'title']
    #分页
    list_per_page = 10

    # 时间分层
    date_hierarchy = 'create_date'

@admin.register(Bank)
class ControlBank(admin.ModelAdmin):
    # 显示的字段
    list_display = ["bank_name", "city", "point"]

@admin.register(CardInfo)
class ControlCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ["card_id", "card_name", "info"]


class ControlAuther(admin.ModelAdmin):
    # 显示的字段
    list_display = ["name", "city", "mail"]

class ControlBook(admin.ModelAdmin):
    # 显示的字段
    list_display = ["book_name", "作者"]

    # 定义一个方法，遍历book的auth，然后用列表返回
    def 作者(self, obj):
        return [a.name for a in obj.auth.all()]

admin.site.register(Auther, ControlAuther)
admin.site.register(Book1, ControlBook)


class MoreInfo(admin.StackedInline):
    model = CardDetail


@admin.register(Card)
class ControlCard(admin.ModelAdmin):
    list_display = ["card_id", "card_user", "add_time"]

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]


