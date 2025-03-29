# The Wave | High-End Seafood with a view

![image](https://github.com/user-attachments/assets/20fa747d-653c-47a9-b849-ea847c23a97a)

Developer - Lewis Bull

[View Live Website Here](https://cl-pp4-the-wave-76e93eea9754.herokuapp.com/)

(Cntrl + Click to open in a new tab)

## About
The Wave is a fictisious buissiness beased around high end seafood dining, the style was chose to imitate michilen star seafood restaurants. Users can book a table, view the extensive food and drinks menu, read a blog posted by the website admins, and creadt an account to see their bookings and add comments on to blog posts

## User Goals

 - To be able to book a table
 - To be able to view my bookings
 - To be able to cancel/edit my bookings
 - To be able to view the menus
 - To be able to view the blog posts
 - To be able to contact the restaraunt from the website

## Site Owner Goals
 - To have a place where customers can book tables
 - To attract more business via the website
 - To allow users to use the wesbite on all devices
 - To have a recogniseable business brand

## User Experience

### Target Audience

 - Users that wish to dine at a high end restaurent
 - Users that enjoy seafood
 - Wealthy individuals
 - Couples on anniversarys/Birthday dinners
 - Past customers of the business

### User Requirements and Expectations

 - Good Design
 - Fully Responsive
 - Accessible to all
 - Contact information
 - Location of the business
 - Social Media links

## User Stories

### Users

1. As a User, I can register an account to store my details for faster bookings in the future.
2. As a User, I can view my booking details so I can easily check the date and time of my reservation.
3. As a User, I can cancel my reservation so I can free up the table if my plans change.
4. As a User, I can view the business hours and contact details to know how to reach them.
5. As a User, I can book a table by selecting an available date and time.
6. As a User, I can navigate the website easily.
7. As a User, I can sign in to access booking features and manage my reservations.
8. As a User, I can check if I am logged in to know whether I can make a reservation or manage an existing one.
9. As a User, I can browse the food and drink menu to decide what I want before booking a table.
10. As a User, I can update my booking to select a new available time if my plans change.
11. As a User, I can not book a past date to ensure that my reservation is valid.
12. As a User, I can not select a time slot that has already been booked to avoid double bookings.
13. As a User, I can receive notifications to confirm whether my booking action was successful.
14. As a User, I can access the site’s blog to read helpful articles and updates.
15. As a User, I can view blog posts in a paginated format to make browsing easier.

### Site Owner / Admin / Authorised User

16. As an Admin, I can log in to manage the back end of the site.
17. As an Admin, I can create, update, and delete items from the food and drink menu to keep our offerings current.
18. As an Admin, I can manually add bookings for customers who call or email the business.
19. As a Site Owner, I can ensure the site is fully responsive to provide a seamless experience for customers.
20. As an Admin, I can filter bookings by date to easily see reservations for any given day.
21. As an Admin, I can validate data entered on the site to ensure accuracy and prevent errors.
22. As an Admin, I can accept or reject bookings to avoid overbooking or double bookings.
23. As an Admin, I can search through bookings and menus to quickly find the information I need.
24. As an Admin, I can log in to manage and update the site’s backend features.
25. As an Admin, I can add or remove food and drink items from the menu to update what is available.

## Design

I chose light colors to relate to the area of the restaurant and the feel of the restaurant. This is because the restauratnt is an outside restaurant and is on the seafront and therefore would be bright and clear.

The colors I chose were from different forumsn such as Stack Overflow to see black, white and grey colors that were not to sharp for the website

Color Palette

 - Image Here(Later)

### Fonts

I chose to use Monterrat font from [Google Fonts](https://fonts.google.com/specimen/Montserrat) as it is a common font used by businesses and looks proffessional

### Structure

#### Pages

The site was designed based off of other common layouts for websites, for example the navigation bar is along the top of the page and a hamburger menu will appear on smaller screens.
The Footer has all of my social media links so that the user can visit any of my social medias if they wish.

The Site has the following pages:
 - **The homepage** features cards that let users book a table, browse the food menu, or explore the drinks menu.
 - **The food menu** displays a categorized list of available dishes from the database, sorted into starters, mains, and desserts.
 - **The drinks menu** showcases the current selection of beverages, organized by type.
 - **The blog page** presents a paginated list of blog posts by admins or authorized users, with four posts per page.
 - **The blog details page** allows users to read a selected blog post. Logged-in users can leave comments, which require approval before being published.
 - **The booking page** enables registered users to reserve a table, specifying the guest count, preferred date, time, and table location.
 - **The "My Bookings" page** displays all reservations made by the user, with past bookings automatically marked as expired.
 - **The edit booking** feature allows users to modify the date, time, table, and guest count of an existing reservation.
 - **The cancel booking** option lets users remove a reservation, which is then deleted from the database.
 - **The contact page** allows registered users to send a direct message. Alternatively, users can reach out via the provided email, phone number, or physical address.
 - **The login/logout page** functionality allows users to sign in to make, view, edit, and cancel bookings.
 - **The registration page** enables new users to sign up and access the booking system.

## Database
The Project was built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

### User Model
The User Model contains the following:

- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

### FoodItem Model
The FoodItem Model contains the following:

- food_id
- food_name
- description
- price
- available

### DrinkItem Model
The DrinkItem Model contains the following:

- drink_id
- drink_name
- description
- price
- available

### Table Model
The Table Model contains the following:

- table_id (PrimaryKey)
- table_name
- max_seats
- available

### Booking Model
The Booking Model contains the following:

- booking_id (PrimaryKey)
- created_date
- requested_date
- requested_time
- table (ForeignKey)
- guest (ForeignKey)
- seats
- guest_count

### Post Model
The Post Model contains the following:

- title
- post_id (PrimaryKey)
- author (ForeignKey)
- created_date
- updated_date
- content
- featured_image
- excerpt
- slug
- status

### Comment Model
The Comment Model contains the following:

- post (ForeignKey)
- name
- email
- body
- created_date
- approved
- Meta: created_on

### ContactUs Model
The ContactUs Model contains the following:

- contact_id (PrimaryKey)
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- body


## Technologies Used

### Languages and Frameworks

 - HTML
 - CSS
 - JavaScript
 - Python
 - Django

### Libraries and Tools

- Google Fonts
- Bootstrap
- Heroku Platform
- jQuery
- Chrome Dev Tools
- Font Awesome
- Git
- Postgres
- Am I Responsive
- Cloudinary
- GitHub
- Summernote
- Balsamiq
- Favicon.io
- Validation
   - 

## Features

### Home Page

- My home page includes a navigation bar, the main body which has a carosel with 3 images, cards to click on for the user to be taken to the booking page, food menu and drinks menu, and a footer with my social medias

### Logo

- Custom Logo for my business
- Fully responsive

### Navigation Bar

- Fullt Responsive NavBar
- Has a Custom Logo on the left
- On smaller screens it switches to a hamburger menu
- Hides the register/Login page if the user is logged in already
- Displayed Across all of my pages

### Footer

- Contains all of my social medias as buttons
- Fully responsive
- Displayed across all of my pages

### Register Page

- Allowes users to register a new account
- Username and password are required for the user to add but the email is optional as indicated by the asterisks (*)
- Fully Responsive

### Login Page

- Users can login to their account on this page
- The username and password need to match to an account on the database

### Booking Page

- Users can book a table using the online booking form
- The form takes in the users name, phone number, email, guest count, the table they would like, the date and the time that they would like
- Users cannot double book at the same time
- Messages are displayed if the data is not valid
- Users cannot book before the present day

### My Bookings Page

- Allows the user to see all of their bookings in a clear layout
- If any bookings are before the present day the booking will automatically disappear
- Status for the booking is displayed to let the user know where their booking is at

### Edit Booking Page

- Allows the user to edit their bookings
- The User can edit the name, time and date, email, type of table and phone number

### Cancel Booking Page

- Allows the user to cancel their booking if they wish
- When Clicked it will ask the user if they are sure that they would like to cancel

### Food Menu Page

- Allows the user to see all of the food that is available on the menu
- Menu is seperated by starters, mains and desserts
- Items are created on the admin panel, the items need a title, description and a price

### Drinks Menu Page

- Allows the user to see all of the drinks that are available on the menu
- Menu is seperated by Wines, Beers and Cocktails
- Items are created on the admin panel, the items need a title, description and a price

### Blog Page

- The blog page displays posts made by staff members
- The page can display 4 posts per page
- The user can click on each title to open the blog details

### Blog Details Page

- When clicked opens the blog details
- Expands with the image at the top and a description/details of the post underneath
- Registered users only can comment on the blog

### Blog Comments

- Comments made are set to a pending status to ensure that the admins have control over what is displayed
- Staff are able to approve or remove comments on the admin panel

### Contact Us Page

- Users can send a message to the staff from the message box
- The message has a name, phone number and email of the user submitting the message
- Underneath the contact page there is a google maps embedded with the address 

## Testing

### Manual Testing

1. As a User, I can register an account to store my details for faster bookings in the future.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the register link in the nav bar|The register page will load|Works as expected|
|Fill in the information in the register page|The website will create an account with the information|Works as expected|

2. As a User, I can view my booking details so I can easily check the date and time of my reservation.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the my bookings link in the nav bar|The my bookings page loads with all the users bookings|Works as expected|

3. As a User, I can cancel my reservation so I can free up the table if my plans change.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on My Bookings and click cancel on the booking that needs to be canceled|The cancel booking page will load|Works as expected|
|Click on yes when asked if sure to cancel the booking|The booking will be cancelled and taken off of the my booking page|Works as expected|

4. As a User, I can view the business hours and contact details to know how to reach them.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the contact us page and scroll down|The times the restaurant is open and the contact details|Works as expected|

5. As a User, I can book a table by selecting an available date and time.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the book link in the nav bar and fill out the information such as date and time|Nav bar works as expected and the booking will be created correctly|Works as expected|

6. As a User, I can navigate the website easily.

|Step|Expected Outcome|Result|
|---|---|---|
|Click on the home link in the nav bar|The homepage will load|Works as expected|
|Click on the menus link in the nav bar anmd select the food menu|Food Menu will load|Works as expected|
|Click on the menus link in the nav bar and select the drinks menu|Drinks Menu will load|Works as expected|
|Click on the blog link in the nav bar|The blogs page will load|Works as expected|
|Click on a blog post on the blog page|The blog details page will load|Works as expected|
|Click on the book link in the nav bar|The booking page will load|Works as expected|
|Click on the Contact us link in the nav bar|The contact us page will load|Works as expected|
|Click on the My bookings link in the nav bar|The My bookings page will load|Works as expected|
|Click on the register link in the nav bar|The register page will load|Works as expected|
|Click on the login page in the nav bar|The Login page will load|Works as expected|
|Click on the Logout page in the nav bar|The logout page will load|Works as expected|


7. As a User, I can sign in to access booking features and manage my reservations.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the login link in the nav bar and login with a registered account|If the user has created an account the login will work|Works as expected|

8. As a User, I can check if I am logged in to know whether I can make a reservation or manage an existing one.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the login link in the nav bar, and login|If logged in the login and register button will disapper and the logout button will appear|Works as expected|

9. As a User, I can browse the food and drink menu to decide what I want before booking a table.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the menus link in the nav bar anmd select the food menu|Food Menu will load|Works as expected|
|Click on the menus link in the nav bar and select the drinks menu|Drinks Menu will load|Works as expected|

10. As a User, I can update my booking to select a new available time if my plans change.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the my bookings link in the nav bar and click the edit button|The edit booking page will open and the user can edit their times or date|Works as expected|

11. As a User, I can not book a past date to ensure that my reservation is valid.
|Step|Expected Outcome|Result|
|---|---|---|
|Create a booking and attempt to put the date before the present day|A message will appear telling the user this is an invalid day|Works as expected|

12. As a User, I can not select a time slot that has already been booked to avoid double bookings.
|Step|Expected Outcome|Result|
|---|---|---|
|Create a booking with a time and date, then attempt to create another one|An error will pop up letting the user know that they have already booked for this date and time|Works as expected

13. As a User, I can receive notifications to confirm whether my booking action was successful.
|Step|Expected Outcome|Result|
|---|---|---|

14. As a User, I can access the site’s blog to read helpful articles and updates.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the blog link in the nav bar|The blogs page will load|Works as expected|

15. As a User, I can view blog posts in a paginated format to make browsing easier.
|Step|Expected Outcome|Result|
|---|---|---|
|Click on the blog link in the nav bar|The blogs page will load|Works as expected|

16. As an Admin, I can log in to manage the back end of the site.
|Step|Expected Outcome|Result|
|---|---|---|
|Visit the admin page at https://cl-pp4-the-wave-76e93eea9754.herokuapp.com/admin/|Enter the admin credentials and gain access to the backend|Works as expected|

17. As an Admin, I can create, update, and delete items from the food and drink menu to keep our offerings current.
|Step|Expected Outcome|Result|
|---|---|---|
|In the admin page, click on food or drink items and click add item|The admin can create a new food or drink item|Works as expected|

18. As an Admin, I can manually add bookings for customers who call or email the business.
|Step|Expected Outcome|Result|
|---|---|---|
|In the admin page, click on Booking tab and click create booking|The admin can create a new booking for a user with a time date and table|Works as expected|

19. As a Site Owner, I can ensure the site is fully responsive to provide a seamless experience for customers.
|Step|Expected Outcome|Result|
|---|---|---|
|Go to the developer tools in google chrome and swap the dimentions to responsive, shrink the screen size and see if all elements are responsive|The webpage will be responsive|Works as expected|
|Test Screen Size: 200px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 400px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 600px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 800px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 1000px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 1200px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 1400px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 1600px|All elements and webpages are responsive|Works as expected|
|Test Screen Size: 1800px|All elements and webpages are responsive|Works as expected|

20. As an Admin, I can filter bookings by date to easily see reservations for any given day.
|Step|Expected Outcome|Result|
|---|---|---|
|Go to the admin page: https://cl-pp4-the-wave-76e93eea9754.herokuapp.com/admin/ and click on booking, in the right there is a filter|The filter allows the admins to filter by date|Works as expected|

21. As an Admin, I can validate data entered on the site to ensure accuracy and prevent errors.
|Step|Expected Outcome|Result|
|---|---|---|
|From the booking page enter a phone number that is too long or short|Error message will appear|Works as expected|
|From the booking page enter a date that is already booked|Error message will appear|Works as expected|
|From the booking page enter a date that is before the current day|Error message will appear|Works as expected|
|From the booking page leave the phone number blank|Error message will appear|Works as expected|

22. As an Admin, I can accept or reject bookings to avoid overbooking or double bookings.
|Step|Expected Outcome|Result|
|---|---|---|
|Go to the booking tab on the admin page, access a booking and change the status|The admin can reject or confirm a booking|Works as expected|

23. As an Admin, I can search through bookings and menus to quickly find the information I need.
|Step|Expected Outcome|Result|
|---|---|---|
|Go to the booking tab on the admin page, there are filter to let the admins access information quickly|The admin can filter the bookings|Works as expected|
|Go to the Food items or drink items tab on the admin page, there are filter and a seach bar to let the admins access information quickly|The admin can filter the bookings|Works as expected|

24. As an Admin, I can log in to manage and update the site’s backend features.
|Step|Expected Outcome|Result|
|---|---|---|
|Access the admin page at https://cl-pp4-the-wave-76e93eea9754.herokuapp.com/admin/ and enter the admin credentials|The admin can login to access the sites backend|Works as expected|

25. As an Admin, I can add or remove food and drink items from the menu to update what is available.
|Step|Expected Outcome|Result|
|---|---|---|
|Go to the food or drinks items tabs on the admin page, click on an item|There is a button the admins can toggle to say if an item is available or not|Works as expected|
