from django.contrib import admin, messages
from django.contrib.auth.models import User
from .models import Movie, Director
from django.db.models import QuerySet


# Register your models here.
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтер по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 59 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gt=40).filter(rating__lt=60)
        if self.value() == 'от 59 до 79':
            return queryset.filter(rating__gt=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gt=79)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть'
        if movie.rating < 70:
            return 'Разок можно посмотреть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топ'

    @admin.action(description='Установить валюту в долларах')
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        count_update = queryset.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновленно {count_update} записей', messages.ERROR)
