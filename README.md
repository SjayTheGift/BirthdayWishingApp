
# BirthDay Wishing

Send user a birthday a birthday once a day has a cron job that checks
for employess who have birthday and send them a birthday wish.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`EMAIL_HOST_USER`

`EMAIL_HOST_PASSWORD`

Please note will need to create an gmail account for yourself to use the email 
then add the email and password into the env file.




## Run Locally

Clone the project

```bash
  git clone https://github.com/SjayTheGift/BirthdayWishingApp.git
```

Go to the project directory

```bash
  cd BirthdayWishingApp
```

Create virtual enviroment

```bash
  python -m venv venv
```

Start virtual enviroment

widowns

```bash
  venv\Scritps\activate
```
Mac

```bash
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Get employees data from API and write it into our database

```bash
  python manage.py download_employees_api
```

Run the script

```bash
  python manage.py runserver --noreload
```

