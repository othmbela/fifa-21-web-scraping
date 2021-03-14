# FIFA 21 Scraper

This repository contains a dataset of FIFA 2021 Player ratings scraped from web.


## Content

This dataset has the following properties:

* Every player in FIFA 21.
* Player personal information such as Nationality, Club, Age, Wage, Salary.
* Attributes based on actual data.

```python
>>> df.columns
Index(['Short Name', 'Full Name', 'Nationality', 'Age', 'Overall',
       'Potential', 'Club', 'Height', 'Weight', 'Foot', 'Best Postion',
       'Value', 'Wage', 'VIT', 'TIR', 'PAS', 'DRI', 'DEF', 'PHY'],
      dtype='object')
```

**Below**: *Screenshot from the web site that I have scraped*

![alt text](/assets/images/players_image.png "Browsable API")


## Installation
* If you want to run the REST API, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Then, clone the repo to your PC
    ```bash
        $ git clone https://github.com/othmbela/fifa-21-web-scraping.git
    ```

* #### Dependencies
    1. Cd into your the cloned repository as such:
        ```bash
            $ cd fifa-21-web-scraping
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python3 -m venv venv
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```


* #### Run It
    Fire up the program using this one simple command:
    ```bash
        $ python main.py
    ```


## Files and Folders structure

```
├── .gitignore
├── logging.conf
├── main.py
├── requirements.txt
├── assets
│   └── images
├── data
├── logs
├── scraper
│   ├── __init__.py
│   ├── scraper_utils.py
│   └── scraper.py
└── utils
    ├── __init__.py
    ├── multi_threading.py
    └── save_data.py
```


## Acknowledgements

The data has been scraped from the https://sofifa.com website.


## Author

**Othmane Belarbi**
