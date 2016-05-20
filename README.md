# suisse-cheese
A companies research platform for Code Suisse, complete with smart charts and machine learning-based analysis

# technology stack
Node.js
Express.js
Knexjs (a query builder for SQL)
MySQL database (hosted on localhost)

# setup
cd suisse-cheese && sudo npm install

run server: npm start

link to index: http://localhost:3000/

To use the database, you must run a local MySQL server on a separate process, since Node.js only has one process (see http://blog.modulus.io/nodejs-and-sqlite). This is why MySQL is preferred over a headless server like sqlite.

Once you install XAMPP, open the manager-osx executable and start the MySQL database by going into the Manage Servers tab.

If you run into the error: "Permissions on configuration file, should not be world writeable" when you start up the php server in XAMPP, try going into your XAMPP folder then run the following command (http://stackoverflow.com/questions/7577490/phpmyadmin-wrong-permissions-on-configuration-file-should-not-be-world-writabl):

sudo chmod 755 xamppfiles/phpmyadmin/config.inc.php


# relevant links
http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/

https://scotch.io/tutorials/use-ejs-to-template-your-node-application

https://scotch.io/tutorials/use-expressjs-to-get-url-and-post-parameters

http://knexjs.org/

