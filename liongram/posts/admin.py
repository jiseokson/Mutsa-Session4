from django.contrib import admin

from posts.models import Comment, Post

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    # 기본, 자주 사용되는 속성
    list_display = ('id', 'content', 'created_at',) # 모델의 속성명 => admin 페이지 표시
    list_filter = ('created_at',) # 리스트 필터
    search_fields = ('id', 'writer__username',) # 검색 방식
    readonly_fields = ('created_at', )

    inlines = [CommentInline]
    actions = ['make_published'] # 원하는 기능 함수로 만들어서 이용 가능

    # list_editable = ('content',) # 리스트 화면에서 편집

    def make_published(modeladmin, request, queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 삭제'
            item.save()

# admin.site.register(Comment)
