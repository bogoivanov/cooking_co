Cooking coach – Django web framework
Requirements for this project are in requirements.txt file.
In this web application, you can view and publish recipes and cocktails, and to comment and like them.
– Users and registration
By overwriting the UserManager, the user of the application no longer has a username, and an email is accepted as a required field.
If the user has a registration, he can log in. When registering, he must use an email, two passwords and date of birth. If a date of birth is entered and the user is at least 16 years of age, it will have a calculated attribute ‘age’. Otherwise, it will not be able to register. Upon registration, the user logs in automatically and redirect to the home page, where he will receive information about recipes and cocktails. If the user is under 21 years old, he will only see information about the non-alcoholic cocktails and recipes on the site. In the navigation bar you will get access to the recipes and cocktails. There will also be an option to log out from there.
– User details
When the user enters their profile page they will have the option to edit or delete their profile. On this page, the number of likes received by his recipes and cocktails will be calculated. When he has five or more likes, he will be able to apply to be a moderator. After the field with his data, if there are no created recipes and cocktails, he will be able to create from a draft. When there are created, you will see their number and they will be listed. For easy adding, after the listed cocktails there will be a draft to create a cocktail or recipe.
– Edit profile
When a users goes to edit their profile, they must enter their first name, last name, select their gender, and upload a profile picture that will replace the user's default image. When editing is complete, you will be redirect to the details page where you will see your changed profile picture and names.
- Delete profile
When the users goes to delete profile there will be an option to cancel and return to their detail page. If he deletes his profile, all the recipes and cocktails he has uploaded to the site will remain in the database, but the user field will be set to null.
– Create recipes and cocktails
Recipes and cocktails can be created through the navigation from Create recipe and Create cocktail, and also through the user profile. Each cocktail or recipe will be associated with the logged in user. On create, you must enter the name of the recipe or cocktail, the main ingredient, additional ingredients and a photo. When the user is under 21 years of age and wants to create a cocktail, his main ingredient will be "non-alcoholic".
The user will be able to edit and delete the recipes and cocktails created by him. There are likes and comments forms for each recipe. When you go to the details of a given cocktail or recipe, there will be a heart that will count the likes to the corresponding recipe. If the user is the owner of the recipe they will not be able to like it. The likes of other users will accumulate there. A user can only like a given recipe once. There will also be a comments where, the owner of the recipe will be able to comment with other users.
– All recipes and All cocktails
Users logged in will be able to see a list of all recipes. When user is under 21 will not see the alcoholic cocktails. From this list with recipes and cocktails, they can go to the corresponding cocktail or recipe via the ‘Details’ button. There they will get detailed information about the recipe and will be able to like and comment with other users.
– Search
When the user goes to ‘Search’ page he will see all the cocktail recipes or only non-alcoholic if he is not 21 years old. It will list cocktail recipes that match the search.
