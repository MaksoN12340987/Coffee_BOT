from django.db import models

from config import settings

class CoffeeCup(models.Model):
    """Модель кофе

    Args:
        drink_name (CharField): Название напитка
        preview (ImageField): Фотография
        description (CharField): Описание напитка
        price (DecimalField): Цена напитка
        caloric_of_drink (DecimalField): Калорийность напитка

    Returns:
        _str_: Название напитка
    """    
   
    drink_name = models.CharField(
        verbose_name="Название напитка", 
        max_length=150, 
        default="COFFEE", blank=True
        )
    preview = models.ImageField(
        verbose_name="Фотография", 
        upload_to="preview_cup/", 
        blank=True, default="images/cup-contour.png"
        )
    description = models.CharField(
        verbose_name="Описание напитка", 
        blank=True, default="Без опиcания"
        )
    price = models.DecimalField(
        verbose_name="Цена напитка", 
        max_digits=10, 
        decimal_places=2, 
        help_text="Укажите цену в рублях: 250.00"
        )
    caloric_of_drink = models.DecimalField(
        verbose_name="Калорийность напитка", 
        null=True, blank=True
        )
    publication_flag = models.BooleanField(
        verbose_name="Видно всем"
        )
    creation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    last_update = models.DateTimeField(
        auto_now=True, verbose_name="Дата создания"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Если юзера удалят, поле станет пустым (null)
        null=True,
        blank=True,
        verbose_name="Кем обновлено"
    )
    number_views = models.IntegerField(
        help_text="Количество просмотров",
        verbose_name="Количество просмотров",
        blank=True,
        default=0,
    )
    
    def __str__(self):
        return self.drink_name
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["id", "drink_name"]


class CustomerReview:
    """Модель отзыва покупателей

    Args:
        description (CharField): Текстовый отзыв
        user (CharField): Имя
        photo (ImageField): Фотография

    Returns:
        _str_: Название напитка
    """
    drink = models.ForeignKey(
        CoffeeCup, on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name="feedbacks"
        )
    telegram_id = models.BigIntegerField(
        verbose_name="Telegram ID"
        )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} ★") for i in range(1, 6)],
        verbose_name="Оценка",
        help_text="От 1 до 5 звёзд"
    )
    description = models.CharField(
        verbose_name="Ваш отзыв", 
        blank=True, null=True,
        max_length=1000
        )
    user = models.CharField(
        verbose_name="Имя", 
        blank=True, default="User"
        )
    photo = models.ImageField(
        verbose_name="Фотография", 
        upload_to="preview_cup/", 
        blank=True, null=True
        )
    
    def __str__(self):
        return f"{self.telegram_id}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["id", "telegram_id"]
