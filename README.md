# **Honda Motorcycle Ecommerce Shop Final Project**
**Edmund O Callaghan**

This is my Honda Ecommerce Motorcycle shop, which gives the end-user an array of motorcycles that can be viewed for interested users. It also has the option for users to buy any of the listed motorcycles

The user can view their profile details, past order details including delivery address and view their items in their shopping cart.

The user can Search for items which contain letters or word structures, they can add motorcycles to their shopping cart and edit the quantity of each motorcycle within the cart.

The shop uses a Stripe api to manage payments, currently the Stripe account is set to development mode, so you can only use stripes test cards for transactions, which can be found [here](https://stripe.com/docs/testing)

The idea for this site is to show CRUD functionality with python3 and sql, Stripe api functionality using jquery. To show user authentication and Djangos CMS system based off the custom models for motorcycles and orders, which is only available to administration users and allows the administration user to add motorcycles and view orders and delete user accounts etc.

The web app also contains forms of contacting me in my footer, via conact me modal, github and linkedin.
 
 
## Demo

A live demo can be viewed [here](https://honda-motorcycle-ecommerce.herokuapp.com/ )

![Desktop Demo](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/static/images/honda-shop-preview.PNG "Desktop Demo")

## User Experience

### User stories
As an end-user I want to find all the motorcycles on this web site with ease, I want to add products to my shopping cart with ease and quick succession. I want to edit my shopping cart contents either by removing them or amending the quantity. I also want to be able to purchase products at the checkout page and add my adddress details so I can receive my motorcycle.

Any employers who visit my site will wannt to see my level of design and consistancy, along with the ability to write functioning code with python3, postgresql and jquery. I also want to his skills with Frameworks such as Django.

Any recruiters who visits my web site will want to see if my site meets the requirments of the position they are recruiting for.

### Strategy

For this project I wanted a motorcycle ecommerce site specifically for honda motorcycles. My aim was to evoke a positive emotional response from the user when they visited my site, and provide them with an array of honda's motorcycles, they coud read shop reviews from previous customers, they could edit a user review, and add their very own review of the shop from the set form structure.

In this project my goal was to create consistancy in design flow, and colour schemes. The site is designed to showcase motorcycles for sale, allow users to create an account, and using there account they can go to the checkout page and fill in the form and add payment details. The web site is designed mobile first, in regards to content layout and css media queries, but the site does respond well on desktop, laptop and tablet screens.

The main goal in this project was to showcase my ability to use a full stack framework called Django which is a python based framework. It also shows my use of a postgresql database.

### Scope
The scope of the project was to provide an application that the end-user could use to purchase whatever honda motorcycle that they prefer best and would respond primarily on a mobile device, and showcase my design, python, Django and postgresql skills to date along with jquery, html, and css.

### Structure
The navigation bar was meant to be easy to access all of the time, so with this in mind it was fixed to the top of the screen. 

The footer has some links using icons that suits appropriate function, the email icon which opens up the modal to contact me, and allows end-users to contact me via email.

The navigation bar has a honda icon linked as a home button, a products button to show all motorcycles for sale, a cart button to show all items currently in the cart, a login button if the user is not logged in, a register button if the user is not logged in, shop reviews to show any reviews from users, add reviews button to add a user review and finally a search input box acompanied by a search button.

The motorcycle app will bring you to all motorcycles available, and the search field can limit the results by name to show similar motorcycles for example you can search for all bikes with 500 and it will limit results to all motorcycles with 500 in there name.

The cart app will show you all items that have been added to the cart when you add them from the products page. 

The login, register or forgot password pages: Login can be used for users who already have an account, and they will just need to enter their user name or email and password. If the user is new to the site and would like to purchase items from their cart, then they can use the register page or else they will not be able to purchase items. The forgot password option will only work for users who are using non-test based email accounts.

The reviews page will show you all user reviews, and gives the user an opinon of the shop sellers before they commit to purchasing any motorcycles. The add review page will allow a user to leave their opinons of the shop and their experience.

For adding the review the user can only access this by the navbar which means it is allways accessible, the button will redirect the users page to an add review page.

### Skeleton

[Index page wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/index-page-wireframe.jpg)


[Motorcycles page wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/motorcycle-items-wireframe.jpg)


[Shopping cart page wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/shopping-cart-wireframe.jpg)


[Profile page wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/profile-wireframe.jpg)


[Checkout page wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/checkout-wireframe.jpg)


[Login, register or reset email wireframes](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/login-register-or-forgot-password-wireframe.jpg)


[User reviews wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/index-page-wireframe.jpg)


[User review, add review and edit wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/user-review-add-or-edit-wireframe.jpg)


[Contact me modal wireframe](https://raw.githubusercontent.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project/master/wireframes/contact-modal-wireframe.jpg)


### Surface

#### Red shades: 
rgb(189, 84, 52);

rgb(204, 0, 0);
#### White shades:

rgb(255, 255, 255);

#Grey Shades:

'#cac8c8c9;'

rgba(0, 0, 0, 0.388);

The colour scheme I was going for was to go with Hondas motorcycles colour scheme. This created a pleasing to the eye, and above all evoking a positive response from the end-user.   

## Technologies

1. HTML 5
2. CSS
3. Bootstrap (4.4.1)
4. JavaScript
5. JQuery (3.4.1)
6. Emailjs (2.3.2)
7. Python3
8. Django (1.11.29)
9. Stripe (2.45.0)
10. Pillow (7.1.1)
11. Django forms bootstrap (3.1.0)
12. Boto3 (1.13.0)
13. botocore (1.16.0)
14. Heroku Postgresql database
15. Gunicorn (20.0.4)
16. AWS s3transfer (0.3.3)
17. Django storages (1.9.1)


## Features
 
### Existing Features

- The core feature of my site is to provide an outlet for a interested user to purchase a Honda motorcycle(s). The user can view motorcycles and add them to the cart but as soon as they go to checkout and if they're not signed in, they will be brought to the sign in page, and once they either create and account from the link in the sign in page saying do you have an account, if not click here, only then will they be able to proceed to the checkout, this will automatically redirect you once you have signed in or up. 

- The user can add their own user review based on their shopping expierence and edit reviews, currently there is only a login required in order to add a review and on editing a review, this will be updated in the future so that the user who is logged in can only edit there own review, but for this initial release this feature won't be available due to limited time constraints.

- For my navigation bar I have it set fixed to the top of the screen for constant accessiblity for the user. This evokes a positive response from the user and makes it easier to find the navigation elements within the navbar. The navigation bar features a search input box and button, this will allow the user to search for items based on similar wording.

- For the footer section I have a contact me logo which bring up a contact me modal form, it also includes social external links to my github and linkedin.

- For the reviews section you can get a glimpse at all the site reviews, and once you click on the see more/read more button you will be able to view a detailed description of the review.

- As the user you can view all current models of motorcycles within the database in the motorcycle/products page. Only the admin user has the accessiblity and rights to manipulate the motorcycles, orders etc.

- In the navigation bar you can choose the `add review` option and this will bring you to the add review page and let you add a new review based on the schema of models and forms.py files for shop_reviews.

### Features Left to Implement

If I had more time I would like to add a requirement for an access key to edit user reviews, this will be updated in the future, but for this initial release this feature won't be available, due to limited time constraints.

I would also like to add the option to filter the users reviews and also have pagination for motorcycles and user reviews, just in case the site receives more traffic in the future, for the moment though this site doesn't have any need for pagination.

I would like to add a pre-order option for customers to pay a deposit for a motorcycle so that it can be ordered and then in orders section to add a pay remainder option if you have pre-ordered the motorcycle.

## Testing 
Testing ID: test-data-centric-project-eoc
### Tested by: 
Edmund O Callaghan

### Tested devices: 
- DELL Desktop, 
- AMD Desktop, 
- DELL Latitude E5470 Laptop, 
- Fujitsu Q702 Ultra book,
- ZTE Axon 7 Mobile,
- Iphone X, 
- Iphone 6, 
- Samsung S9.

### Tested Resolutions: 
320px x 640px to 4K resolution: 

Note: On 4k screens the site does not support the view height of the screen.  

### Tested Browsers:
- FireFox,
- Google Chrome, 
- Edge. 

- Note: on edge browser the colour of the contact me modal and the add review modal are not supported by edge.
### Code validation Testing:

[Index HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/index-page-validation.PNG)

[Critics Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/critics-page-validation.PNG)

[Edit User HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/edit-user-page-validation.PNG)

[User Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/user-page-validation.PNG)

[Single Critic Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/single-critic-page-validation.PNG)

[Global JavaScript Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/general-js-validation.PNG)

[Send Mail JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/send-mail-code-validation.PNG)

[Python Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/python-code-validation.PNG)

[CSS Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/css-validation.PNG)

### User stories
For my user stories testing, I had to put myself in the shoes of the user, anyone looking for a quick way to get information about potential kawasaki modals. They would want to see expierenced riders opinons on the matter and detailed descriptions. They would also be looking for more personal and like minded reviews, to get an idea what the everyday rider thinks of these bikes.

The everday user will want to gain access to the applications quickly and will be looking for quick input(s), that give back what they are looking for, like user reviews brings you straight to the reviews at hand, and critic reviews does the same, and the see more option is easy to interpret, which brings you to a detailed review of each particular motorcycle.

They want to be given clean and clear directions as to where they should navigate to in order to achieve their intentions, whether that be sending an email, or adding a review themselves.

As a recruiter or employer I want to find out with quick succession, whether this candidate has the required skills as a database designer/developer for the job spec. When you arrive at the site you are greeted with a professional, concise and impactful website, this showcases good design and clear intentions as to what it is. 

With regards to the above mentioned user stories & the usability of the web app, the outcome for this test was successful, It met all expectations of ease of use. 


### **Responsive Flow Testing:**

#### Home Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | On Desktop screens the jumbotron stretches out 75% of the screen, the background image is centered | as expected |
| Laptop(s) | On laptop devices it remains the same bar the footer which you now need to scroll down to access | as expected |
| Tablet(s) | On tablet devices the background image is still centered, but the ends of the motorcycle are cut from view and you need to scoll down to view the footer in landscape view | as expected |
| Mobile(s) | On mobile the jumbotron takes up 75% of the width, and the background image is positioned to the center right of the screen, you can't see the footer until you scroll down | as expected |

#### Critics Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | The cards for each review are in rows of 3 | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The cards for each review are in rows of 2 | as expected |
| Mobile(s) | The cards for each review are in rows of 1 | as expected |

**Note:** For user reviews the page behaves the same bar when in mobile view, where there is a small margin around the cards, which is as expected.

#### See more critic review Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | The card takes up 75% of the screen width and has a scroll option for the detailed description | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The layout changes where the image stacks on top of the preview description and the overall description stack under the preview description while maintaining the scroll option  | as expected |
| Mobile(s) | The layout remains the same as the tablet bar the content width, which is now 100% of the screen's width. There is no longer a scroll option for the detailed description | as expected |

### **Functional testing** 

**This test goes through every functional aspect of the project through GUI based manual tesing**

**Note:** When testing the navigation bar all links bring you to the intended locations. This is as expected.

#### **Critic reviews actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| See more button | Click on element | Brings you to specific review  | as expected |
| Back to critic reviews button | Click on element | Brings you back to critic reviews  | as expected |


#### **User reviews actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Edit button | Click on element | Brings you to the edit page  | as expected |
| Delete button | Click on element | deletes the review | as expected |


#### **Add review actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Add review link in navbar | Click on element | Brings up the add review modal  | as expected |
| models dropdown | Click on element and choose a model | no warning messages appear | as expected |
| overall rating dropdown | Click on element and choose a rating | no warning messages appear | as expected |
| name input field | type in a name | no warning messages appear | as expected |
| ride quality and brakes dropdown | Click on element and choose a rating | no warning messages appear | as expected |
| engine dropdown | Click on element and choose a rating | no warning messages appear | as expected |
| build quality and reliability dropdown | Click on element and choose a rating | no warning messages appear | as expected |
| running costs and value dropdown | Click on element and choose a rating | no warning messages appear | as expected |
| review summary input field | type in a summary between 25 chars and 100 | no warning messages appear | as expected |
| Add review button | Click on element | closes the modal and adds the review in user reviews | as expected |


**Note:** for the input fields for summary and name, they re both required fields. Name field has no min value, but has a max of 25 characters. you will not be allowed to enter any more, this is the same for summary just that the minimum is 25 characters and the max is 100 characters. You won't be allowed to submit if they are blank, or is the summary is less then 25, and you simply won't be allowed to type anymore the the required amount(s).

**Note:** for the edit review section the fields are the same, bar the edit button which simply updates the review that is currently open. The data from the particular review that is being edited is populated within each specific field, so there is no room for leaving a blank entry for dropdown, but they can be changed. You can however leave the input fields blank, and this will again bring up a warning saying they are required. The edit review section is not a modal so there is no close button, in order to go back to user reviews you need to use the navigation bar, other then this there is no difference found for the testing results.

#### **Footer Secttion expected actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| linkedin icon | clicks on linkedin icon | brings you to an external link | as expected |
| github icon | clicks on github icon | brings you to an external link | as expected |
| email icon | clicks on contact button | opens up a contact me modal | as expected |
| input name | type in your name | no warning messages come up | as expected |
| input email address | type in your email | no warning messages come up | as expected |
| input message area | type in your message | no warning messages come up | as expected |
| submit button | click send | message sent is displayed | as expected |

#### **Footer Secttion unexpected actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| input name | leave this field blank | please fill this field | as expected |
| input email address | leave blank or input a invalid email format | please fill this field at least 10 characters & must included @ and .com | as expected |
| input message area | leave blank | please fill this field | as expected |

### **CRUD database testing** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Create option | use the add review form and submit to the database | the database receives the object and the site updates the content accordingly | as expected |
| Read option | Click critic reviews, click user reviews | the site updates the content accordingly from the database and the cluster matches what is on the page | as expected |
| Update option | use the edit review form and submit to the database | the database receives the object and the site updates the content accordingly | as expected |
| Delete option | in user reviews click the delete option | the database receives the request to delete the entry and the site updates the content accordingly | as expected |

**Note:** when testing the database the results on the site and on the database were cross referenced, all data matches as expected.

## Deployment

The project is hosted using heroku as github pages doesn't support mongodb.

In order to deploy your site to heroku you will need to follow these steps:

- If you don't have a heroku account already then please follow this link to sign up. [Heroku sign up](https://signup.heroku.com/login)

- After this step [Heroku sign in](https://id.heroku.com/login)

- Now go to your [Heroku dashboard](https://dashboard.heroku.com)

- From this point you should see an option to the right of the screen called        'New' just under your navigation bar. if you can't find it try this link        [Create new app](https://dashboard.heroku.com/new-app)

- From this point you want to choose a unique name as it won't allow you to         choose one already taken.

- You'll need to set the region for where the servers will be based, so that is up to you, it can be US or EU, if most users willl be from EU, then you should choose EU.

- Click Create app, then you will be brought to the deploy tab.

- Scroll down and you will see 'Deployment method' on your left, from there choose 'Heroku Git'. This has all the commands you'll need to login to heroku via your IDE and deploy/push to heroku.

- In your IDE cli you will need to first login, using command line interface.
    Please type the following into you cli: 
    
    $ heroku login

- You will be asked to press any key from the cli, from this point you will want to do so, and then an external or internal browser will open, which will log you into heroku using the browser or require you to do so if you are currently signed out on your browser, then verify if it was successful.

- Assuming it has been successful, you will want to push/deploy to heroku.

- Before deployment you will need to make sure your procfile, requirements.txt have been created and are up to date in your IDE, if not then please add both to your IDE and then follow the next steps.

        Procfile contents: 'web: python app.py'

        requirements.txt file contents:

            Click==7.0

            dnspython==1.16.0

            Flask==1.1.1

            Flask-PyMongo==2.3.0

            itsdangerous==1.1.0

            pymongo==3.10.1

            Werkzeug==1.0.0


- In order to deploy the site to heroku use the following commands in you cli on your IDE:

    $ git add .

    $ git commit -m "final deployment"

    $ git push heroku master

- After deployment, you still need to setup **config variables**, please follow the instructions below to do so:

    - Go to the '**Heroku Dashboard**' and look for **Settings**.
    - Then click the option to **Reveal Config Vars**.
    - Enter in the variable names and their values
        - Name: **YourSitesURIName** value: Database url here
        - Name: **IP**  value: 0.0.0.0
        - Name: **Port** value: 5000


In order to run the site locally, you can use the clone this site by using the following link in your terminal: `git clone https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews.git` To remove any connections with Github repository use the following in your terminal: `git remote rm origin`.  

If you need anymore help in cloning this repo, then go to GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).


## MongoDb Schema

### The critic's MongoDB collection `critic reviews` takes the following schema.

{
    "_id": {
        "$oid": "5e63de321c9d440000a20906"
    },

    "image": "",

    "model": "",

    "price": "",

    "engineSize": "",

    "power": "",

    "insuranceGroup": "",

    "seatHeight": "",

    "overallRating": "",

    "overallDescription": "",

    "rideQualityAndBrakes": "",

    "Engine": "",

    "BuildQualityAndReliability": "",

    "InsuranceRunningCostsValue": "",

    "Equipment": ""
}

### The user's MongoDB collection `user reviews` takes the following schema.

{
    "_id": {
        "$oid": "5e63dfe51c9d440000a20907"
    },

    "image": "",

    "model_select": "",

    "overall_rating": "",

    "name": "",

    "ride_quality_and_brakes": "",

    "engine": "",

    "build_quality_and_reliability": "",

    "running_costs_and_value": "",

    "review_summary": ""
}

## Credits

### Media
I used [Pinterest](https://www.pinterest.com/) for my background image, and other motorcycle images.

### Acknowledgements

I used [MCN's site](https://www.motorcyclenews.com/) for my critic reviews content description section, and for general information about each motorcycle that was used in this project.

Modal Contact Form outer sections Reference can be found [here](https://mdbootstrap.com/docs/jquery/modals/forms/)

Bootstrap code I used to look up for reference purposes, I used [bootstrap.com](https://getbootstrap.com/)

**This project is for educational purposes.** 

[![Build Status](https://travis-ci.org/Novicetheaf/Honda-Motorcycle-Ecommerce-Project.svg?branch=master)](https://travis-ci.org/Novicetheaf/Honda-Motorcycle-Ecommerce-Project)