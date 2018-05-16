const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const express = require('express');
const app = express();
var mysql = require('mysql');
var models = require('./db');
var $sql = require('./sqlMap');

//设置跨域访问
app.all('*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By",' 3.2.1')
    res.header("Content-Type", "application/json;charset=utf-8");
    next();
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
// 连接数据库
var conn = mysql.createConnection(models.mysql);

conn.connect();


app.get('/', function (req, res) {
   res.send('Hello World');
})


app.get('/ComicName', function (req, res) {
  var sql = $sql.user.select_table_ComicName;
	conn.query(sql, function(err, rows, fields) {
        if (err) {
            console.log('[query] - :' + err);
            return;
        }
        console.log(rows);
        res.send(rows);  //这里在页面上输出数据
	});
})

app.get('/ComicChapter/:id', function (req, res) {
  var sql = $sql.user.select_table_ComicChapter + req.params.id + " ORDER BY ChapterNum ASC;"
  console.log(sql);
  conn.query(sql, function(err, rows, fields) {
        if (err) {
            console.log('[query] - :' + err);
            return;
        }
        console.log(rows);
        res.send(rows);  //这里在页面上输出数据
  });
})

var server = app.listen(8000, function () {
 
  var host = server.address().address
  var port = server.address().port
 
  console.log("应用实例，访问地址为 http://%s:%s", host, port)
 
})