from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, member_id, email, name, phone, password=None):
        if not member_id:
            raise ValueError('must have user member_id')
        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user name')
        if not phone:
            raise ValueError('must have user phone')
        user = self.model(
            email = self.normalize_email(email),
            member_id = member_id,
            name = name,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, member_id, email, name, phone, password=None):
        user = self.create_user(
            email = email,
            password = password,
            member_id = member_id,
            name = name,
            phone = phone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=150, null=False, blank=False, unique=True)
    member_id = models.IntegerField(default='', null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=20, null=False, blank=False)
    phone = models.CharField(default='', max_length=20, null=False, blank=False, unique=True)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정
    USERNAME_FIELD = 'email'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name', 'phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return str(self.member_id)