<template>
  <div class="ComicPicShow">
    <div v-for="data in comic_content">
      <img :src="data.path">
    </div>
  </div>
</template>

<script>
export default {
  	name: 'ComicPicShow',
    data () {
      return {
        name : '',
        page : 0,
        path : '',
        comic_content: []   
      }
    },
	mounted(){
	    this.name = this.$route.query.name;
      this.page = this.$route.query.page;
      this.path = this.$route.query.path;

      for (var i=1; i < this.page; i++) {
        var path = this.path + i + ".jgp";
        var comic_content = { "path":path};
        this.comic_content.push(comic_content);
      }
	 }
}


</script>