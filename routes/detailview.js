var express = require('express');
var router = express.Router();

/* GET /info page for a certain stock */
router.get('/:id', function(req, res, next) {
	console.log(req.params.id);
	stock_id = req.params.id;
	var db = require('../db.js');

	// With the WHERE clause, we must make sure to use prepared statements to prevent SQL injections.
	db.get().query('SELECT * FROM companies WHERE symbol = ?', [stock_id], function(err, results) {
    console.log(results);
    res.render('detailview', { title: 'Express', stock_info: results});
  });
});

module.exports = router;
