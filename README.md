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
6. As a User, I can navigate the website easily using a navbar, footer, and social media icons.
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

user_id
password
last_login
is_superuser
username
first_name
last_name
email
is_staff
is_active
date_joined

### FoodItem Model
The FoodItem Model contains the following:

food_id
food_name
description
price
available

### DrinkItem Model
The DrinkItem Model contains the following:

drink_id
drink_name
description
price
available

### Table Model
The Table Model contains the following:

table_id (PrimaryKey)
table_name
max_seats
available

### Booking Model
The Booking Model contains the following:

booking_id (PrimaryKey)
created_date
requested_date
requested_time
table (ForeignKey)
guest (ForeignKey)
seats
guest_count

### Post Model
The Post Model contains the following:

title
post_id (PrimaryKey)
author (ForeignKey)
created_date
updated_date
content
featured_image
excerpt
slug
status

### Comment Model
The Comment Model contains the following:

post (ForeignKey)
name
email
body
created_date
approved
Meta: created_on

### ContactUs Model
The ContactUs Model contains the following:

contact_id (PrimaryKey)
name (ForeignKey)
email (ForeignKey)
phone (ForeignKey)
body


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

### Logo

### Navigation Bar

### Footer

### Register Page

### Login Page

### Booking Page

### My Bookings Page

### Edit Booking Page

### Cancel Booking Page

### Food Menu Page

### Drinks Menu Page

### Blog Page

### Blog Details Page

### Blog Comments

### Contact Us Page
