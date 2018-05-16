<template>
  <div class="comic">
    <hr>
    <Row class="style_row">
      <Carousel v-model="value" :autoplay="true" class="carousel_inner" loop>
        <CarouselItem>
          <div class="demo-carousel"><router-link :to="{name:'ComicChapter', query:{name:'海贼王', id:1, path:'/static/海贼王/海贼王.jpg', introduce:'路飞为实现与因救他而断臂的香克斯的约定而出海，他在旅途中不断寻找志同道合的伙伴，开始了以成为海贼王为目标的伟大的冒险旅程。'} }"><img src="/static/海贼王/轮播.jpg" alt="海贼王"></router-link></div>
        </CarouselItem>
        <CarouselItem>
          
          <div class="demo-carousel"><router-link :to="{name:'ComicChapter', query:{name:'火影忍者', id:2, path:'/static/火影忍者/火影忍者.jpg', introduce:'在木叶忍者村，身为孤儿的漩涡鸣人受尽村人冷落。为了让更多的人认可自己，他的目标是成为火影。鸣人怀着过人的自信与勇气开始了训练，但一切要比他想象的要困难的多。'} }"><img src="/static/火影忍者/轮播.jpg" alt="火影忍者"></router-link></div>
        </CarouselItem>
      </Carousel>
    </Row>
    <hr>
    <Row class="style_row">
      
        
          <div v-for="data in comic_content">
            <Col :xs="{ offset: 2, span: 20 }" :lg="{ span: 4, offset: 1 }">
              <router-link :to="{name:'ComicChapter', query:{name:data.name, id:data.id, path:data.path, introduce:data.introduce} }"><img :src="data.path" class="style_Comic_pic" :alt="data.name">{{ data.name }}</router-link>
            </Col>  
          </div>
      
      
    </Row>
  </div>
</template>

<script>
export default {
  name: 'comic',
  components: {
  },
  data() {
    return{
      value: 0,
      comic_content : [],
    }
    
  },

  mounted() {
  this.$ajax.get('http://198.13.54.7:8000/ComicName').then(response => {
    for (var i = 0; i < response.data.length; i++) {
      var path          = "/static/" + response.data[i].Name + "/" + response.data[i].Name + ".jpg";
      var comic_content = { "path": path, "name": response.data[i].Name, "introduce": response.data[i].Introduce, "id": response.data[i].ID}; // 字典 
      this.comic_content.push(comic_content)  
    }
  }, response => {
    console.log(response);
  })
  }
}
</script>

<style>
  .carousel_inner img {
    margin: 0 auto;
    height: 25rem;
    width:60%;
  }
    
  .hr {
    
    border-bottom: 3px solid #aaa;
    margin-bottom: 10px;
    height:10px;
  }

  .style_Comic_pic {
    height: 10rem; 
    width: 100%; 
    display: block;
  }

  .style_row {
    margin-top:1rem;
  }
</style>