<template>
  <div class="ComicChapter">
    <div class="container">
      <div class="jumbotron">
        <div class="row">
          <div class="col-xs-12">
            <div class="col-xs-6">
              <img :src="path" width="450" height="280" class="img-rounded">
            </div>
            <div class="col-xs-6">
              <div class="row">
                <div class="col-xs-12">
                  <h2 class="text-left comic-name">{{name}}</h2>
                  <div class="text-left comic-intro">
                    <span>漫画简介</span>
                  </div>
                  <div class="text-left intro-switch">
                    <span>{{introduce}}</span>
                  </div> 
                </div>
              </div>
              <div class="row">
                <div class="col-xs-1 top">
                  <router-link :to="{name:'ComicPicShow', query:{name:first_content.name, page:first_content.page, path:first_content.path} }">
                    <button type="button" class="btn btn-primary">开始阅读</button>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div> 

      <Table height="200">

              
              <tr v-for="(data) in (comic_content)">
                <td><router-link :to="{name:'ComicPicShow', query:{name:data[0].name, page:data[0].page, path:data[0].path} }">{{data[0].name}}</router-link></td>
                <td><router-link :to="{name:'ComicPicShow', query:{name:data[1].name, page:data[1].page, path:data[1].path} }">{{data[1].name}} </router-link></td>
                <td><router-link :to="{name:'ComicPicShow', query:{name:data[2].name, page:data[2].page, path:data[2].path} }">{{data[2].name}}</router-link></td>
                <td><router-link :to="{name:'ComicPicShow', query:{name:data[3].name, page:data[3].page, path:data[3].path} }">{{data[3].name}}</router-link></td>
              </tr>
              

    </Table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  	name: 'ComicChapter',
    data () {
      return {
        name: '',
        id  : 0,
        path: '',
        introduce: '',
        comic_content: [],
        first_content: {"name":'', "page":0, "path":''}
      }
    },
	mounted(){
	    this.name      = this.$route.query.name;
      this.id        = this.$route.query.id;
      this.path      = this.$route.query.path;
      this.introduce = this.$route.query.introduce;
      console.log(this.introduce);

      var url   = 'http://198.13.54.7:8000/ComicChapter/'+this.id 
      this.$ajax.get(url).then(response => {
        var lst_comic = []
        for (var i=0; i < response.data.length; i++) {
          var path = "/static/" + this.name + "/" + response.data[i].ChapterName + "/";
          var dict_comic= { "name":response.data[i].ChapterName, "page":response.data[i].PicNum, "path":path};

          if (i == 0) {
            this.first_content = dict_comic
          }
          lst_comic.push(dict_comic);
          if ((i%4) == 0 && i>0) {
            this.comic_content.push(lst_comic);
            lst_comic = []
          }
        }
      }, response => {
        console.log(response);
      })
	 }
}


</script>

<style>
    .comic-name{color:#333;font-size:18px;padding-top:14px}
    .comic-intro span{display:inline-block;border-bottom:2px solid #f5ce03}
    .intro-switch span{display:inline-block;border-bottom:2px}
    .bottom { margin-bottom: 50px; }
    .top    { margin-top: 50px; }

/* Custom Styles */
    ul.nav-tabs{
        width: 140px;
        margin-top: 20px;
        border-radius: 4px;
        border: 1px solid #ddd;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.067);
    }
    ul.nav-tabs li{
        margin: 0;
        border-top: 1px solid #ddd;
    }
    ul.nav-tabs li:first-child{
        border-top: none;
    }
    ul.nav-tabs li a{
        margin: 0;
        padding: 8px 16px;
        border-radius: 0;
    }
    ul.nav-tabs li.active a, ul.nav-tabs li.active a:hover{
        color: #fff;
        background: #0088cc;
        border: 1px solid #0088cc;
    }
    ul.nav-tabs li:first-child a{
        border-radius: 4px 4px 0 0;
    }
    ul.nav-tabs li:last-child a{
        border-radius: 0 0 4px 4px;
    }
    ul.nav-tabs.affix{
        top: 30px; /* Set the top position of pinned element */
    }
</style>