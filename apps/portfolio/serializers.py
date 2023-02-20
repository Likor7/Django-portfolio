from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    ReadOnlyField,
)
from rest_framework.exceptions import ValidationError

from apps.portfolio.models import Portfolio, Image, Comment


class CreateMixin:
    @property
    def request(self):
        return self._context["request"]

    def create(self, validated_data):
        validated_data.update(
            {
                "created_by": self.request.user,
            },
        )
        return super().create(validated_data)


class ImageSerializer(CreateMixin, ModelSerializer):
    comments = PrimaryKeyRelatedField(many=True, read_only=True)
    created_by = ReadOnlyField(source="created_by.username")

    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "portfolio",
            "comments",
            "created_by",
            "created_at",
            "image",
        )
        read_only_fields = ["created_by", "created_at"]

    def validate_image(self, value):
        if not value.name.lower().endwith((".png", ".jpg", ".jpeg")):
            raise ValidationError("Invalid file type")
        return value


class ImageListSerializer(ModelSerializer):
    created_by = ReadOnlyField(source="created_by.username")
    portfolio = ReadOnlyField(source="portfolio.name")

    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "portfolio",
            "created_by",
            "created_at",
        )
        read_only_fields = ["created_by", "created_at"]


class PortfolioSerializer(ModelSerializer):
    images = ImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio

        fields = [
            "name",
            "description",
            "images",
        ]


class PortfolioListSerializer(ModelSerializer):
    created_by = ReadOnlyField(source="created_by.username")

    class Meta:
        model = Image
        fields = (
            "id",
            "name",
            "description",
            "created_by",
            "created_at",
        )
        read_only_fields = ["created_by", "created_at"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "image",
        ]
