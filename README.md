# ShelfieChallenge API V1
### Built with Django-Rest-Framework

## Table of Contents:
* [Admin Panel](#Admin)
* [Authentication](#Authentication)
* [Media Storage](#Media)
* [Setup](#Setup)

## Models:
* [ShelfieChallenge](#ShelfieChallenge)
* [ShelfieGame](#ShelfieGame)
* [ShelfiePost](#ShelfiePost)
* [ShelfiePrize](#ShelfiePrize)
* [ShelfieTeam](#ShelfieTeam)
* [ShelfieUser](#ShelfieUser)



## <a name="Admin">Admin:</a>

Access the admin panel at /admin
* Must be either staff or superuser to login
* Set permissions
* Create, Retrieve, Update, Destroy records



## <a name="Authentication">Authentication:</a>

Using [django-rest-knox](https://github.com/James1345/django-rest-knox) Token Authentication

### Workflow
1. Authenticate user (either Login or Create route)
2. Request Knox Token
3. Receive Knox Token and user object
4. Use Knox Token as Authorization header in future requests
   Example Auth header: { headers: { Authorization: 'Token <knox_token>' } }

### Auth Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | -------------- |
| api/v1/login              | POST   | { 'username', 'password' } | { 'token', 'user' } |
| api/v1/logout             | POST   | 'knox_token' | Logout user |
| api/v1/logoutall          | ---    | ---    | ---            |



## <a name="Media">Media Storage:</a>
### Amazon S3
* Bucket Name: "shelfie-challenge"
* Region: US West (N. California)
* File Tree:
   * shelfie-challenge
      * posts
         * photos
         * videos
      * teams
         * logos

### Posts
* Uploaded by front-end
* Url stored in ShelfiePost.Post
* Naming convention:
   * '<random_game_id>-<randomly_generated_id>'

### Teams
* Logos uploaded through form in admin panel
   * Using 'storages.backends.s3boto.S3BotoStorage'
   * Can't be uploaded from front-end



## <a name="Setup">Setup:</a>
Clone repository:
```
git clone https://github.com/KyleLawson16/shelfie-backend.git
```

Create a virtual environment and activate it:
```
virtualenv env
source env/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Initialize database:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver
```



## <a name="ShelfieChallenge">ShelfieChallenge</a>
### ShelfieChallenge.Challenge Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_challenge_id       | string | *(PK) |
| name                      | string | *Name of challenge |
| description               | string | *Description of challenge |
| point_value               | integer | *Point value of challenge |

### ShelfieChallenge Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/challenges         | GET    | None   | list of challenges |
| api/v1/challenges/<random_challenge_id> | GET | None | challenge |



## <a name="ShelfieGame">ShelfieGame</a>
### ShelfieGame.Game Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_game_id            | string | *(PK) |
| date                      | date/time | *Date and time of game |
| home_team                 | FK(ShelfieTeam.Team) | Home team in game |
| away_team                 | FK(ShelfieTeam.Team) | Away team in game |
| organization              | FK(ShelfieTeam.Team) | Organization in charge of game |
| location                  | string | Location of game (arena, city, state) |
| challenges                | ManyToMany(ShelfieChallenge.Challenge) | List of challenge objects available in game |
| prizes                    | ManyToMany(ShelfiePrize.Prize) | List of prize objects available in game |
| fans                      | ManyToMany(ShelfieUser.User) | List of user objects that joined game |

### ShelfieGame Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/games              | GET    | None   | list of games |
| api/v1/games/<random_game_id> | GET | None | game |
| api/v1/games/<random_game_id> | PUT | 'random_user_id' | adds user to Game.fans |
| api/v1/games/<random_game_id>/leaderboard | GET | None | { 'random_user_id', 'username', 'points' } in descending order of pts |



## <a name="ShelfiePost">ShelfiePost</a>
### ShelfiePost.Post Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_post_id            | string | *(PK) |
| user                      | FK(ShelfieUser.User) | *User post belongs to |
| game                      | FK(ShelfieGame.Game) | *Game the post was created for |
| challenge                 | FK(ShelfieChallenge.Challenge) | *Challenge the post was completing |
| is_video                  | boolean | *Specifies whether or not the post was an image or video |
| media_url                 | string | *Path to image/video |
| caption                   | string | Caption of post |
| timestamp                 | date/time | (auto) Date when post was created |
| likes                     | ManyToMany(ShelfieUser.User) | List of user objects that liked post |

### ShelfiePost Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/posts              | GET    | None   | list of posts |
| api/v1/posts/create       | POST   | **required:** { 'user', 'game', 'challenge', 'is_video', 'media_url' } **optional:** { 'caption' } | None |
| api/v1/posts/<random_post_id> | GET | None | post |
| api/v1/posts/<random_post_id>/like/add | POST | 'random_user_id' | adds user to Post.likes |
| api/v1/posts/<random_post_id>/like/delete | POST | 'random_user_id' | removes user from Post.likes |




## <a name="ShelfiePrize">ShelfiePrize</a>
### ShelfiePrize.Prize Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_prize_id           | string | *(PK) |
| name                      | string | *Name of prize |
| description               | string | *Description of prize |
| winner                    | FK(ShelfieUser.User) | User that won the prize |

### ShelfiePrize Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/prizes             | GET    | None   | list of prizes |
| api/v1/prizes/<random_prize_id> | GET | None | prize |




## <a name="ShelfieTeam">ShelfieTeam</a>
### ShelfieTeam.Team Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_team_id            | string | *(PK) |
| name                      | string | *Name of team |
| location                  | string | Location of team |
| logo_url                  | image  | path to team's logo image |
| point_of_contact          | string | (Will be updated to a Foreign Key) |

### ShelfieTeam Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/teams              | GET    | None   | list of teams |
| api/v1/teams/<random_team_id> | GET | None  | team |




## <a name="ShelfieUser">ShelfieUser</a>
### ShelfieUser.User Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | ------ | :--------------------------------------- |
| random_user_id            | string | *(PK) |
| username                  | string | *Username of user |
| email                     | string | *Email address of user |
| first_name                | string | *First name of user |
| middle_name               | string | Middle name of user |
| last_name                 | string | *Last name of user |
| phone_number              | string | Phone number of user |
| is_active                 | boolean | *Specifies whether or not the user is active |
| is_staff                  | boolean | *Specifies whether or not the user has staff permissions |
| date_joined               | date/time | (auto) Date of user creation |
| gender                    | string | Choices: (male, female) |

### ShelfieUser Routes

| Route                     | Type   | Takes  | Response       |
| ------------------------- | :----: | ------ | ------------ |
| api/v1/create-user        | POST   | **required:** { 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'is_staff', 'is_superuser' } **optional:** { 'phone_number', 'middle_name', 'gender' } |
| api/v1/users              | GET    | None   | list of users |
| api/v1/users/<random_user_id> | GET | None  | user |
| api/v1/users/logged-in-user | GET  | None   | user |
| api/v1/profile            | ---    | ---    | ---          |
| api/v1/profile/change-photo | ---  | ---    | ---          |
| api/v1/validate/user      | ---    | ---    | ---          |
