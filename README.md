# ShelfieChallenge API V1
### Built with Django-rest-framework

## Models:
* [ShelfieUser](#ShelfieUser)
* [ShelfieTeam](#ShelfieTeam)
* [ShelfieChallenge](#ShelfieChallenge)
* [ShelfiePrize](#ShelfiePrize)
* [ShelfiePost](#ShelfiePost)



## <a name="ShelfieChallenge">ShelfieChallenge</a>
### ShelfieChallenge.Challenge Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | :----: | :--------------------------------------- |
| random_challenge_id       | string | *(PK) |
| name                      | string | *Name of challenge |
| description               | string | *Description of challenge |
| point_value               | integer | *Point value of challenge |

### ShelfieChallenge Routes

| Route                     | Type   | Takes  | Output       |
| ------------------------- | :----: | :----: | :----------: |
| api/v1/challenges         | GET    | None   | list of challenges |
| api/v1/challenges/<random_challenge_id> | GET | None | challenge |



## <a name="ShelfieGame">ShelfieGame</a>
### ShelfieGame.Game Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | :----: | :--------------------------------------- |
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

| Route                     | Type   | Takes  | Output       |
| ------------------------- | :----: | :----: | :----------: |
| api/v1/games              | GET    | None   | list of games |
| api/v1/games/<random_game_id> | GET | None | game |
| api/v1/games/<random_game_id> | PUT | 'random_user_id' | adds user to Game.fans |
| api/v1/games/<random_game_id>/leaderboard | GET | None | { 'random_user_id', 'username', 'points' } in descending order of pts |




## <a name="ShelfieUser">ShelfieUser</a>
### ShelfieUser.User Fields

| Field                     |  Type  | Description (* indicates required)       |
| ------------------------- | :----: | :--------------------------------------- |
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

| Route                     | Type   | Takes  | Output       |
| ------------------------- | :----: | :----: | :----------: |
| api/v1/create-user        | POST   | **required:** { 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'is_staff', 'is_superuser' } **optional:** { 'phone_number', 'middle_name', 'gender' } |
| api/v1/users              | GET    | None   | list of users |
| api/v1/users/<random_user_id> | GET | None  | user |
| api/v1/users/logged-in-user | GET  | None   | user |
| api/v1/profile            | ---    | ---    | ---          |
| api/v1/profile/change-photo | ---  | ---    | ---          |
| api/v1/validate/user      | ---    | ---    | ---          |
