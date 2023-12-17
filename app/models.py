from django.db import models

TYPE_CHOICES = [
    ("М", "Мужская"),
    ("Ж", "Женская"),
    ("Д", "Детская"),
]


class Categories(models.Model):
    name = models.CharField(verbose_name="Наименование",
                            null=False,
                            blank=False,
                            max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategories(models.Model):
    name = models.CharField(verbose_name="Наименование",
                            max_length=200,
                            null=False,
                            blank=False
                            )
    category = models.ForeignKey(Categories,
                                 verbose_name="Категория",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Services(models.Model):
    ordering = ["subcategory", "name"]
    name = models.CharField(max_length=300,
                            verbose_name="Наименование",
                            null=False,
                            blank=False
                            )

    price = models.IntegerField(verbose_name="Стандартная цена",
                                null=False,
                                blank=False,
                                )
    top_price = models.IntegerField(verbose_name="Топ цена",
                                    null=False,
                                    blank=False
                                    )
    subcategorу = models.ForeignKey(SubCategories,
                                    verbose_name="Подкатегория",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)
    type = models.CharField(max_length=1,
                            choices=TYPE_CHOICES,
                            verbose_name="Тип",
                            null=True,
                            blank=True
                            )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Team(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Фамилия/имя",
                            null=False,
                            blank=False
                            )
    post = models.CharField(max_length=70,
                            verbose_name="Должность",
                            )
    isTop = models.BooleanField(verbose_name="Топ",
                                null=False,
                                blank=False,
                                default=False)
    text = models.TextField(verbose_name="Описание")
    photo = models.ImageField(verbose_name="Фото",
                              upload_to='photos/%Y/%m/%d/',
                              null=False,
                              blank=False
                              )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'

