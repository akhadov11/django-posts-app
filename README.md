# django-posts-app
Test assignment for InfoTech internship 

###local installation and run###
1. git clone https://github.com/akhadov11/django-posts-app.git
2. pip install -r requirements.txt
3. python manage.py makemigrations + python mange.py migrate
4. python manage.py runserver


###functionality description###
On the home sreen a list of posts is displayed. There is also a button to add a post. All users can add posts.

Moreover, there is an authentication system. You can sign up and then log in to the system. 
Now your posts will include your username in a new field for author`s name. You can get all your posts by pressing the corresponding button(my posts).
In addition to this, users can add images to their publications.

Also, there are various filters ont the posts list page. For example, you can sort the posts in descending or ascending(by default) oreder.
What`s more, it is possible to get posts published during last 24 hours.

###deploy###
The app is deployed to Heroku. Link - "http://posts-app-infotech.herokuapp.com/"


###future plans###
1. dockerize and redeploy the app
2. make the frontend fancier 
3. improve the auth system(add roles, permissions etc.)
