from django.contrib import auth
from django.db import models


class Publisher(models.Model):
    """Компания, издающая книги."""
    name = models.CharField(max_length=50, help_text="Название издательства.")
    website = models.URLField(help_text="Сайт издательства.")
    email = models.EmailField(help_text="Адрес электронной почты издателя.")

    def str(self):
        return self.name


class Book(models.Model):
    """Опубликованная книга."""
    title = models.CharField(max_length=70, help_text="Название книги.")
    publication_date = models.DateField(verbose_name="Дата публикации книги.")
    isbn = models.CharField(max_length=20, verbose_name="Номер ISBN книги.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def str(self):
        return self.title


class Contributor(models.Model):
    """Вклад в создание книги, например, автор, редактор, соавтор."""
    first_names = models.CharField(max_length=50, help_text="Имя или имена вкладчика.")
    last_names = models.CharField(max_length=50, help_text="Фамилия или имена вкладчика.")
    email = models.EmailField(help_text="Контактный адрес электронной почты плательщика.")

    def str(self):
        return self.first_names


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices): AUTHOR = "AUTHOR", "Автор"

    CO_AUTHOR = "CO_AUTHOR", "Соавтор"
    EDITOR = "EDITOR", "Редактор"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Роль, которую этот автор сыграл в книге.", choices=ContributionRole.choices,
                            max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book that this review is for.")
