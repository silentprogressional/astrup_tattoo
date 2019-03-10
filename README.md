**Django Personal Blog Web App**

**#Keywords: python, django, bootstrap, javascript, jquery **



This project is a way for people to have their own web page that customizes their portfolio and helps them to share their posts in a nicely-formatted manner.</br>
The application contains two section:

#1) Portfolio Part:
- This part have been design by single-page design and it helps you to describe yourself and tell about your activities.</br>
![Screenshot](static/myApp/media/readme/readme1.png)
</br></br>
- You can share your CV by using "about me" section</br>
![Screenshot](static/myApp/media/readme/readme2.png)
</br></br>
- People can send email to you by using "contact me" section. </br>
![Screenshot](static/myApp/media/readme/readme3.png)
</br></br>

#2) Blog Part:
- You can now publish your posts and articles with simple, elegant design.</br>
![Screenshot](static/myApp/media/readme/readme4.png)
</br></br>
- Only authors can publish a post(django authentication).</br>
- Users can comment on posts easily.</br>
![Screenshot](static/myApp/media/readme/readme5.png)
</br></br>
- Sqlite database is used to store posts, authors and comments.
</br>
#To run </br>
`python manage.py makemigrations` </br>
`python manage.py migrate` </br>
'python manage.py loaddata admin.json' </br>
`pyton manage.py runserver` </br>

