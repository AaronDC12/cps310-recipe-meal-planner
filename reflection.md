\# CPS 310 Final Project Reflection

\## Recipe \& Meal Planner



\### 1. Project Overview



For my CPS 310 final project, I am developing a Recipe \& Meal Planner application using Python. The purpose of the application is to help users browse recipes, save favorite recipes, and organize meals throughout the week.



\### 2. Features Selected



The three features selected for this project are:



1\. Recipe Favorites

2\. 7-Day Meal Planning

3\. Grocery List Generation



\### 3. Features Implemented



I successfully implemented two of the three selected features.



\*\*Recipe Favorites\*\*



Users can add recipes to their favorites, remove recipes from their favorites, and view their saved favorite recipes. Favorite information is stored in a JSON file so it can be loaded again when the application restarts.



\*\*7-Day Meal Planning\*\*



Users can assign recipes to individual days of the week, from Monday through Sunday. The application displays the complete weekly meal plan and saves it in a JSON file. I tested that the meal plan remains available after restarting the application.



\*\*Grocery List Generation\*\*



This feature is planned but has not yet been implemented.



\### 4. GitHub and Development Process



I used Git and GitHub to organize my development work.



I created GitHub Issues to track the three selected features and used separate feature branches to develop the implemented features.



I completed and merged the following pull requests:



\- PR #4: Implement recipe favorites.

\- PR #5: Implement 7-day meal planning.



I also created meaningful commits to document my changes and updated the README to describe the implemented functionality.



\### 5. Testing



I expanded the automated tests using pytest.



The test suite currently contains 17 tests, and all 17 tests pass.



I also manually tested the application by adding a recipe to the weekly meal plan, viewing the seven-day schedule, closing the application, and restarting it to confirm that the saved meal plan loaded correctly.



\### 6. Challenges and Lessons Learned



One important part of this project was learning how to save and load application data using JSON files.



I also gained experience organizing code into reusable utility functions and testing those functions with pytest.



Using Git branches and pull requests helped me organize my work and understand how changes can be developed and merged into the main branch.



\### 7. Future Improvements



The next major feature I plan to implement is grocery list generation based on the recipes in the weekly meal plan.



I would also like to continue improving the application and adding more tests as development progresses.



\### 8. Conclusion



This project has helped me improve my Python programming, debugging, testing, and GitHub workflow skills. I have successfully implemented recipe favorites and weekly meal planning, and I plan to continue developing the remaining grocery list feature.

