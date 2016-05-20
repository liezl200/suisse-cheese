var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var db = require('../db.js')
	db.get().query('SELECT name, symbol FROM companies', function(err, results) {
    console.log(results)
<<<<<<< HEAD
    res.render('index', { title: 'Express', results: results });
  });

=======
    res.render('index', { title: 'Express', names: results});
  });
  
>>>>>>> 740972a81f50618d44d74c6af84672161a061d51
});

module.exports = router;
