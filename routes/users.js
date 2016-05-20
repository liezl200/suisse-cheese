var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
	var db = require('../db.js')
	db.get().query('SELECT name, symbol FROM companies', function(err, results) {
    //console.log(results)
  });
  //res.send('respond with a resource');
  res.render('index', { title: 'lol' });
});

module.exports = router;
