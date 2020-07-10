from rest_framework import serializers
import uuid
from myapp.models import UserInfo, Project


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # 指定需要序列化的数据
    account = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    linenos = serializers.DateField(required=False)

    class Meta:
        model = UserInfo
        fields = "__all__"
        # extra_kwargs = {
        #     'id': {'required': False}
        # }

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return UserInfo.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """更新，instance为要更新的对象实例"""
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.part_id = validated_data.get('part_id', instance.part_id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.x = validated_data.get('x', instance.x)
    #     instance.y = validated_data.get('y', instance.y)
    #     instance.save()
    #     return instance


class ProjectSerializer(serializers.Serializer):

    class Meta:
        model = Project
        fields = '__all__'
