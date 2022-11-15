# **XBOX ANTICIPATOR**

## **INTRODUCTION**
This fourth Portfolio Project is the product of knowledege and techniques combined from all modules of the Code Institute Full Stack Developer Course to date, culminating in the creation of this Full Stack Framework Django project. The Application will allow an admin user to store and manipulate data records and also allow nominated staff users to create, read, update and delete additional data records for the **Xbox Anticipator** website.

A live version of the site can be found [here](https://pp04-xbox-anticipator.herokuapp.com/)

![site preview](readme_media/)

### **PROJECT FUNCTIONALITY**
The application uses Django 3 to encourage rapid development, by following a model-template-view architecture pattern.
Alongside using Django, sqlite was used in the Project's inception phase as a test database for local testing. Sqlite is self-contained highly reliable, SQL database engine that features all the normal relational database management. Later, development was switched PostGreSQL (aka Postgres), to ensure any data entered was visible in the deployed application. Postgres is open source and boosts a fully technical and easy to use Object relational database management system.
The project is version controlled via Git & Github and is deployed via Heroku. All environment variables & secret variables are stored in an env.py file, which is then held in a git-ignored file, ensuring project integrity is held to a high secure present day and project requirements standard.

Using Django and the above Database methods the site owner, as an administrator for the application, has complete access to a custom Admin dashboard where they can Create, Read, Update and Delete records for each of the application models as appropriate. An 'is staff' field was included in the User model specifically to allow for the creation of trusted community members as staff, with the ability to maintain, add to and curate the database of upcoming Xbox games the **Xbox Anticipator** site showcases. 

To this end, please ensure when using the site and testing the CRUD funcionality of this application, **please log in as the non-admin, staff-enabled test user, Ben Kenobi:** 

| IS STAFF? | USER | EMAIL | PASSWORD | IS ADMIN? |
|-----|-----|-----|-----|-----|
| YES | Ben Kenobi | **kenobi@test.com** | **1234star4321** | NO |
| NO | Luke Skywalker | skywalker@test.com | 1234star4321 | NO |
| YES | Paul Whiteside | alfa23@test.com | alfa1606 | YES |

----

# **UCD Phase 1: STRATEGY** 

## **PROJECT GOALS**

**title** aims to... 

## **USER GOALS:** 

| ID | CONTENT | SOLUTION |
|-----|-----|-----|
| [#1]

*Unregistered User (Logged Out) Goals* include:
- 
- 
- 

*Registered User (Logged In) Goals* include:
- 
- 
- 

*Site Admin (Superuser) Goals* include:
- 
- 

## **USER EXPECTATIONS:**

- Intuitive/conventional navigation elements
- Familiar and/or easily understandable site structure
- Responsive: access site easily on any device


## **USER STORIES:**

A **GitHub** classic kanban project board was utilised throughout to log all User Stories, track their progress and manage the project. This helped keep focus by moving them, in manageable batches, through *lanes*; from "to do" through "in progress" into "done", as they were completed.

![kanban image](readme_media/)

---- 

# **UCD Phase 2: SCOPE**

### Analysis and grading of *Phase One considerations* allows a simple ***Strategy Table*** to be generated:

| OPPORTUNITY/PROBLEM/FEATURE                | IMPORTANCE | VIABILITY/FEASIBILITY | ID    | 
|--------------------------------------------|:----------:|:---------------------:|:-------
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | A     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | B     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | C     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | D     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | E     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | F     |
| OPPORTUNITY/PROBLEM/FEATURE                | 5          | 5                     | G     |
| TOTAL                                      | 35         | 35                    |       |

![UCD Strategic Trade-Offs: Importance vs Feasibility](readme_media/planning_docs/)

## **STRATEGIC TRADE-OFFS**

Plotting the Strategy Table results provides a visible indication of what is feasibily within the scope of the project at this time. As I am unable to meet all requirements at present, I will aim to provide **Title** initially as an MVP or Minimum Viable Product, therefore, due to time and current-skill limitations the site will be developed in phases:

  ***Initial Phase:*** Delivery of MVP, a fully functioning website, with the exception of
    
  - 
  
  - 

  ***Secondary Phase:*** 
    
  - 

----

# **UCD Phase 3: STRUCTURE**

## **LAYOUT** 

Detail.

![Image](readme_media/planning_docs/)

---- 

# **UCD Phase 4: SKELETON**

## **INITIAL WIREFRAMES**

Following current conventional practice, **nerdOmeter** was designed with a Mobile First approach.

----

![Balsamiq](readme_media/planning_docs/wireframes/)

----

![Balsamiq](readme_media/planning_docs/wireframes/)

All wireframes generated in [Balsamiq](https://balsamiq.com)

---- 

# **UCD Phase 5: SURFACE**

## **DESIGN CHOICES**

## Fonts

All fonts utilised in this project were sourced from and served by [**Google Fonts**](https://fonts.google.com)

- **Heading Font:** *FontName*
  
  *FontName* is...

- **Body Font:** *FontName*

  *FontName* was chosen as a compliment to *FontName*.

![Google Fonts Choices](readme_media/site_screens/pp04_googlefonts.png)

## Colours

Colours utilised were chosen from the palette of the background video, with the **60:40:10 rule** in mind 

  • 60% Background/Primary - **#000000** *ColorName*
  
  • 40% Body Text/Secondary: **#000** *ColorName* chosen for excellent contrast with Primary
  
  • 10% Accent/Tertiary: **#000** *ColorName* chosen as a clean, fresh contrast to Primary and compliment to Tertiary

## Imagery

  • 

----

# **TECHNOLOGIES**

During the course of this project I have utilised the following technologies:

## **LANGUAGES, VERSION CONTROL and FRAMEWORKS**

### HTML, CSS, JS & Python - core languages used to create this CRUD application:
- [**JavaScript**] (https://www.javascript.com/) was used to add interactivity and enrich the User eXperience
- [**HTML5**] (https://html.com/html5/) (HyperText Markup Language) was used for structuring & presenting site content
- [**CSS**] (https://www.css3.info/) (Cascading Style Sheets) was used to provide styling to the HTML
### VERSION CONTROL and FRAMEWORKS:
- [**Python 3**]
- [**Git**] (https://git-scm.com) was used for version control (commit to Git and push to GitHub)
- [**Gitpod**] (https://www.gitpod.io/) was used to write my code; an online IDE linked to the GitHub repository
- [**GitHub**] (https://github.com/) was used to create the repository and store the project's code after being pushed from Git
- [**Bootstrap Framework**] (https://getbootstrap.com/) was used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity
- [**Bootstrap's Imported Javascript & JQuery**] (https://getbootstrap.com/docs/4.3/getting-started/introduction/#js) used for Responsive Navbar expand & collapse, roundSlider and alert messages timeout functionality
- [**Django**] (https://www.djangoproject.com/) was used as the architectural engine following the model-template-view approach
- [**Heroku**] (https://www.heroku.com/) A cloud platform as a service enabling deployment for this CRUD application

## **TOOLS USED**
- [**PostgreSQL**] A free, open-source relational database management system emphasizing extensibility and technical standards compliance
- [**Balsamiq**] (https://balsamiq.com) used to generate mobile and desktop wireframes
- [**favicon**] (https://www.favicon.cc/) was used to create a custom favicon for the project
  ![favicon (readme_media/)]
- [**Google Chrome Dev Tools**] (https://www.google.com/intl/en_uk/chrome/) used to debug & test source code using HTML5 and to test site responsiveness, also assisted in identifying the correct style properties to override some Bootstrap styling
- [**Google Fonts**] (https://fonts.google.com) used for all fonts utilised in the project
- [**amiresponsive**] (http://ami.responsivedesign.is/) used to check how responsive the site is on different devices
- [**Web Page Test**] (https://www.webpagetest.org/) used to test site performance
- [**JSHint**] (https://jshint.com/), [**W3C Markup**] (https://validator.w3.org/) and [**W3C Jigsaw**] (http://jigsaw.w3.org/css-validator/) used to validate all source JavaScript, HTML & CSS code
- [**PEP 8 Online Validator**] (http://pep8online.com/) used to check my python code to be consistent with PEP8 requirements
- [**Font Awesome Icons**] (https://fontawesome.com/icons?d=gallery) used for social icons in footer and site-wide iconography
- [**ToC**] (https://) used to generate ReadMe Table of Content

## Database

The database used for this Project was Postgres, as an Installed add-on to the deployed Heroku Application. Sqlite3 was used initially to test User Authentication, Registration & Login, and for testing the creation of Game data. However later in development I moved to local & deployed testing so Postgres was utilised from that point on.

When the app and its models were created and implemented, `python manage.py makemigrations` was run in the terminal to create the initial model package and `python manage.py migrate` was then used to apply the model to the database and create the table.
Where possible, first-time-right methodology was approached when creating the models to avoid to many alterations to the models and the database table through multiple `makemigrations` and `migrate` commands.


----

# **FEATURES**

## **SITE-WIDE FEATURES**

**Feature**

![FeatureImage](readme_media/site_screens/)

  - 
      
      • 
  
## ***FEATURES TO IMPLEMENT***

- Identified as **Strategic Trade-offs** at ***UXD Phase 2***, a **GOAL** and **GOAL** will be addressed, skills and time permitting, as and when possible.

----

# **TESTING**

## AUTOMATED TESTING

## jshint Validator Testing 

- JavaScript
  - No errors were returned when passing through the [JSHint validator](https://jshint.com/)

![JSHint JS](readme_media/check_screens/)

## W3C Validator Testing 

- HTML
  - No errors were returned when passing through the [(X)HTML5 Validator](https://html5.validator.nu/)

![W3C HTML](readme_media/check_screens/)

- HTML
  - 3 errors were returned when passing through the official [W3C validator](https://validator.w3.org)
    - These relate to the outdated convention of only *ever* using one `<main>` tag

![W3C HTML](readme_media/check_screens/)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org)

![W3C CSS](readme_media/check_screens/)

**Google Developer Tools**

- I made use of the built-in **Chrome Dev Tools** to experiment and debug while coding, in addition to testing simulated responsive behaviour across a wide range of mobile and desktop devices, and finally checking all pages Performance using **Lighthouse**. 

**Response Testing**

In order to make sure that RJW Illustration was responsive to all device sizes, I used [amiresponsive](http://ami.responsivedesign.is/)

![amiresponsive](readme_media/check_screens/)

**WebPageTest**

- I used [WebPageTest](https://www.webpagetest.org/) set to London/Chrome as a final test for **Title**.

![WebPageTest Main](readme_media/check_screens/)

## **MANUAL TESTING**

In addition to my own testing a link to the project was shared to family & friends for rigorous testing across varied devices and screen sizes.

  - **Browsers** including: 
    - Chrome
    - Safari
    - Edge

  - **Devices** including: 
    - iPhone SE (Gen 1)
    - iPhone 11
    - iPhone 12 Mini
    - Google Pixel 4a
    - iPad Pro (2018)
    - iPad Air (2020)
    - MacBook Pro (2015)
    - Windows 10 PC 

## Manual Testing Results Summary

**TEST ITEM**

| TEST | OUTCOME | PASS/FAIL |
|---|---|:---:|
| Test | Outcome | FAIL |

----

# **DEVELOPMENT CYCLE**

## **PROJECT CHECKLIST**

- Install **Django** and supporting libraries

    - Install **Django** and **Gunicorn**. Gunicorn is the server utilised to run Django on Heroku
    - Install support libraries including **psycopg2**, used to connect the **PostgreSQL database**
    - Install **Cloudinary** libraries, a host provider service for persistent image storage
    - Create ***requirements.txt*** file, which includes the dependencies to allow the project to run in Heroku

- Create a new, blank **Django Project**

    - Create new project: 'anticipator'
    - Create new app: 'xbox'
    - Add 'xbox' to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use **Cloudinary** and **PostgreSQL**
 
    - Create new **Heroku app**
        - Sign into **Heroku**
        - Select *New*
        - Select *Create new app*
        - Enter a relevant app name
        - Select appropriate region
        - Select the *Create app* button

    - Attach **PostgreSQL database**
 
        - In **Heroku** -> resources
        - Search add-ons for *Postgres*
        - Select: *Heroku Postgres*
        - Submit order form

    - Prepare ***environment*** and ***settings.py*** files
 
        - Create ***env.py*** file
        - In ***env.py***:Add DATABASE_URL with the Postgres URL from Heroku
        - Get a randomly generated **SECRET_KEY** from [key generator](https://)
        - In **Heroku**: Add SECRET_KEY + generated key to the config vars
        - In ***settings.py***: Add if statement to prevent production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary§1§§
        - Create Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPLATES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile

- Deploy new empty project to Heroku

----

# **DEPLOYMENT**

This full stack application was developed using in-browser IDE Gitpod Code v1.73.1 and version controlled via local (git) and online (github) repository technologies. All secret environment variables were stored in an `env.py` file, which was added to a `.gitignore` file and out of the public repo. Those variables detailed in the env.py file were re-enacted in Heroku Settings for this application under the `Config Vars` section, allowing the deployed site to utilise these secret variables.

The terminal was used to deploy the project locally:
- Create a repository on GitHub from the Code Institute full template
- Open repository in source code editor (GitPod)
- Enter "python3 manage.py runserver" into the terminal
- Open local host address on web browser
- All local saved changes appear here

Deploying this application was achieved by:
- Pushing code from the IDE to Github via Git and the built-in bash terminal
- Creating an app on Heroku & deploying it from same
- Adding secret environment variables to the app's Config Vars in Heroku/Settings and assigning to the respective secret values held in the env.py for Live Deployment
- In Heroku/Deploy, deployment method set to Github
Final deployment to Heroku:
- Set debug = False in settings.py file
- Commit & push all files to GitHub
- In Heroku/Settings: Remove DISABLE_COLLECTSTATIC from Config Vars
- In Heroku/Deploy: Check auto deploy and click 'Deploy branch' to deploy app 

A live link to this project can be found [here]([https://alfa23.github.io/](https://pp04-xbox-anticipator.herokuapp.com/))

To clone the repository:
- Select the Repository from Github Dashboard
- Click on the green 'Clone or download' button
- Click on the clipboard icon to the right of the Git URL to copy the web URL of the Clone
- Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window
- Change the directory to where you want to clone the repository to
- Paste the Git URL copied from above and click 'Ok'
- Once open, create an env.py file and assign the Database URL, Secret Key and other secret variables - ensure the `env.py` is in the root project directory and add it to `.gitignore` to ensure any Secret details aren't exposed


----

## **CHALLENGES, BUGS and FIXES**

### **Bug: Challenges finding, extracting and handling current_user_score value in GameDetailView**
  
  • *Issue:* 
  
  • *Fix:* https://stackoverflow.com/questions/54815303/how-to-extract-data-from-django-queryset

  ![image](readme_media/)

----

### **Bug: Success message method not working for DeleteView:**
  
  • *Issue:* 
  
  • *Fix:* https://stackoverflow.com/questions/24822509/

  ![image](readme_media/)

----

### **Bug: Date picker in Django form:**
  
  • *Issue:* Initial Django/Crispy Form renderings for CreateView weren't displaying a date picker in the input field, only the option to type dates manually.  
  
  • *Fix:* Code to enable DateInput widget referenced/sourced from: https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django

  ![image](readme_media/)

----






### **CONTRIBUTIONS**

• **All document fonts** sourced from google fonts: 

• **Django Custom User Model** process and code referenced/sourced from: https://testdriven.io/blog/django-custom-user-model/

• **Settings for CustomUser email as username in Django-AllAuth** process and code referenced/sourced from: https://pyphilly.org/know-thy-user-custom-user-models-django-allauth/


• **Rating method theory & constraints** referenced/sourced from: https://stackoverflow.com/questions/58115738/realizing-rating-in-django

----

## **CREDITS**

----
