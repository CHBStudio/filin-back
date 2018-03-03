from rest_framework import serializers

from app.models import Photo


class ProductServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=1000, required=True)
    link = serializers.CharField(max_length=1000, required=True)
    description = serializers.CharField(max_length=1000, required=True)
    phone = serializers.CharField(max_length=1000, required=True)
    housing = serializers.IntegerField(required=False)
    floor = serializers.IntegerField(required=False)
    tags = serializers.SerializerMethodField('get_tagslist')

    def get_tagslist(self, obj):
        tags = obj.tags.all()
        return ProductServiceSerializer(tags, many=True).data


class LeaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    main_photo = serializers.SerializerMethodField('get_mediaphoto')
    square = serializers.FloatField(required=True)
    cost = serializers.IntegerField(required=True)
    floor = serializers.IntegerField(required=True)
    housing = serializers.IntegerField(required=False)
    function = serializers.CharField(max_length=255, required=True)
    show = serializers.BooleanField()
    order = serializers.IntegerField(required=False)
    photos = serializers.SerializerMethodField('get_photos')

    def get_mediaphoto(self, obj):
        if obj.main_photo:
            return obj.main_photo.url[1:]
        return None

    def get_photos(self, obj):
        photos = Photo.objects.filter(lease=obj)
        if len(obj.photos) > 0:
            return [ph.photo for ph in photos]
