from django.db import models
from authentication.models import User


class Income(models.Model):

    SOURSES_OPTIONS = [
        ("SALARY", "SALARY"),
        ("BUSINESS", "BUSINESS"),
        ("SIDE-HUSTLES", "SIDE-HUSTLES"),
        ("OTHERS", "OTHERS"),
    ]

    source = models.CharField(
        choices=SOURSES_OPTIONS, max_length=255, null=True, blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ("-updated_at",)

    def __str__(self):
        return str(self.owner) + "s income"
