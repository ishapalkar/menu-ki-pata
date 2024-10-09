from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, Feedback
from .forms import FeedbackForm
from datetime import date

# Show today's menu with filtering by meal type
def today_menu(request):
    meal_type = request.GET.get('meal', 'breakfast')  # Default to breakfast
    meals = Meal.objects.filter(meal_type=meal_type, date=date.today())
    return render(request, 'menu/today_menu.html', {'meals': meals, 'meal_type': meal_type})

# View for a single meal, showing details and feedback
def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    feedback_list = meal.feedback.all()  # Get all feedback for this meal
    return render(request, 'menu/meal_detail.html', {'meal': meal, 'feedback_list': feedback_list})

# Collect feedback for a specific meal
def add_feedback(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.meal = meal
            feedback.save()
            return redirect('meal_detail', meal_id=meal.id)
    else:
        form = FeedbackForm()
    return render(request, 'menu/add_feedback.html', {'form': form, 'meal': meal})
