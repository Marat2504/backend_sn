from rest_framework import serializers

from .models import Team, TeamMember


# для получения данных о командах
class TeamSerializer(serializers.ModelSerializer):
    is_user_member = serializers.SerializerMethodField()

    def get_is_user_member(self, obj):
        user = self.context.get('user')

        if user:
            return obj.members.filter(user=user).exists()
        return False

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'slug', 'avatar',
                  'count_members', 'captain_id', 'is_user_member']


# для создания новой команды
class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'avatar',
                  'count_members', 'captain_id']


class TeamMemberSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = ['id', 'user', 'team']
        depth = 0



