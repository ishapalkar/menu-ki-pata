from django.db import models

# Meal Model
class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    nutrition_info = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.meal_type}) - {self.date}"

# Feedback Model
class Feedback(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.meal.name} - {self.rating}/5"
