var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
	var db = require('../db.js')
	db.get().query('SELECT * FROM companies WHERE id = 1', function(err, results) {
    console.log(results[0].name)
  });
  res.send('respond with a resource');
});

module.exports = router;
