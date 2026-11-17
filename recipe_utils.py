
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
