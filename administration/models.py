from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _


# Create your models here.
class Curator(models.Model):
    class Meta:
        verbose_name = "Куратор (Подразделение)"
        verbose_name_plural = "Кураторы (Подразделения)"

    title = models.CharField(
        max_length=120,
        verbose_name="Куратор"
    )

    def __str__(self):
        return self.title.__str__()


class UserTypes(models.Model):
    class Meta:
        verbose_name = "Тип пользователя"
        verbose_name_plural = "Типы пользователя"

    title = models.CharField(
        max_length=120,
        verbose_name="Тип пользователя",
        help_text="Администратор, Куратор, БПиЭА, Пользователь, Экономист, Спкциалист АСЭЗ, Юрист"
    )

    def __str__(self):
        return self.title.__str__()


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.DO_NOTHING,
    #     verbose_name="Пользователь")
    curator = models.ForeignKey(
        Curator,
        verbose_name="Подразделение (Куратор)",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    # email = models.EmailField()
    # email = models.EmailField(_('email address'), blank=True)
    # name = models.CharField(
    #     max_length=150,
    #     verbose_name="Фамилия, Имя, Отчество"
    # )
    position = models.CharField(
        max_length=200,
        verbose_name="Должность",
        null=True,
        blank=True
    )
    user_type = models.ForeignKey(
        UserTypes,
        verbose_name="Тип пользователя (Пользователь, Администратор, Куратор, Суперпользователь, БПиЭА, Юрист, Экономист, Специалист АСЭЗ)",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    # blocked_status = models.BooleanField(
    #     default=True,
    #     verbose_name="Активный пользователь/Заблокированный"
    # )


class UserActivityJournal(models.Model):
    class Meta:
        verbose_name = 'Журнал действий пользователя'
        verbose_name_plural = 'Журналы действий пользователя'

    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    date_time_of_activity = models.DateTimeField(
        verbose_name="Дата и время работы пользователя в системе",
        auto_now_add=True
    )
    activity = models.CharField(
        max_length=200,
        verbose_name="Действия пользователя в системе",
        blank=True,
        null=True
    )
    clicks = models.PositiveIntegerField(
        verbose_name="Количество кликов пользователя",
        default=0
    )
    activity_system_module = models.CharField(
        max_length=100,
        verbose_name="Раздел системы",
        blank=True
    )

    def __str__(self):
        try:
            return 'Журнал действий пользователя: {0}'.format(self.user)
        except:
            return 'Ошибка в данных'
