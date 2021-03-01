from django.contrib.auth import get_user_model
from rest_framework import serializers

from edavids.newletter.models import Newsletter, Subscriber

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["subject", "contents", "created_at", "updated_at"]

        extra_kwargs = {
            "url": {"view_name": "api:newsletter-detail"}
        }

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ["email"]

        extra_kwargs = {
            "url": {"view_name": "api:subscriber-detail"}
        }
