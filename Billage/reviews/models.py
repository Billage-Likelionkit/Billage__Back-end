from django.db import models


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    send_id = models.ForeignKey('accounts.User', related_name='send_id', on_delete=models.CASCADE, verbose_name='송신자',
                                db_column="send_id")
    receive_id = models.ForeignKey('accounts.User', related_name='receive_id', on_delete=models.CASCADE,
                                   verbose_name='수신자', db_column="receive_id")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='글 작성 시간')
    star = models.IntegerField()
    content = models.TextField(blank=False)

    def __str__(self):
        return self.content