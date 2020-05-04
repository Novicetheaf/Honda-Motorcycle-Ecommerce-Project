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
Testing ID: Honda-Motorcycle-Ecommerce-Project-eoc
### Tested by: 
Edmund O Callaghan

### Tested devices: 
- DELL Desktop, 
- AMD Desktop, 
- DELL Latitude E5470 Laptop, 
- Fujitsu Q702 Ultra book,
- Axon 7 mini Mobile,
- Iphone X, 
- Iphone 6, 
- Samsung S9.

### Tested Resolutions: 
349px x 640px to 4K resolution  

### Tested Browsers:
- FireFox,
- Google Chrome, 
- Edge. 

### Code validation Testing:

- Validation code testing not complete, due to gitpod workspace corruption.

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
For my user stories testing, I had to put myself in the shoes of the user, anyone looking to purchase honda motorcycles. They would want to be given an array of different types of bikes available. They would also be looking to find out what customers thought of the shopping expierence at the Honda motorcycles shop. They would want to be able to make payments for the motorcycle(s) that peaks their interest. They would need a way to view their orders to make sure that the address entered was correct. They would need to be able to create an account in order to store what is in their cart and orders.

The everday user will want to gain access to the applications quickly and will be looking for quick input(s), that give back what they are looking for, shop reviews brings you straight to the shop reviews at hand, products/motorcycles does the same, add reviews, search box, log out, etc.

They want to be given clean and clear directions as to where they should navigate to in order to achieve their intentions, whether that be viewing motorcycles, viewing profile, viewing cart, navigating to checkout, making a payment, signing in, registering, sending an email, or adding a shop review themselves.

As a recruiter or employer I want to find out with quick succession, whether this candidate has the required skills as a database designer/developer for the job spec. When you arrive at the site you are greeted with a professional, concise and impactful website, this showcases good design and clear intentions as to what it is. 

With regards to the above mentioned user stories & the usability of the web app, the outcome for this test was successful, It met all expectations of ease of use. 


### **Responsive Flow Testing:**

#### Home Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | On Desktop screens the jumbotron stretches out 75% of the screen, the background image is centered | as expected |
| Laptop(s) | On laptop devices it remains the same bar the footer which you now need to scroll down to access | as expected |
| Tablet(s) | On tablet devices it remains the same bar the footer which you now need to scroll down to access| as expected |
| Mobile(s) | On mobiles and small tablets the jumbotron takes up 100% of the width and you can't see the footer until you scroll down | as expected |

#### Motorcycles/Products Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | The cards for each motorcycle are in rows of 3 | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The cards for each motorcycle are in rows of 2 | as expected |
| Mobile(s) | The cards for each motorcycle are in rows of 1 | as expected |

**Note:** The images on the cards are reduced along with the card size between 600px and 999px, as expected.

#### Shopping cart Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | White background for cart takes up 100% width, card for motorcycle placed within in similar sized card to motorcycles page, with exception of the amend button, the checkout btn is placed to the right center | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The same as desktop bar the motorcycle card which only fit two in a row and they begin to stack under if there is more then 2 unique items in the cart. The checkout button now goes to the far right | as expected |
| Mobile(s) | The layout remains the same as the tablet bar the checkout button positon, which is now center rigth of the screen. | as expected |

**Note:** The checkout button becomes hidden between 577px and 659px, this issue was left unfixed due to time constraints, and an issue with gitpod workspace which took valuble time from me where I could have been perfecting the breakpoints and styling.

#### Checkout Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | White background for checkout takes up 85% width, the motorcycle cards are now much wider, they have less details and take up 3 spaces within the container of the checkout, the payment details in place below the items and it takes up 50% of the width of the container, the submit button is centered | as expected |
| Laptop(s) | The same as desktop, bar the issue where the images are overflowing which has been mentioned below | as expected |
| Tablet(s) | The container is now at 100% width and the payment form is now taking 95% of the container width, the submit button is now to the far left, motorcycles are now stacked one per row | as expected |
| Mobile(s) | The layout remains the same as the tablet | as expected |

**Note:** At 1280px to 1200px the images for the motorcycles within the cart start to overflow over the cards, this issue was worse but breakpoints were added to amend this issue, however this small range of screen width was left unamended due to time contraints.

#### Profile Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | White background for checkout takes up 100% width, the welcome box takes up 50% width, the orders section takes up to 1140px width due to the container its in and the text is centered and hr's are seperating each order | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The same as desktop, bar the container is now at a max width of 720% | as expected |
| Mobile(s) | The profile container now has only 25px padding left to right and there is no max width set, so the content fills about 95% of the width | as expected |

**Note:** The styling for this section is quite basic and could definatly do with more styling to make it consistantly professional, but due to time constraints this profile section will need to be updated at a later date but for now it serves its purpose quite well.

#### Shop Reviews Page
- With regards to the shop reviews section the container for the reviews are again confined witin the 1140px max width, they have a white background and 3 cards in one row, they are stacked if the number goes over 3, as soon as the screen size gets to 933px the cards for each review are now only in 1 card per row, and are again stacked. The content within are centered. Once you get down to 550px the cards take up 100% of the width and with a small margin left to right, bar this there is no change to the reviews section. 

- As expected

#### Shop Review Page
-With regards to the individual review the review container is again within the 1140px width maximum, and the card is centered within this container, the content is left aligned. Once you get down as far as 1000px the breakpoints change and the max width is now 720px, bar this there is no change. At 575px the container for the card takes 100% width, bar this there is no change.

- As expected

#### Add Review and Edit Pages
- The add reviews and edit reviews page is contained within a 1140px container, and a 720px container for under 1000px, and it takes up 100% width for mobile view. The form input box's and save button are centered within this container.

- As expected

#### Login, Register And Forgot Password
- The login and register page is set with a max width of 1000px and the forgot page is set with a max width of 800px for desktop view, once the screen width gets down below 1000px the container takes up 100% width, and this is the same for the forgot password option at below 800px.

**Note:** On the register page there is a qoute 'aleady got an account', and it is coloured white which makes it not visible, bar when you hover, this link is an element that should have been styled black, but it will be updated in the future, this was left unfinished due to gitpod workspace issue.

### **Functional testing** 

**This test goes through every functional aspect of the project through GUI based manual tesing**

**Note:** When testing the navigation bar all links bring you to the intended locations. This is as expected.

#### **Home page actions**
- The home page renders a signin option if the user is not signed in, or a view products button if they are signed in, these links bring you to the intended pages.

#### **Sign in Register and Forgot Password**
- The sign in page has two required fields username/email and password, once both are correct and match what you enterd originally when you registered it will bring you back to the home page and notify you that you signed in. 

- The register page has four fields username, email, password, and confirm password, all bar the email are client side required, so you can create an account without an email, this just mean that you wont have an email to use forgot password for and you wont have email details to populate the profile field that showcases you email.

- Forgot password option was unfortunaly not working on my gmail account, it comes up with an smtp error in debug mode and a 500 server error in production, this issue was unfortunaly not fixed in time, and it will be updated in the near future. 

#### **Motorcycles/products actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Add button | Click on element | Adds one of the items you clicked | as expected |
| Quantity input | type the qty or use the arrows to adjust qty | By doing this it will change how much of the same item you want to add to your cart, you can see the cart icon's qty icon goes up when you do this | as expected |

- This was as expected.

**Note:** Whatever qty of a certain item you add to the cart cannot be canged unless you go into the cart and choose amend, so this means you can reduce or increase the qty, you can add whatever qty at first from the products/motorcycles page, but after that you need to go to cart to amend the qty or remove. 

#### **Shopping cart actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Amend button | Click on element | Amends the qty of the item you clicked | as expected |
| Quantity input | type the qty or use the arrows to adjust qty | By doing this it will change how much of the same item you want to add to your cart, you can see the cart icon's qty icon goes up when you do this and this is also reflected within the checkout page | as expected |
| Checkout button | Click on element | brings you to the payment details as long as you are signed in, otherwise redirects you to login page | as expected |

- This was as expected.

#### **Checkout actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Submit button | Click on element | Attempts to make a payment and save order details in your profile, this results in payment successful or if the card details are not correct it will be payment declined etc, there will be a client side confirmation tabjust under the navbar with a response | as expected |

- This was as expected.

**Note:** All input fields for payment details form are required via client side validation, bar card number, cvv, month and year of card, these options will be validated by stripe api and will return a message under the navigation bar regarding its result. 

#### **Profile page**
No functional elements to be tested here, the profile button brings you to the page and it renders your user name, and email, and all orders from first to last. 

- This was as expected.

#### **Shop reviews actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Go to review | Click on element | filters the reviews and renders only the review you clicked on within the user review page | as expected |

**Note:** Within the user review page, you can click the edit button and this will bring you to the form to update teh details of the review, now there was an issue where the details of the review didn't fill the form fields, this is a feature that will be added at a later date.

- This was as expected.

#### **Add or edit review actions** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Save button | Click on element | Saves the new review or updates an existing review | as expected |
| Input Fields | Type in your details | These details are required via client side validation, you will need to filll all fields | as expected |

- This was as expected.

#### **Search Input Field**
- For this option you can search letters of words, and if the item in motorcycles contains that charector or combination it will appear in the main content, other you will receive a message notifying you that no motorcycles matched your search.

#### **404 page not found**
- This was tested by turning off debug mode and entering an extension to the web address that was not related to the site, this brings back a 404 not found message and asks the user to have a look at the products available.

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

### **database testing client side and admin access only** 

| Element Tested | Action | Expected outcome | Outcome |
| --- | --- | --- | --- |
| Add option | use the site base address with '/admin/' extension which brings you to admin panel sign in, then go to motorcycles model, click add, enter the appropriate data into the fields and hit save, for adding user reviews go to add review from the navbar client side and enter details and click save, add an order go to bikes add items, cart and checkout, then add payment and address details correctly using stripes testing cards as above then submit | the database receives the object and the site updates the content accordingly | as expected |
| Read option | Click products/motorcycles, profile, shop reviews, shop review, search option | the site updates the content accordingly from the database and the data on the admin panel matches the data on the client side of the site | as expected |
| Update option | use the edit shop review form, admin edit products, admin edit order, admin edit users and submit to the database | the database receives the object and the site updates the content or access accordingly | as expected |
| Delete option | only administration users have the rights to delete an entry, they can delete a user, order, reviews, motorcycles and save | the database receives the request to delete the entry and the site updates the content accordingly | as expected |

**Note:** when testing the database the results on the site and on the database were cross referenced, all data matches as expected. I used Datazenit's heroku data explorer to allow me to view my Heroku Postgresql database [Datazenit's tool can be found here.](https://datazenit.com/heroku-data-explorer.html)

## Deployment



The project is hosted using heroku as github pages doesn't support a postgresql database, It also uses AWS for my static folder, which containes all javascript, css and images.

In order to deploy your site to heroku you will need to follow these steps:

- If you don't have a heroku account already then please follow this link to sign up. [Heroku sign up](https://signup.heroku.com/login)

- After this step [Heroku sign in](https://id.heroku.com/login)

- Now go to your [Heroku dashboard](https://dashboard.heroku.com)

- From this point you should see an option to the right of the screen called 'New' just under your navigation bar. if you can't find it try this link        [Create new app](https://dashboard.heroku.com/new-app)

- From this point you want to choose a unique name, as it won't allow you to choose one already taken.

- You'll need to set the region for where the servers will be based, so that is up to you, it can be US or EU, if most users willl be from EU, then you should choose EU.

- Click Create app, then you will be brought to the deploy tab.

- Scroll down and you will see 'Deployment method' on your left, from there choose 'Heroku Git'. This has all the commands you'll need to login to heroku via your IDE and deploy/push to heroku.

- In your IDE cli you will need to first login, using command line interface.
    Please type the following into you cli: 
    
    $ heroku login

- You will be asked to press any key from the cli, from this point you will want to do so, and then an external or internal browser will open, which will log you into heroku using the browser or require you to do so if you are currently signed out on your browser, then verify if it was successful.

- Assuming it has been successful, you will want to push/deploy to heroku.

- Before deployment you will need to make sure your procfile, requirements.txt have been created and are up to date in your IDE, if not then please add both to your IDE and then follow the next steps.

        Procfile contents: 'web: gunicorn honda_ecommerce.wsgi:application'

        requirements.txt file contents:

            boto3==1.13.0
            botocore==1.16.0
            dj-database-url==0.5.0
            Django==1.11.29
            django-forms-bootstrap==3.1.0
            django-storages==1.9.1
            docutils==0.15.2
            gunicorn==20.0.4
            jmespath==0.9.5
            Pillow==7.1.1
            psycopg2==2.7.3.1
            pylint-django==2.0.15
            pylint-plugin-utils==0.6
            pytz==2019.3
            s3transfer==0.3.3
            stripe==2.45.0


- In order to deploy the site to heroku use the following commands in you cli on your IDE:

    $ git add .

    $ git commit -m "final deployment"

    $ git push heroku master

- After deployment, you still need to setup **config variables**, please follow the instructions below to do so:

    - Go to the '**Heroku Dashboard**' and look for **Settings**.
    - Then click the option to **Reveal Config Vars**.
    - Enter in the variable names and their values
    
        SECRET_KEY = 'x'
        
        STRIPE_PUBLISHABLE = 'x'
        
        STRIPE_SECRET = 'x'
        
        AWS_ACCESS_KEY_ID = 'x'
        
        AWS_SECRET_ACCESS_KEY = 'x'
        
        DATABASE_URL = 'x'

- If you want to use AWS to host your static folder like I have, you will need to create a bucket in aws's s3 and edit the variables in settings.py.

*Note in order to push the static files to your s3 bucket, you must run this command: 

  python3 manage.py collectstatic

- In order to update the database with the models created from this project, you will need to run the following commands to update the postgresql database: 

 python3 manage.py makemigrations
 
 python3 manage.py migrate

In order to run the site locally, you can use the clone this site by using the following link in your terminal: `git clone https://github.com/Novicetheaf/Honda-Motorcycle-Ecommerce-Project.git` To remove any connections with Github repository use the following in your terminal: `git remote rm origin`.  

If you need anymore help in cloning this repo, then go to GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).


- Create an env.py file in the projects base directory, then enter input the following:

       os.environ.setdefault("SECRET_KEY", "x")
       
       os.environ.setdefault("STRIPE_PUBLISHABLE", "x")
       
       os.environ.setdefault("STRIPE_SECRET", "x")
       
       os.environ.setdefault("AWS_ACCESS_KEY_ID", "x")
       
       os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "x")
       
*Note:
        By default django will create a local sqlitedb, you can however choose one from heroku, go to resources,
        then type Heroku Postgres in the addons input field.
        
        To link the database use the following in your settings.py file:
        
        os.environ.setdefault("DATABASE_URL", "X")


## Database Schema for custom models

### Motorycles

|  |  Motorcycle |
| --- | --- |
| name | CharField(max_length=199, default='') | 
| engine | IntegerField(default='') |
| weight | IntegerField(default='') |
| description | TextField(max_length=350) |
| price | DecimalField(max_digits=9, decimal_places=2) |
| image | ImageField(upload_to='images') |

### Shop Reviews

|  |  ShopReview |
| --- | --- |
| review_title | CharField(max_length=100) | 
| reviewer_name | CharField(default='', max_length=50) |
| review_description | TextField(max_length=200) |
| review_date | DateTimeField(blank=True, null=True, default=timezone.now) |
| review_views | IntegerField(default=0) |

<hr>

## Credits

### Media
I used [Pinterest](https://www.pinterest.com/) for my background image, and other motorcycle images.

### Acknowledgements

I used [MCN's site](https://www.motorcyclenews.com/) for motorcycle stats.

Modal Contact Form outer sections Reference can be found [here](https://mdbootstrap.com/docs/jquery/modals/forms/)

Bootstrap code I used to look up for reference purposes, I used [bootstrap.com](https://getbootstrap.com/)

Some of the core apps, such as the accounts app are based off the Ci documentation on github & tutorials on [Ci's site](https://courses.codeinstitute.net/courses/)

**This project is for educational purposes.** 

[![Build Status](https://travis-ci.org/Novicetheaf/Honda-Motorcycle-Ecommerce-Project.svg?branch=master)](https://travis-ci.org/Novicetheaf/Honda-Motorcycle-Ecommerce-Project)
