from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CHOICE_GENDER=(
        ('m','남성'),
        ('f','여성'),
        ('x','선텍안함'),
    )

    img_profile = models.ImageField(upload_to='user',  blank= True)
    site = models.URLField(blank=True)
    introduce = models.TextField(blank= True)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    relations = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.username

    @property
    def following(self):
        # 내가 follow중인 User Query리턴
        # hint: __in=[<pk list>]
        # user_pk_list = self.relations_by_from_user.filter(relation_type=Relation.RELATION_TYPE_FOLLOW, ).values('to_user')
        # return User.objects.filter(pk__in=user_pk_list)

        # 아래 정의한 property 활용시
        return User.objects.filter(pk__in=self.following_relations.values('to_user'))

    @property
    def followers(self):
        # 나를 follow중인 User Query리턴
        # hint: __in=[<pk list>]
        # user_pk_list = self.relations_by_to_user.filter(relation_type=Relation.RELATION_TYPE_FOLLOW, ).values('from_user')
        # return User.objects.filter(pk__in=user_pk_list)

        # 아래 정의한 property 활용시
        return User.objects.filter(pk__in=self.follower_relations.values('to_user'))


    @property
    def following_relations(self):
        #내가 follow 중인 Relation Query리턴
        return self.relations_by_from_user.filter(
            relation_type=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def follower_relations(self):
        # 나를 follow 중인 Relation Query리턴
        return self.relations_by_to_user.filter(
            relation_type=Relation.RELATION_TYPE_FOLLOW,
        )

    @property
    def block_relations(self):
        # 내가 block 중인 Relation Query리턴
        return self.relations_by_from_user.filter(
            relation_type=Relation.RELATION_TYPE_BLOCK,
        )


class Relation(models.Model):
    """
    User간의 MTM연결 중계테이블

    """
    RELATION_TYPE_BLOCK='b'
    RELATION_TYPE_FOLLOW='f'
    CHOICES_RELATION_TYPE =(
        (RELATION_TYPE_BLOCK,'Block'),
        (RELATION_TYPE_FOLLOW,'Follow'),
    )

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    relation_type = models.CharField(max_length=1, choices=CHOICES_RELATION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'From {from_user} to {to_user} ({type})'.format(
            from_user=self.from_user.username,
            to_user=self.to_user.username,
            type=self.get_relation_type_display(),
        )