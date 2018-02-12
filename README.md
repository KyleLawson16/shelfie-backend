# ShelfieChallenge API V1
### Built with Django-rest-framework

## Models:
* [ShelfieUser](#ShelfieUser)
* [ShelfieTeam](#ShelfieTeam)
* [ShelfieChallenge](#ShelfieChallenge)
* [ShelfiePrize](#ShelfiePrize)
* [ShelfiePost](#ShelfiePost)

## ShelfieUser

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
