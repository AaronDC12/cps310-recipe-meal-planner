
"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]



"""Utility functions for the Recipe & Meal Planner."""

import json


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]


def load_favorites(filename):
    """Load favorite recipe names from a JSON file."""
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_favorites(favorites, filename):
    """Save favorite recipe names to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(favorites, file, indent=2)


def toggle_favorite(favorites, recipe_name):
    """Add a recipe to favorites or remove it if already favorited."""
    updated_favorites = favorites.copy()

    if recipe_name in updated_favorites:
        updated_favorites.remove(recipe_name)
    else:
        updated_favorites.append(recipe_name)

    return updated_favorites


def filter_favorites(recipes, favorites):
    """Return only recipes whose names are in the favorites list."""
    return [
        recipe
        for recipe in recipes
        if recipe["name"] in favorites
    ]


def load_meal_plan(filename):
    """Load a saved weekly meal plan from a JSON file."""
    try:
        with open(filename, encoding="utf-8") as file:
            meal_plan = json.load(file)
    except FileNotFoundError:
        meal_plan = {}

    return {
        day: meal_plan.get(day)
        for day in WEEKDAYS
    }


def save_meal_plan(meal_plan, filename):
    """Save the weekly meal plan to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(meal_plan, file, indent=2)


def assign_meal(meal_plan, day, recipe_name):
    """Assign a recipe to a day of the week."""
    day = day.capitalize()

    if day not in WEEKDAYS:
        raise ValueError("Day must be a valid weekday.")

    updated_plan = meal_plan.copy()
    updated_plan[day] = recipe_name
    return updated_plan


def display_meal_plan(meal_plan):
    """Return a readable list of the week's planned meals."""
    return [
        (day, meal_plan.get(day))
        for day in WEEKDAYS
    ]
