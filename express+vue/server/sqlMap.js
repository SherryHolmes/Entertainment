// sql语句
var sqlMap = {
    // 用户
    user: {
        select_table_ComicName: 'SELECT * FROM EntertainmentDB.ComicName',
        select_table_ComicChapter: 'SELECT * FROM EntertainmentDB.ComicChapter WHERE Dept_ID=' 
    }
}

module.exports = sqlMap;