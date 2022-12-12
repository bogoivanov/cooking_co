Cooking Coach web application is built using the Django web framework. The application
allows users to view, publish, and comment on recipes and cocktails. By overwriting 
UserManager, the user of the application no longer has a username and an email 
is accepted as a required field.
When you go to the website address, you access the home page, register and log in. 
At home page, user will be able to see information about recipes and cocktails 
as a user under 21 years old.
Users must be at least 16 years old to register on the site. Upon registration,
the user is automatically logged in and redirected to the home page where they can 
view information about recipes and cocktails. Аfter successful registration the user
will receive a welcome email. Аfter successful registration the user will receive a 
welcome email. If the user is under 21 years old, they will only see information about 
non-alcoholic cocktails and recipes on the site. In the navigation bar, the user 
can access the recipes and cocktails, as well as log out from the site.
On the user profile page, they can edit or delete their profile. The number of likes
received by their recipes and cocktails will be calculated. If the user has five or
more likes, they will be able to apply to become a moderator. The user can also create
recipes and cocktails from a draft on this page.
Users can edit their profile by entering their first name, last name, selecting their 
gender, and uploading a profile picture. When editing is complete, the user is redirected
to their details page where they can see their changed profile picture and names. 
Users can also delete their profile, but the recipes and cocktails they have uploaded 
to the site will remain in the database with the user field set to null.
Recipes and cocktails can be created through the navigation bar or on the user profile page. 
Each cocktail or recipe is associated with the logged-in user. Users under 21 years old
must use the main ingredient "non-alcoholic" when creating a cocktail. The user can edit 
and delete the recipes and cocktails they have created. There are forms for likes and comments 
on each recipe. Users can like a recipe, but the owner of the recipe cannot like it.
Users can see a list of all recipes on the site. If the user is under 21, they will not see 
the alcoholic cocktails. From this list, they can go to the details page of a specific cocktail
or recipe and view detailed information, as well as like and comment with other users. 
The site also has a search feature that allows users to search for specific cocktail recipes.
The web application has an admin part where there are superusers and groups of users 
with different levels of access. The "StaffCC" group has full CRUD (create, read, update, delete) 
access, while the "ModeratorsCC" group has CRUD access on cocktails and recipes, comments, and likes.
