from django.db import models
from django.utils import timezone

class User(models.Model):
    ROLES = [
        ("ADMIN", "Admin"),
        ("SECURITY", "Security"),
        ("VISITOR", "Visitor"),
    ]

    userId = models.AutoField(primary_key=True, auto_created=True)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    role = models.CharField(choices=ROLES, max_length=10, null=False)
    password = models.CharField(max_length=200, null=False)

class Visits(models.Model):
    PURPOSE_OF_VISIT = [
        ("AUDITION", "Audition"),
        ("INVITATION", "Invitation"),
        ("FIELD VISIT", "Field visit"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
    ]

    visitId = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, related_name="visiting_user", on_delete=models.CASCADE)
    visit_date = models.DateTimeField(null=False, default=timezone.now)
    check_out_date = models.DateTimeField(null=False)
    purpose_of_visit = models.CharField(choices=PURPOSE_OF_VISIT, max_length=20, null=False)
    accepted = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="PENDING", null=True)
