

"""CPS 310 Recipe & Meal Planner application."""

from recipe_utils import (
    filter_by_category,
    filter_favorites,
    load_config,
    load_favorites,
    load_recipes,
    save_favorites,
    search_by_name,
    toggle_favorite,
)


def display_recipe(recipe):
    """Display one recipe in a readable format."""
    print(f"\n{recipe['name']}")
    print("-" * len(recipe["name"]))
    print(f"Category: {recipe['category']}")
    print(f"Servings: {recipe['servings']}")
    print(f"Prep time: {recipe['prep_time']} minutes")
    print(f"Cook time: {recipe['cook_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(
            f"- {ingredient['quantity']} "
            f"{ingredient['unit']} {ingredient['name']}"
        )


def list_recipes(recipes):
    """Display a numbered list of recipe names."""
    if not recipes:
        print("\nNo recipes found.")
        return

    print("\nRecipes")
    print("-------")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['name']} ({recipe['category']})")


def choose_recipe(recipes):
    """Prompt the user to select and view a recipe."""
    list_recipes(recipes)
    if not recipes:
        return

    try:
        selection = int(input("\nEnter recipe number: "))
    except ValueError:
        print("Invalid selection.")
        return

    if selection < 1 or selection > len(recipes):
        print("Invalid selection.")
        return

    display_recipe(recipes[selection - 1])


def manage_favorite(recipes, favorites):
    """Allow the user to add or remove a recipe from favorites."""
    list_recipes(recipes)
    if not recipes:
        return favorites

    try:
        selection = int(input("\nEnter recipe number to favorite/unfavorite: "))
    except ValueError:
        print("Invalid selection.")
        return favorites

    if selection < 1 or selection > len(recipes):
        print("Invalid selection.")
        return favorites

    recipe_name = recipes[selection - 1]["name"]
    updated_favorites = toggle_favorite(favorites, recipe_name)

    if recipe_name in updated_favorites:
        print(f"{recipe_name} added to favorites.")
    else:
        print(f"{recipe_name} removed from favorites.")

    return updated_favorites


def main():
    """Run the Recipe & Meal Planner."""
    config = load_config("config.json")
    recipes = load_recipes(config["recipe_file"])
    favorites = load_favorites("favorites.json")

    while True:
        print(f"\n{config['app_title']}")
        print("=" * len(config["app_title"]))
        print("1. List all recipes")
        print("2. Search recipes by name")
        print("3. Filter recipes by category")
        print("4. View recipe details")
        print("5. View favorite recipes")
        print("6. Add or remove a favorite")
        print("7. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            list_recipes(recipes)

        elif choice == "2":
            term = input("Enter recipe name: ").strip()
            list_recipes(search_by_name(recipes, term))

        elif choice == "3":
            category = input("Enter category: ").strip()
            list_recipes(filter_by_category(recipes, category))

        elif choice == "4":
            choose_recipe(recipes)

        elif choice == "5":
            print("\nFavorite Recipes")
            print("----------------")
            favorite_recipes = filter_favorites(recipes, favorites)
            list_recipes(favorite_recipes)

        elif choice == "6":
            favorites = manage_favorite(recipes, favorites)
            save_favorites(favorites, "favorites.json")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()
