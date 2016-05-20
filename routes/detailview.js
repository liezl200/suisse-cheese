var express = require('express');
var router = express.Router();

/* GET /info page for a certain stock */
router.get('/:id', function(req, res, next) {
	//
	console.log(req.params.id);
	var db = require('../db.js');
	db.get().query('SELECT name, symbol FROM companies', function(err, results) {
    //console.log(results);

    res.render('detailview', { title: 'Express', names: results});
  });

});


module.exports = router;
