from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    send_id = models.ForeignKey('accounts.User', related_name='send_id', on_delete=models.CASCADE, verbose_name='송신자',
                                db_column="send_id")
    recieve_id = models.ForeignKey('accounts.User', related_name='recieve_id', on_delete=models.CASCADE,
                                   verbose_name='수신자', db_column="recieve_id")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='글 작성 시간')
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.TextField(blank=False)

    def __str__(self):
        return self.content