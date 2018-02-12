# ShelfieChallenge API V1
### Built with Django-rest-framework

## Models:
* [ShelfieUser](#ShelfieUser)
* [ShelfieTeam](#ShelfieTeam)
* [ShelfieChallenge](#ShelfieChallenge)
* [ShelfiePrize](#ShelfiePrize)
* [ShelfiePost](#ShelfiePost)

## <a name="ShelfieUser">ShelfieUser</a>
### ShelfieUser.User Fields

| Property                  |  Type  | Description (* indicates required)       |
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

### Routes

| Route                     | Type   | Takes  | Output       |
| ------------------------- | :----: | :----: | :----------: |
| api/v1/create-user        | POST   | { 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'is_staff', 'is_superuser' } optional: ( 'phone_number', 'middle_name', 'gender' ) |
| api/v1/users              | GET    |        | list of user objects |
| api/v1/users/<random_user_id> | GET |       | specific user info |
| api/v1/users/logged-in-user | GET  |        | user object of logged in user |
| api/v1/profile            | ---    | ---    | ---          |
| api/v1/profile/change-photo | ---  | ---    | ---          |
| api/v1/validate/user      | ---    | ---    | ---          |
