# RECIPE-CONNECT
A recipe application designed for users to share their recipes to the world. A user can register an account and create, edit and upload recipes for the world to see.
The user can build and edit long ingredient and instruction lists at ease without having to restart each. The user can add description and image values to their recipe.

A user can search recipes by cuisine, ingredient and allergen exclusion, in which will return the most popular, most viewed and most recent items first. 
With a special drop down box system, a user can view recipe summaries of each found result before going to a separate page to view it in full, making it easier to find what they want.
A user can also view bar charts under categories allergens, ingredients, cuisine and country of origin.
 
## UX

### User Stories

As a user I want to be able to .. 

- Create a user user account and be able to use my username to login into a profile database.
- be able to 
    - create, edit and view my recipes upon loging in to the application.
    - add name, cuisine, description, image, ingredients, allergens, instruction details to the recipe upon creating them through a recipe form.
    - view a profile page that shows the list of recipes I have built. 
    - view all details of each recipe from the recipe list, so I don't have to relocate to an individual recipe page.
    - delete recipes from the profile page, and have the recipe list reloaded upon deletion showing the recipe has been removed
    - be relocated to an edited form when deciding to edit a recipe, in which shows various recipes details as values of inputs and lists of individual data, in which I will be able to change all of it.
- from both from both the recipe creation and editing forms
    - I want to be alerted when required fields are missing.
    - I want to be able to 
        - add and delete ingredients to/from a collection, in which each item can show the name, amount and associated allergens of each ingredient.
        - add, delete and edit individual instructions, in which I can create a clear adaptable number ordered list of instructions.
- I want to be able to search multiple recipes from various users, in which will return them as list and will show the most popular recipes as a first primary, most viewed as a second primary, and most recently updated as a third primary. 
- I don't need to login when searching all recipes.
- I will atleast be able to view a summary of key recipe details from each search result, by clicking on each found recipe item, 
- The item summary will show the recipe name, image, cuisine, upvotes, views, ingredients, allergens, description, user who created it and her/his country of origin.
- Upon searching recipes, I can create a search query, in which will have the options of including a recipe cuisine, ingredient aswell the option of excluding an allergen from the query.
- The search query will not be completely strict and will only return (or exclude) results that contain the text in my query.
- From each found recipe item, I can relocate to an individual page of the recipe, in which shows all the recipe's details. If I am logged into the application, I have the option to give the recipe an upvote from the individual page. If I have already upvoted the recipe, the recipe page will tell me.
- I want to be able to view bar chart summaries of 5 of the most found words in different categories. These categories will be cuisine, ingredients, allergens, cuisine and country of origin of the users.

### Design and Inspiration

- For design I looked at multiple recipe websites for design inspiration, while keeping in mind I wanted to keep the design more simple.
- I found that most of the websites had a white or bright yellow backgound. I didn't like this color scheme, because I always found with my past applications, that bright backgrounds are not favoured.
- So from a safe stance I went with a darker blue background with mostly white text so it is easier on the eyes.
- I kept the colour scheme to a minimum and mostly had shades of blue and red on all pages.
- I took inspiration from [Stack Over Flow's search results design](https://stackoverflow.com/search?q=iterate+through+an+array) and [the Chefkoch website](https://www.chefkoch.de/rs/s0/butter/Rezepte.html) to get a refence on how to layout multiple details in each search result as I wanted to show summary details on each found item.
- [All Recipes website](https://www.allrecipes.com/recipe/237474/chef-johns-roasted-leg-of-lamb/?internalSource=rotd&referringContentType=Homepage) was a small inspiration to me on the layout of the each recipe, and for more than one page on my site.
- [Stack Over Fow's tags key of key words](https://stackoverflow.com/questions/9329446/for-each-over-an-array-in-javascript/9329476#9329476) inspired me to have ingredients and allergens as tags to help summaries my recipes while making the most of left and right space. In stack over flow's example, 'arrays', 'loops' and 'javascript' are tags to summarise the categories of the post.

- [Wireframe 1](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/wireframe1.jpeg)
- [Wireframe 2](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/wireframe2.jped)
- [Wireframe 3](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/wireframe3.jpeg)
- [Wireframe 4](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/wireframe4.jpeg)
- [Wireframe 5](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/wireframe5.jpeg)
- [Data-schema 1](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/data-schema1.JPG)
- [Data-schema 2](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/data-schema2.JPG)
- [Data-schema 3](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/data-schema3.JPG)
- [Data-schema 4](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/data-schema4.JPG)
- [Data-schema 5](https://raw.githubusercontent.com/TommyJackson85/recipe-connect/master/static/images/data-schema5.JPG)


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features
 
### Existing Features
- Header - Consistently found on all pages, contains links for user for all pages and a logo in which also acts as a link to restart page. On small devices the links are displayed in a drop down button.
- Home page display - consists of Logo and a table layed of food. If logged in a button to link to your recipes is available and if logged out its a button to link to the login page.
- login and register page - has two forms. One for loging in, in which only requires username and won't work if username doesn't exist. If it exists, it will redirect you to the user recipes page showing your recipes. The other for registering, requiring username and your country. This form wont work if username already exists.
- user recipes page - only accessable when logged in and will show your list of recipes in full detail. To view remaining description, ingredients and instruction details you must click the recipe box to cause a drop of these details. From each item delete it or edit it through separe buttons. The editing button will redirect you to an editing form.
- create recipe page - a form with two list builders, allows the user to create comprehensive recipes. Clicking submit will add recipe to your list.
    - For saving a recipe, name, cuisine inputs are required while description, image inputs, ingredients and instruction lists are not.
    - ingredients list builder contain ingredient name, amount fields (required to create an ingredient) aswell as 5 optional allergen inputs. Also contains a list box and add to box butto, in which adds items to box in the form of a tag. Each added item can be deleted clicking the delete icon.
    - instruction list builder is simular to indredients builder but with only one required input. It adds each item to a box, creating an ordered list. User can choose to edit item so not to disrupt ordered list, and can also delete instruction items. Clicking edit opens a new form for editing.

- edit recipe page - accessed through the user recipes list on each item. Its almost the same as the create recipe page but loads the form inputs and list builders in their previous setting. Upon clicking submit, the recipe is updated and doesnt add a new recipe.
- search recipes page. Allows user to search recipes by a criteria, with the options to user to use allergen exclusion, ingredient, cuisine inputs upon clicking search. The search results are not strict and just must contain/exclude the typed text. Clicking search also returns a summary fo the found recipes above the list. Returns a list up to 20 results, with each item showing the summary of the recipe in a drop down box when clicked. Contains other details such as upvotes, views, cuisine and a view recipe button. When reopened/reloaded it displays the last search results.
- individual recipe page. accessed through clicking the view recipe button. It uses an entire page to display a full recipe with larger text and the recipe image at its full capacity to the user. Upon viewing it increments the recipe view count. If logged in it will display an upvote recipe button. When clicked it upvotes the recipe. 
- recipe charts - when accessed, it initially shows the cuisine summary, but user has the option to view ingredient, allergen and country of origin summaries. It shows the five most found in the websites recipes.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- redevelop the the list builders on the forms - As an alternative to the current system I have now, I could have the user click a button to add an input to the dom when deciding to add data to a list. For example, a user could add an two inputs representing a new ingredient (one for its name, the other for its cuisine), and then have the option to add one or more allergen inputs to this ingredient. The user could add as many ingredient inputs he/she wants. This could be used for both ingredients and instructions list buiilders. Then when sent to the Python file, I could have python build an object based on this data.
- an advanced search device - simularly, I could have users add more search inputs to build a bigger search query. The user could add more ingredients and exclude allergen inputs to shorten the search results even more.
- have a favourite recipes section on a user profile page - I would first rename user recipes file to user profile. It would still initially load the user recipes, but the user would have the option to switch between favourite recipes (of other users) and the user's own recipes. The favourite recipes could be from the users upvoted recipes list (on the users mlab data). The display of the favourite recipes list will be simular to the listing of search recipes to keep it consistant.
- advanced bar charts - Use the dc.js library I may add further development to the charts, where on clicking each bar it would drill down into other bar chart results to compare data.

### Reworking code in the future

- For building some HTML in JavaScript, I didn't use jQuery, I just added strings together. I understand that this is not the safest of practices but I was rushing the development of them to get the project done. Regardless, it works perfectly at the moment and I will use jQuery to build the HTML.
- My access deletes functions (for ingredients and instructions list builders) both have alot of repeat code. I may rework both as one global function to be used with different arguments (i.e. accessDeleteButtons(instructions) and accessDeleteButtons(ingredients)).
- Rework python. I will revise my Python code to see if there is any code that is repeating. I could put some of it into a global function and call it recall it where its needed.

## Technologies Used

- Python 3 was used to build much of the functionality when transitioning between the backend and front end
- [mLab](https://mlab.com/) 
    - Used for hosting data through Mongodb database collections.
    - Python3 with Flask was used to interact with the database data, though mongo functions such as updating, deleting, inserting, searching, data aggregation.
- [JQuery](https://jquery.com) and regular JavaScript
    - The project uses **JQuery** to simplify DOM manipulation, more strictly for front end tasks. 
    - i.e. building arrays and objects of data to be retrieved from Flask form requests, aswell as to display and interact with data on the form.
- [Materialisecss](https://materializecss.com/)
    - The project uses the **Materialise** css/javascript library to design and develop the form, buttons, lists, nav, side nav, list box and drop down elements.
- [https://dc-js.github.io/dc.js/](dc.js)
    - This project uses the **dc.js** library to build a basic chart that is reusable.
- [Flask](http://flask.pocoo.org/)
    - This project uses the **Flask** python framework for rendering html templates on the dom, redirecting to different templates, passing python data to DOM, rechieving data from its request function and forms. 

## Testing for Code/Tech Quality and Bugs

### code validation testing

- Tested and fixed most of the Python code to fit majority of the PEP8 requirements with [pep8online](http://pep8online.com/)
- I left some long lines unbroken, as it wasn't possible to split them in two as it cause code errors.
- Used the [w3 HTML validator](https://validator.w3.org/) to test for syntax issues and fix them.
- Used the [w3 Jigdaw CSS validator](https://jigsaw.w3.org/css-validator/ ) to test for syntax issues and fix them.
- Used [jshint](https://jshint.com/) to test syntax issues and fix them.

### testing of mLab data changes
When a user...
- logs in, the logbase collection shows the users id as a foreign key.
- logs out, the logbase shows no user details.
- creates an account, their details are uploaded to mLab, such as including username, country and their recipe list array list, and upvoted recipes array list are created and added to the collection object.
- creates a new recipe, the recipe is added to the recipes collection, including text data such as recipe name, cuisine, description, ingredients object and instructions list array, allergen summary list array, user details (name and country); numerical data such as upvotes and views, user id as a foreign key; The recipe id is also added to the users recipe list as a foreign key.
- updates a recipe, the recipe values are changed to their correct values.
- views individual recipes, it increments the recipe views section of the recipe.
- upvotes a recipe, it increments the recipe upvotes section of the recipe, and adds the recipe id to the users data under its recipes upvote section.
- deletes a recipe, it removes the recipe data from the recipes collection, and it removes the recipe foreign key from the user's recipes list data and its removed from all users recipe upvotes list (if they hold the id)

### bugs found and fixed.
- Pymongo code 
    - for removing upvoted recipe ids from users recipes list (on each user database), was not working properly and was only removing one from one found user. I had to each iterate through each user who upvoted the recipe, and remove from each through an individual mongo request. I am looking for an alternative to to do all in one request.
    - for searching results without an allergy wasn't working as I wanted, I had to use re.compile and re.IGNORECASE to fix it.
- jQuery AJAX
    - for sending data to python from forms, I initially wanted to use AJAX because I was sending arrays and objects, and because Flask's request forms was limited to input values. While I got it working, it wasn't redirecting the page properly. Appending inputs with its values containing the values was the best option. 
    - Sending Object and Array data between Flask and JavaScript had its problems in that I had to turn JSON to strings for sending the data and then back to JSON.
    - I had trouble using single inverted commas when building lists of ingredients and instructions. Flask would read them as a break in the string and caused an error. I compensated this by having the commas removed from each string through JavsScript. I will translate them over to python strings as a future development.
    - I had frequent bugs when deleting and editing instructions, to do with accessing the buttons again after changes. I fixed them by just reloading the array data to the dom and reaccessing the built lists. This is not ideal in terms of performance (Especially when dealing with mass data. I will rework this in the future if performance becomes a stronger requirement.
    - When deleting instruction items, I had a common problem in that more items would be deleted after each one. I reworked the for loop to only delete one.
Heroku
    - I had to restart my heroku application due not loading my page. This was due to mistakes in commits.

## User Story testing

- In reflection of my user requirements I went through every section.

### header
- The page's header's logo consists of its name and a font-awesome's knife and fork sign. It is also a link that reloads the whole site.
- My header consistently has links to my my Search Recipes and Recipe Charts pages on all pages, allowing consistent access.
- When I am logged into the application, my header also consistantly displays (on all pages) links to my 'My Recipes' (user recipes), 'Add Recipe' (create recipe) pages, and a 'Log Out' link which logs user out and redirects to Login and Register page.
- When I am logged out, my header has a link to my Login and Register page consistantly.
- For smaller screens and mobile devices, these links are located in a side nav bar that pops out when I click the list button on the left
- If one of the links is associated with the current loaded page, the link is highlighted.

### home page
- Upon loading the website, I am directed to the home page, in which shows an image of food.
- If I am..
    - not logged in, I am presented with a link to the login/register page.
    - logged in, I am presented with a link to my recipe list page.
- Each button redirects me to the associated page.

### login and register page
- Upon loading the login and register page, I am greeted with a 'welcome to recipe-connect!..' message.
- Registration and login submissions are not submitted if any of its input fields are empty, and I am alerted if one of them is missing.
- Failed login and registration attempts redirect me to the login and register page, greeting me with a red warning message.
- A failed 
    - Login due to login name not existing greets me with 'Login username could not be found!...'.  
    - registration due to username existing, greets me with 'Registered username already exists!...'.
- A succesful 
    - registration reloads the login and register page so I can now login and greet me with 'Registration was a success!' in green text.
    - login redirects me to the user recipes page of my account, showing my previously built recipes.

### user recipes page
- My recipes are displayed on a list of boxes, showing the recipe name, cusine, last updated, upvotes, views and two buttons for deleting and editing.
- If I have no recipes created, one box item prompting me to start creating recipes, including a Create Recipe button in which redirects me to the create recipes page.
- Upon clicking the base of each box, a drop down box is appears showing the description value (wether its empty or not). 
- The listings of ingredients (including their amounts and associated allergens) and instructions can also be displayed in the dropbox if their values are not completely empty.
- Upon clicking the delete button of each recipe, the user recipes page is reloaded, redisplaying the recipes list and showing that the recipe is now missing. No other recipes are removed and there are no other faults.
- Upon clicking the edit button of each recipe, I am redirected to the edit recipe page.

### Create Recipe page
- When I am redirected to this page, a form is displayed showing recipe name, cuisine and description inputs, an ingredients adder device, an instructions list builder device, and a 'submit new recipe' button.
- Upon clicking the submit button,
    - If the Recipe Name or Cuisine inputs are empty, I am alerted about it and the recipe is not submitted.
    - If they are not empty, the recipe is inserted to my recipe list (through the mongodb database) and I am redirected to the user recipes page in which shows the recipe has been added. All information from the form is added to the recipe display (including description, built ingredients, instructions lists) of the recipe item on the 'user recipes' page.
    - There is no duplication of this recipe added, it is just the one, with no missing information.

#### the Ingredients adder
- contains list box, ingredient, amount inputs, 5 optional allegen inputs, and an 'add to box' button.
- Upon clicking 'add to box' and If ingredient and amount inputs are...
    - Empty, I am alerted about it and no ingredient is added.
    - Not Empty, the ingredient (including amount and delete button/icon) is added to the box within a yellow boxed item keeping it separated. All ingredient input fields are cleared allowing me to start a creating a new ingredient.
- The add to box button does not created a duplication of the item. It only adds one ingredient at a time.
- If one to five of the allergen inputs are filled upon clicking, they are included with the ingredient in the yellow box.
- If I make a mistake, I can click the red delete button of each item to remove it.

#### the Instructions list builder
- contains list box, instruction input, and an 'add to box' button.
- The 'Add to box' but clearly indicated to me that it is for adding to the list box above.
- Upon clicking 'add to box' and If the instruction input is...
    - Empty, I am alerted about it and no instruction is added
    - Not Empty, the instruction is added to a numerical list in the list box (including delete and edit button/icons).
- The add to box button does not created a duplication of the item. It only adds one instruction at a time.
- If I make a mistake on each added instruction, I can click the red delete button to delete it OR click the blue edit button to edit it.
- Upon clicking the editing icon, an edit instruction item box appears below the the list box, showing an input field containing the instruction value and a 'save instruction edit' button.
- Upon clicking 'save instruction edit', ...
    - and If I make the input empty it doesn't alerts me about it, doesn't save the edit and leaves the edit box open.
    - and If I've changed or haven't changed the text, it saves the edit regardless. It only overwrites the one section of data and no other data.
- While the edit box is open I can't edit or delete other ingredient / instruction items (and their individual buttons are faded to tell me.)
- I can disregard the edit, removing the edit box, when I attempt to add an ingredient, instruction, or submit my recipe. This does not over write the data either.
- The restrictions make the device feel secure and lest complicated

### Edit recipe page and saving a recipe edit
- When redirected to this page, it displays a form of the same structure of the Add Recipe page but includes the recipe's values in their associated inputs and list boxs, i.e. the recipes ingredients are loaded in the recipe addes list box and the recipe name is the value of the recipe name input.
- This allows me to conveniantly edit the recipe where I left.
- The form follows the same rules as the Add Recipe page form, except when submitting it.
- Upon clicking Submit Recipe Edit, it submits the recipe to be updated and redirects me the user recipes page.
- From the user recipes page I can see that the specific recipe has been updated, and no new recipes added.
- All other recipes have not been changed.

### Recipes search page
- Upon loading the recipes search page, I am given the option of using three inputs variations for searching, i.e. 'Ingredient', 'Cuisine', and 'Without Allergen'. On load they are either empty or show the values of the last search.
- A search is conducted on loading the page aswell, correlating with the whats in the search inputs. The search shows maximum results of 20.
- I tested the the search button regularly, with various inputs:
    - While the ingredient and/or cuisine fields are filled, the 'search recipes' button only returns results related to those fields. If I inlude a value in the 'without allergen' field for a search, the search results excludes the allergen value.
    - I can use one to all input fields as long as they are filled. 
    - When inputs are empty they are not used in the search.
- The search button always returns the most upvoted recipes as first priority, the most viewed as second priority and the most recently updated as third priority.
- Each returned search result on initial display shows the recipe's name, cuisine, upvotes, views, last updation, user who created the recipe and his/her country of origin, and a view recipe button in which on click brings me to an individual recipe page showing all details of recipe.
- Above the list of recipes, the user can find brief summary details, of new recipes (7 days or less), older recipes, number of countries found, and cuisine types found.
- Upon clicking each box base, it shows a brief summary of the recipe's ingredients names' listed, allergen summary, a description and a picture of the recipe.
- This helps me break down what I am looking for, before clicking view recipe on each item.

### Each recipe page
- Upon clicking view recipe from each found recipe, I am redirected to an individual recipe page showing the full details of the recipe.
- This page shows all the recipe details as large as possible, making the most user of the screen width span.
- On load, I increment the recipe views by onw.
- If I am logged in, there is an upvote recipes button available, in which on click reloads the page telling me I upvoted the recipe and increments the recipe upvotes instead of the views.
- When ever I revisit this recipe when logged in, it tells me I upvoted the recipe.

### Recipes charts page
- Upon loading the recipes chart page, I am presented with a bar chart showing the 5 most common cuisines ( and their individual amounts ) found on the website.
- If I hover over each it reveals the exact stats on each.
- Above the chart are four buttons for four cetofries including cuisines. Other categories are ingredients, allergens, and countries of the users who created the category.
- Upon clicking each button, it reloads the page for each category.
- Upon loading the page, or changing category, the individual bars relaod scrolling from the bottom to the top, giving me a clear indication they have changed.

### General User Experience
- Upon hovering over buttons and interactive items, they are highlight a different color or shade to tell me its interactive.
- On small screens, the text doesn't feel to big and there aren't excessive spaces disrupting the content.
- The listing of items on the user recipes and search recipes page uses as much the space as possible, alligning items where possible, reducing the height, to keep as many items in the screen as possible
- The drop down box doesn't use as much space, keeping each section neatly layerd on top of each other and not alligne next to each other.
- Images aren't too big for most cases. On individual recipe pages, they are larger making the most of the page.
- Buttons aligning on top of each have enough space between, making them easy to use on mobile devises.
- Buttons and main headings are centred and use enough space for ease of use and reading.
- Most of the listed data or where data is stacked on top of each other, (i.e. from found search results, recipe pages and user recipes) are left alligned within its own section, for more consistency and ease of reading, this includes buttons like Edit and Delete buttons on list items.

## Deployment

The project has been developed on Cloud9 while linked to mLab Mongodb database though a direct link. 
When developing the project, the code is run locally from the run function on app.py in provides a link to view the project.
The project has been deployed to [Github](https://github.com/TommyJackson85/recipe-connect), in which now contains multiple commits.
From its initial commits I have been hosting it to [Heroku](http://recipe-connect.herokuapp.com/user_recipes/5c6dae9de7179a27eb645024).
When ever I make a commit, the project automatically updates on Heroku. At times I might restart Heroku's dynos if the link doesn't work.
From its last commit, the project is linked to mLab to a more secure link, with its config vars located on Heroku. 
The mlab database user name and passwords have been changed to fix for security purposes.

## Credits

Special thanks goes to the following for assisting me through the development of my project:
My mentor Moosa Hassan.
Tutors and administration at Code Institute.

### Media
- Home page originally from this [link](https://www.tripadvisor.ie/Restaurant_Review-g293984-d2039127-Reviews-Falafel_Gabay-Tel_Aviv_Tel_Aviv_District.html). The Image is for Falafel Gabay restaurant @ Bograshov 25, Tel Aviv Israel, and for the trip advisor page.
- 'No Image Found' image originally from this [website](http://www.inimco.com/blog/).
- All other imaged are imaged hosted on mLab by various users. Go into developer tools to check HTML to find links to images.
- The images used in this project are not for commercial benefit as this project is for learning purposes only.

### Acknowledgements

I took inspiration from..
- [Stack Over Flow](https://stackoverflow.com/) for search results designs and tags.
- [The Chefkoch website](https://www.chefkoch.de/) for search results designs and recipe.
- [All Recipes website](https://www.allrecipes.com/) recipe layout.
