var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var db = require('../db.js')
	db.get().query('SELECT name, symbol FROM companies', function(err, results) {
    console.log(results)
  });
  res.render('index', { title: 'Express' });
});

module.exports = router;
