from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User =get_user_model()


class RelationTestCase(TestCase):
    def test_follow(self):
        """
        특정  User 가 다른 User를 follow했을 경우, 정상 작동하는경우.

        :return:
        """
        # 임의의 유저 2명 생성 (u1, u2)
        u1 = User.objects.create_user(username='u1')
        u2 = User.objects.create_user(username='u2')

        # u1 이 u2를 follow하도록 함.
        relation = u1.relations_by_from_user.create(to_user=u2, relation_type='f')



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