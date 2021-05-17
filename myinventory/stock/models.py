from django.db import models

# Create your models here.
class Type(models.Model):
    """A item the user is going to add."""
    Name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      """Return a string representation of the model."""
      return self.Name

class Item(models.Model):
   """Something specific to add to the item category."""
   item = models.ForeignKey(Type, on_delete=models.CASCADE)
   Name = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   
class Meta:
   verbose_name_plural = 'Items'
def __str__(self):
   """Return a string representation of the model."""
   return f"{self.Name[:50]}..."