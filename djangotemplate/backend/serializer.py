from rest_framework import serializers
from backend.models import *

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostModel
    fields = ("title", "description", "comments", "classTags",
              "schoolTags", "areaTags", "author",
              "date_submitted", "id")