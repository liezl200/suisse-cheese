# suisse-cheese
A companies research platform for Code Suisse, complete with smart charts and machine learning-based analysis

# Presentation / documentation/ design link (complete with screenshots for your viewing pleasure): https://docs.google.com/presentation/d/1x6nTmVySRdTtMqi2lLCYH-nW-wbWoax6p_JyZossDpk/edit?usp=sharing

# Technology Stack
MySQL database (hosted on localhost)

Express.js

Node.js

EJS (Embedded JavaScript)

Bootstrap

## Libraries used:
JQuery

Selectize

ChartJS


# Challenges & Solutions

## Front end challenges
As a first attempt at responsive design, we used Bootstrap sidebars with the "affix" class, which treats the right panel with the graph as a sticky panel. Although this worked perfectly to our specifications on desktop and tablet, a problem arose, however, when we tested the design on mobile. The graph visualization disappears due to the nature of the sidebar, but the recommendations were displayed in a concise list. Ideally, we would create a separate mobile view and user interface to optimize for these devices, but for now, the mobile companion site serves as a quick summary / lookup tool without visualizations.

# Setup
This setup requires that you have node installed.

## Clone repo and install dependencies
```git clone https://github.com/liezl200/suisse-cheese.git```

```cd suisse-cheese && sudo npm install```

## Set up database
To use the database, you must run a local MySQL server on a separate process, since Node.js only has one process (see http://blog.modulus.io/nodejs-and-sqlite). This is why MySQL is preferred over a headless server like sqlite.

Once you install XAMPP, open the manager-osx executable and start the MySQL database by going into the Manage Servers tab.

If you run into the error: "Permissions on configuration file, should not be world writeable" when you start up the php server in XAMPP, try going into your XAMPP folder then run the following command (http://stackoverflow.com/questions/7577490/phpmyadmin-wrong-permissions-on-configuration-file-should-not-be-world-writabl):

```sudo chmod 755 xamppfiles/phpmyadmin/config.inc.php```

Create a database and run the importdata_noNA.sql script for the database you just created. Then change the connection pool settings in db.js to reference localhost (or wherever you are hosting your database), your username/ password for the database server, and your new database name. We use "suissecheese" as our database name, "root" as our database user, "" as our password, and "localhost" as our database host (user: "root", password: "", host: "localhost" is the default for XAMPP.

## Run app
Make sure you are in the suisse-cheese repo then run: ```npm start```

## Go to index
In your browser, navigate to the homepage: http://localhost:3000/(http://localhost:3000/)


# Relevant Links
http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/

https://scotch.io/tutorials/use-ejs-to-template-your-node-application

http://knexjs.org/

