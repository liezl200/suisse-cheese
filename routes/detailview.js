var express = require('express');
var router = express.Router();

/* GET /info page for a certain stock */
router.get('/:id', function(req, res, next) {
	stock_id = req.params.id;
	var db = require('../db.js');

	// With the WHERE clause, we must make sure to use prepared statements to prevent SQL injections.
	db.get().query('SELECT * FROM companies WHERE symbol = ?', [stock_id], function(err, results) {
    console.log(results);
    res.render('detailview', { title: stock_id + ' Info', stock_info: results});
  });
});

/* GET /info page without stock parameter passed in */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Search', names: results});
});


module.exports = router;
