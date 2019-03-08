#Keywords: python, django, bootstrap, javascript, jquery </br>

- This simple full stack website is a way for people to have a very quick and easy personable website that customize your own portfolio with a simple logo, and some description text in a nicely-formatted manner.  </br>
- You can now create your own personal page easily.  </br>

#There are two main content in app:

#1) Portfolio Part:
- This part have been design by single-page design and it helps you to describe yourself and tell about your activities.
</br>
![Screenshot](static/myApp/media/readme/readme1.png)
</br></br>
- You can share your CV by using "about me" section
</br>
![Screenshot](static/myApp/media/readme/readme2.png)
</br></br>
- People can send email to you by using "contact me" section. 
</br>
![Screenshot](static/myApp/media/readme/readme3.png)
</br></br>

#2) Blog Part:
- You can now publish your posts and articles with simple, elegant design.
</br>
![Screenshot](static/myApp/media/readme/readme4.png)
</br></br>
- Only authors can publish a post(django authentication).
</br>
- Users can comment on posts easily.
</br>
![Screenshot](static/myApp/media/readme/readme5.png)
</br></br>
- Sqlite database is used to store posts, authors and comments.
</br>
#To run </br>
`python manage.py makemigrations`
`python manage.py migrate`
`pyton manage.py runserver`
