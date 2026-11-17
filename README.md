\# CPS 310 Final Project

\# Recipe \& Meal Planner



A Python command-line application for browsing recipes, managing favorite recipes, and planning meals for an entire week.



\## Features



\### Recipe Management

\- List all available recipes.

\- Search recipes by name.

\- Filter recipes by category.

\- View recipe details, including ingredients, servings, and preparation and cooking times.

\- Add and remove favorite recipes.

\- View saved favorite recipes.



\### Weekly Meal Planning

\- Create a 7-day meal plan from Monday through Sunday.

\- Assign a recipe to a selected weekday.

\- View all seven days in the weekly meal plan.

\- Save and load meal plans using JSON files.

\- Keep meal plans saved when the application is closed and restarted.



\### Grocery List

\- Grocery list generation is a planned project feature and has not yet been implemented.



\## Project Files



\- `app.py` — Main application and interactive menu.

\- `recipe\_utils.py` — Recipe, favorites, and meal-planning utility functions.

\- `test\_recipe\_utils.py` — Automated tests for utility functions.

\- `recipes.json` — Recipe data.

\- `config.json` — Application configuration.

\- `requirements.txt` — Python dependencies.



\## Setup



\### Windows



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

python -m pip install -r requirements.txt

```



\### macOS



```bash

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirements.txt

```



\## Run the Application



\### Windows



```powershell

python app.py

```



\### macOS



```bash

python3 app.py

```



\## Run Tests



\### Windows



```powershell

python -m pytest -v

```



\### macOS



```bash

python3 -m pytest -v

```



The project currently has \*\*17 passing automated tests\*\* covering recipe utilities, favorites, and weekly meal planning.



\## Data Files



The application saves user data in local JSON files:



\- `favorites.json` — Saved favorite recipe names.

\- `meal\_plan.json` — Saved weekly meal plan.



These files are generated when the application saves favorites or meal plans.



\## Development Progress



Completed features

