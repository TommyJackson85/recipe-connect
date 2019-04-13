# Your Project's Name

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

# user stories

As a user I want to be able to .. 

Create a user user account and be able to use my username to login into a profile database.
be able to create, edit and view my recipes upon loging in to the application.
be able to add name, cuisine, description, ingredients, allergens, instruction details to the recipe upon creating them through a recipe form.
be able to view a profile page that shows the list of recipes I have built. 
Be able to view all details of each recipe from the recipe list, so I don't have to relocate to an individual recipe page.
Be able to delete recipes from the profile page, and have the recipe list reloaded upon deletion showing the recipe has been removed
be relocated to an edited form when deciding to edit a recipe, in which shows various recipes details as values of inputs and lists of individual data, in which I will be able to change all of it.
from both from both the recipe creation and editing forms, I want to be able to add and delete ingredients to/from a collection, in which each item can show the name, amount and associated allergens of each ingredient.
from both from both the recipe creation and editing forms, I want to be able to add, delete and edit individual instructions, in which I can create a clear adaptable number ordered list of instructions.
from both from both the recipe creation and editing forms, be alerted when required fields are missing.

be able to search multiple recipes from various users, in which will return them as list and will show the most popular recipes as a first primary, most viewed as a second primary, and most recently updated as a third primary. 
I don't need to login when searching all recipes.
I will atleast be able to view a summary of key recipe details from each search result, in which will show the recipe name, cuisine, upvotes, views, ingredients, allergens, description, user who created it and her/his country of origin.
upon searching recipes, I can create a strict search query, in which will have the options of including a recipe cuisine, ingredient aswell the option of excluding an allergen from the query.
For each found recipe, I can relocate to an individual page of a recipe, in which shows all the recipe's details. If I am logged into the application, I have the option to give the recipe an upvote from the individual page. If I have already upvoted the recipe, the recipe page will tell me.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:


As a user I want to be able to .. 

Create a user user account and be able to use my username to login into a profile database.

### header and footer
- My header's logo consists of its name and a font-awesome's plus-circle sign. It is also a link that reloads the whole page.
- My header consistently has links to my my Search Recipes and Recipe Charts pages on all pages, allowing consistent access.
- When I am logged into the application, my header also consistantly displays (on all pages) links to my 'My Recipes' (user recipes), 'Add Recipe' (create recipe) pages, and a 'Log Out' link which logs user out and redirects to Login and Register page.
- When I am logged out, my header has a link to my Login and Register page consistantly

### login and register page
- Upon loading website, and if there isn't a user logged in, I am redirected to the login and register page. I am greeted with a 'welcome to recipe-connect!..' message.
- Registration and login submissions are not submitted if any of its input fields are empty, and I am alerted if one of them is missing.
- Failed login and registration attempts redirect me to the login and register page, greeting me with a red warning message.
- A failed login due to login name not existing greets me with 'Login username could not be found!...'.  
- A failed registration due to username existing, greets me with 'Registered username already exists!...'.
- A succesful registration reloads the login and register page so I can now login and greet me with 'Registration was a success!' in green text.
- A succesful login redirects me to the user recipes page of my account, showing my previously built recipes.

### user recipes page
- My recipes are displayed on a list of boxes, showing the recipe name, cusine, last updated, upvotes, views and two buttons for deleting and editing.
- If I have no recipes created, one box item prompting me to start creating recipes, including a Create Recipe button in which redirects me to the create recipes page.
- Upon clicking the base of each box, a drop down box is appears showing the description value (wether its empty or not). 
- The listings of ingredients (including their amounts and associated allergens) and instructions can also be displayed in the drop if their values are not completely empty.
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
- If one to five of the allergen inputs are filled upon clicking, they are included with the ingredient in the yellow box.
- If I make a mistake, I can click the red delete button of each item to remove it.

#### the Instructions list builder
- contains list box, instruction input, and an 'add to box' button.
- Upon clicking 'add to box' and If the instruction input is...
    - Empty, I am alerted about it and no instruction is added
    - Not Empty, the instruction is added to a numerical list in the list box (including delete and edit button/icons).
- If I make a mistake on each added instruction, I can click the red delete button to delete it OR click the blue edit button to edit it.
- Upon clicking the editing icon, an edit instruction item box appears below the the list box, showing an input field containing the instruction value and a 'save instruction edit' button.
- Upon clicking 'save instruction edit', ...
    - and If I make the input empty it doesn't alerts me about it, doesn't save the edit and leaves the edit box open.
    - and If I've changed or haven't changed the text, it saves the edit regardless.
- While the edit box is open I can't edit or delete other ingredient / instruction items (and their individual buttons are faded to tell me.)
- I can disregard the edit, removing the edit box, when I attempt to add an ingredient, instruction, or submit my recipe.

#### Edit recipe page and saving a recipe edit
- When redirected to this page, it displays a form of the same structure of the Add Recipe page but includes the recipe's values in their associated inputs and list boxs, i.e. the recipes ingredients are loaded in the recipe addes list box and the recipe name is the value of the recipe name input.
- This allows me to conveniantly edit the recipe where I left.
- The form follows the same rules as the Add Recipe page form, except when submitting it.
- Upon clicking Submit Recipe Edit, it submits the recipe to be updated and redirects me the user recipes page.
- From the user recipes page I can see that the recipe has been updated, and no new recipes added.

#### Recipes search page
- Upon loading the recipes search page, I am given the option of using three inputs variations for searching, i.e. 'Ingredient', 'Cuisine', and 'Without Allergen'. On load they are either empty or show the values of the last search.
- A search is conducted on loading the page aswell, correlating with the whats in the search inputs. The search shows maximum results of 20.
- I tested the the search button regularly, with various inputs:
    - While the ingredient and/or cuisine fields are filled, the 'search recipes' button only returns results related to those fields. If I inlude a value in the 'without allergen' field for a search, the search results excludes the allergen value.
    - I can use one to all input fields as long as they are filled. 
    - When inputs are empty they are not used
- The search button always returns the most upvoted recipes as first priority, the most viewed as second priority and the most recently updated as third priority.
- Each returned search result on initial display shows the recipe's name, cuisine, upvotes, views, last updation, ingredients names' listed, allergen summary, user who created the recipe and his/her country of origin, and a view recipe button in which on click brings me to an individual recipe page showing all details of recipe.
- All results are displayed in a box as a summary. Having the ingredients and allergens summary displayed helps me break down what I am looking for in a recipe so I can search through all recipes.
- When clicking the base of each box, a description drops down.

#### 

be able to search multiple recipes from various users, in which will return them as list and will show the most popular recipes as a first primary, most viewed as a second primary, and most recently updated as a third primary. 
I don't need to login when searching all recipes.
I will atleast be able to view a summary of key recipe details from each search result, in which will show the recipe name, cuisine, upvotes, views, ingredients, allergens, description, user who created it and her/his country of origin.
upon searching recipes, I can create a strict search query, in which will have the options of including a recipe cuisine, ingredient aswell the option of excluding an allergen from the query.
For each found recipe, I can relocate to an individual page of a recipe, in which shows all the recipe's details. If I am logged into the application, I have the option to give the recipe an upvote from the individual page. If I have already upvoted the recipe, the recipe page will tell me.


1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
