var express = require('express');
var router = express.Router();

/* GET /info page for a certain stock */
router.get('/:id', function(req, res, next) {
	stock_ids = req.params.id.split(",");

	query_string = "";
	for(var i = 0; i < stock_ids.length-1; i++){
		query_string += "?,";
	}
	query_string += "?";

	// With the WHERE clause, we must make sure to use prepared statements to prevent SQL injections.
	// Note that concatenation of query_string is secure because the
	// concatenated query string can only have some number of question marks,
	// which are safe characters so the query still uses prepared statements with sanitized inputs.
	var db = require('../db.js');
	db.get().query('SELECT * FROM companies WHERE symbol IN ( ' + query_string + '); SELECT name, symbol FROM companies;', stock_ids, function(err, results) {
    console.log(results);
    res.render('detailview', { title: 'Stock Info', stock_info: results[0], names: results[1]});
  });
});

module.exports = router;
