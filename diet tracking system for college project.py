class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

class Meal:
    def __init__(self, name):
        self.name = name
        self.foods = []
        self.calories = 0

    def add_food(self, food, serving_size):
        self.foods.append((food, serving_size))
        self.calories += food.calories * serving_size

class DietTracker:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def get_total_calories(self):
        return sum([meal.calories for meal in self.meals])

# example usage
if __name__ == "__main__":
    diet_tracker = DietTracker()

    # create some foods
    apple = Food("Apple", 90)
    chicken_breast = Food("Chicken Breast", 200)
    brown_rice = Food("Brown Rice", 206)

    # create some meals and add foods to them
    breakfast = Meal("Breakfast")
    breakfast.add_food(apple, 1)
    diet_tracker.add_meal(breakfast)

    lunch = Meal("Lunch")
    lunch.add_food(chicken_breast, 6)
    lunch.add_food(brown_rice, 1)
    diet_tracker.add_meal(lunch)

    # get the total number of calories for the day
    total_calories = diet_tracker.get_total_calories()
    print(f"Total calories for the day: {total_calories}")
