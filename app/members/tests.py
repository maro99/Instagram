
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase, TransactionTestCase

# Create your tests here.
from members.exception import RelationNotExist

User =get_user_model()


class RelationTestCase(TransactionTestCase):  #TestCase에서 바뀜

    def create_dummy_user(self,num):
        # num 에 주어진 개수만큼 유저를 생성 및 리턴.
        return [User.objects.create_user(username=f'u{x}')for x in range(num)]

    def test_follow(self):
        """
        특정  User 가 다른 User를 follow했을 경우, 정상 작동하는경우.

        :return:
        """
        # 임의의 유저 2명 생성 (u1, u2)
        u1 = User.objects.create_user(username='u1')
        u2 = User.objects.create_user(username='u2')

        # u1 이 u2를 follow하도록 함.
        # relation = u1.relations_by_from_user.create(to_user=u2, relation_type='f') # 직관적이지 못해서 아래처럼 해봄.
        relation = u1.follow(u2)



        #u1 의 following에 u2가 포함되어 있는지 확인

        #Relation의 related_query_name 설정 안해줘서 자동으로 lowercase가 된것.
        # u1.following.filter(user=u2).exists()  # user라는 속성 User에 없는데 filter되서 의아했었다.
        # 이렇게 한건 user랑 비교한게 아니라 relation의 from_user와 비교한것.

        # u1.following.filter(pk=u2.pk).exist() #0-->올바른 경우.
        self.assertIn(u2, u1.following)# 테스트에서는 이런식으로함. 포함 안되면 바로 애러뜸 실제러는 in실행한것과같다. .



        #u1의 following_relations에서 to_user가 u2인 Relation이 존재하는지 확인

        #이렇게도 가능.
        self.assertTrue(u1.following_relations.filter(to_user=u2).exists())


        #생성됬었던 relation이 u1.follwoing_relations에 포함되어 있는지.
        self.assertIn(relation, u1.following_relations)


    def test_follow_only_once(self):
        u1 = User.objects.create_user(username='u1')
        u2 = User.objects.create_user(username='u2')

        # #u2로의 follow를 두번 실행한다.
        # u1.follow(u2)
        # u1.follow(u2)#--------------->팔로우 두번하면 안되니까 안되는게 맞다.

        #u2로의 follow를 두번 실행한다.
        u1.follow(u2)

        #2번째 실행에서는 IntegretyError 발생할 것이다.
        with self.assertRaises(IntegrityError):  # with은 block을 만들어서 실행하고
            u1.follow(u2)


        #u1의 follwing이 하나인지 확인
        self.assertEqual(u1.following.count(),1)


    def test_unfollow_if_follow_exist(self):
        u1, u2 = self.create_dummy_user(2)

        # u1이 u2를 follow후 uunfollow 실행
        u1.follow(u2)
        u1.unfollow(u2)

        # u1의 following에 u2가 없어야함.
        self.assertNotIn(u2, u1.following)


    def test_unfollow_fail_if_follow_not_exist(self):
        u1, u2 = self.create_dummy_user(2)

        #아래 코드는 올바르지 않아아햠.(Exception이 발생해야함.)
        with self.assertRaises(RelationNotExist):
            u1.unfollow(u2)