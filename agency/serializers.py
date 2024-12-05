from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from agency.models import SpyCat, Mission, Target
from agency.services import is_breed_valid


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ["id", "name", "years_experience", "breed", "salary"]

    def validate_breed(self, breed_name: str) -> str:
        if not is_breed_valid(breed_name):
            raise ValidationError(
                "Invalid breed name."
                "You should choose a breed from 'api.thecatapi.com/v1/breeds'"
            )
        return breed_name


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "mission", "name", "country", "notes", "complete"]

    def update(self, instance: Target, validated_data: dict) -> Target:
        # Prevent updating notes if the target is marked as complete
        if instance.complete and "notes" in validated_data:
            raise ValidationError("Notes cannot be updated for a completed target.")
        return super().update(instance, validated_data)


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ["id", "complete", "cat", "targets"]
