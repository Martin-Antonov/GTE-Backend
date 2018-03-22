import datetime

from rest_framework import serializers

from tree.models import Tree


def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    in_seconds = (dt - epoch).total_seconds()
    return in_seconds * 1000


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = (
            'title',
            'screenshot_url',
            'tree_json',
        )

    def to_representation(self, instance):
        serialized_data = super(TreeSerializer, self).to_representation(instance)
        date_to_use = instance.date.replace(tzinfo=None, microsecond=0)
        date = datetime.datetime.strptime(str(date_to_use), '%Y-%m-%d %H:%M:%S')
        date = date.replace(tzinfo=None)
        serialized_data['date'] = str(unix_time_millis(date))
        return serialized_data
