from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=127)
    years_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=127)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Mission(models.Model):
    complete = models.BooleanField(default=False)
    cat = models.OneToOneField(
        SpyCat, null=True, blank=True, on_delete=models.CASCADE, related_name="missions"
    )

    def __str__(self):
        return f"Mission #{self.id}"


class Target(models.Model):
    mission = models.ForeignKey(
        Mission, on_delete=models.CASCADE, related_name="targets"
    )
    name = models.CharField(max_length=127)
    country = models.CharField(max_length=127)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=True)

    def __str__(self):
        return self.name
