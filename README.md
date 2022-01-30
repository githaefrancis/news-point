# News Point

## Description
This is a Flask application that displays News from different sources provide by News Api. A user can view News by a news source or by category. The application allows the user to read the full News article in the source website.


## Author

Francis Githae

# Technologies

Python 3.8.10
Flask
Bootstrap
## Dependencies

autopep8==1.6.0
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
pycodestyle==2.8.0
python-dateutil==2.8.2
six==1.16.0
toml==0.10.2
Werkzeug==2.0.2


## Setup and Installation

1. Clone the repository

```bash
git@github.com:githaefrancis/news-point.git
```

2. Navigate to project folder

```bash
cd news-point
```

3. Install the dependencies

4. Create the .env variables in the root folder
```bash
touch .env
```
Create the environment  variables

export NEWS_BASE_URL='https://newsapi.org/v2/'
export NEWS_API_KEY='<Your Api Key>'

4. Grant the python executable permissions

```
chmod +x start.sh
```
5. Run the application

```
./start.sh
```

## Contact
Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae