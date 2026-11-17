

"""Tests for the Recipe & Meal Planner."""

import json
import pytest

from recipe_utils import (
    WEEKDAYS,
    assign_meal,
    display_meal_plan,
    filter_by_category,
    filter_favorites,
    load_config,
    load_favorites,
    load_meal_plan,
    load_recipes,
    save_favorites,
    save_meal_plan,
    search_by_name,
    toggle_favorite,
)


def test_search_by_name_finds_partial_match():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "chicken")
    assert result == [{"name": "Chicken Alfredo", "category": "Dinner"}]


def test_search_by_name_is_case_insensitive():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "SMOOTHIE")
    assert result == [{"name": "Berry Smoothie", "category": "Snack"}]


def test_search_by_name_returns_empty_list_when_no_match():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert search_by_name(recipes, "pizza") == []


def test_filter_by_category_returns_matching_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]
    result = filter_by_category(recipes, "Dinner")
    assert result == [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]


def test_filter_by_category_is_case_insensitive():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert filter_by_category(recipes, "dinner") == [
        {"name": "Chicken Alfredo", "category": "Dinner"}
    ]


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "app_title": "Test Planner",
                "recipe_file": "recipes.json",
                "default_servings": 2,
            }
        ),
        encoding="utf-8",
    )
    result = load_config(config_file)
    assert result["app_title"] == "Test Planner"
    assert result["default_servings"] == 2


def test_load_recipes_reads_json(tmp_path):
    recipe_file = tmp_path / "recipes.json"
    sample = [
        {
            "name": "Test Recipe",
            "category": "Lunch",
            "servings": 2,
            "prep_time": 5,
            "cook_time": 10,
            "ingredients": [],
        }
    ]
    recipe_file.write_text(json.dumps(sample), encoding="utf-8")
    assert load_recipes(recipe_file) == sample


def test_load_favorites_returns_empty_list_when_file_missing(tmp_path):
    favorites_file = tmp_path / "favorites.json"
    assert load_favorites(favorites_file) == []


def test_save_and_load_favorites(tmp_path):
    favorites_file = tmp_path / "favorites.json"
    favorites = ["Chicken Alfredo", "Berry Smoothie"]

    save_favorites(favorites, favorites_file)

    assert load_favorites(favorites_file) == favorites


def test_toggle_favorite_adds_recipe():
    favorites = ["Chicken Alfredo"]
    result = toggle_favorite(favorites, "Berry Smoothie")
    assert result == ["Chicken Alfredo", "Berry Smoothie"]


def test_toggle_favorite_removes_recipe():
    favorites = ["Chicken Alfredo", "Berry Smoothie"]
    result = toggle_favorite(favorites, "Chicken Alfredo")
    assert result == ["Berry Smoothie"]


def test_filter_favorites_returns_only_favorite_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]
    result = filter_favorites(recipes, ["Berry Smoothie", "Tomato Pasta"])
    assert result == [
        {"name": "Berry Smoothie", "category": "Snack"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]


def test_load_meal_plan_returns_empty_week_when_file_missing(tmp_path):
    plan_file = tmp_path / "meal_plan.json"

    result = load_meal_plan(plan_file)

    assert result == {day: None for day in WEEKDAYS}


def test_save_and_load_meal_plan(tmp_path):
    plan_file = tmp_path / "meal_plan.json"
    plan = {day: None for day in WEEKDAYS}
    plan["Monday"] = "Chicken Alfredo"
    plan["Tuesday"] = "Berry Smoothie"

    save_meal_plan(plan, plan_file)

    assert load_meal_plan(plan_file) == plan


def test_assign_meal_updates_selected_day():
    plan = {day: None for day in WEEKDAYS}

    result = assign_meal(plan, "Monday", "Chicken Alfredo")

    assert result["Monday"] == "Chicken Alfredo"
    assert result["Tuesday"] is None


def test_assign_meal_rejects_invalid_day():
    plan = {day: None for day in WEEKDAYS}

    with pytest.raises(ValueError):
        assign_meal(plan, "Funday", "Chicken Alfredo")


def test_display_meal_plan_includes_all_seven_days():
    plan = {day: None for day in WEEKDAYS}
    plan["Monday"] = "Chicken Alfredo"

    result = display_meal_plan(plan)

    assert len(result) == 7
    assert result[0] == ("Monday", "Chicken Alfredo")
    assert result[1] == ("Tuesday", None)
