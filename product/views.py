from django.http import Http404
from django.shortcuts import render, get_object_or_404

from product.models import *


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})


# def products_list(request, category_slug):
#     # products = Product.objects.all()
#     # if Category.objects.filter(slug=category_slug).exist():
#     #     raise Http404
#     # products = Product.objects.filter(category_id=category_slug)
#
#     # category = get_object_or_404(Category, slug=category_slug)
#
#     products = get_list_or_404(Product, category_id=category_slug)  # универсально
#     return render(request, 'product/products_list.html', {'products': products})

# def products_list2(request):
#     category_slug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#     return render(request, '', {'products': products})


def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return  render(request,'product/product_details.html', {'product': product})

# TODO добавить детали продукта
# TODO сделать переход из категории в лист продуктов
# TODO переписать на классах

# all() выводит все объекты моделей
# select * from name_of_tab


# filter() фильтрует результаты запроса
# select * from name_of_tab WHERE .....


# exclude(category_id=1) исключает из результата объекты отвечающие условию
# select * from table where category_id != 1;
# exclude(title__startswith='Apple')
# select * from product where title not like 'Apple%'


# order_by - сортировка результатов запроса
# Product.objects.order_by('price');
# Select * from product Order by price ASC;

# Product.objects.order_by('-price');
# Select * from product Order by price BESC;

# Product.objects.order_by('price', 'popularity')
# Select * from product Order by price ASC, popularity ASC;

# Product.objects.order_by('?') - рандомная сортировка


# reverse - меняет порядок результатов с конца в начало


# distinct - исключает повторения
# Product.objects.values_list('category', flat=True).distinct()


# values() - список из словарей
# можно брать только конкретные поля нп values('id', 'title')


# values_list() - представляет объекты в виде кортежа
# тоже можно вытаскивать несколько полей
# Product.objects.values_list('title', flat = True) что бы не оборачивал в кортежи


# none() - пустой queryset


# select_related() - уменьшает нагрузку на бд используется для СВЯЗАННЫХ таблиц (нп через продукт категорию)
# prod = Product.objects.select_related('category').get(id=1)


# defer() - нужен для того что бы указать какие поля не НЕ нужны


# only() - нужен для того что бы указать какие поля НУЖНЫ


# get() - возвращает объект (один)
# ищет по идентефикатору нп get(id=1)
# если нет объекта по условию: -> product.DoesNotExist
# если get находит несколько объектов:  -> Product.MultipleObjectsReturned


# create() - позволяет создавать новые объекты модели


# get_or_crate(условие) - выбирают объект отвечающий условию, если его нет, создает


# update_or_create() - обновляет или создает объекты


# bulk_create() - позволяет создовать несколько объектов


# bulk_update() - позволяет обновлять несколько объектов


# update() - позволяет обновлять все объекты


# count() - возврощает количество результатов queryset


# first(), last() - первое и последние значение
# earliest(), latest() - первое и последние значение по какомуто полю


# exists() - проверяет есть ли в queryset хотя бы один из результатов возвращает True or False


# delete() - удаляет результаты queryset


# explain() - возвращает SQL запрос queryset


"""
field lookups
"""
# сравнение
# gt-> >
# lt-> <
# gte-> >=
# lte-> <=


# текстовые
# startswith='A' -> Like 'A%'
# contains='day' содержит ли строка эту строку
# title__exact = "Milk" -> WHERE title= 'Milk'

# isnull= True проверяет поле ноль можн False написать

# id__in = [1,2,3,4] -> Where id in (1, 2, 3, 4);

# Order.object.filter(data__range=(start_data,stop_date))->
# Where date between start_date and end_date


# MVC - model, wiew, controler


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='products', null=True, blank=True)
#
#     def get_image_url(self):
#         if self.image:
#             return  self.image.url
#         return ''
