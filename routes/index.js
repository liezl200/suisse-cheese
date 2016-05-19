var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	connection.query('SELECT * FROM companies WHERE id = 1', function(err, results) {
    console.log(results[0].name)
  });
  res.render('index', { title: 'Express' });
});

module.exports = router;
