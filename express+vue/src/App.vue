<template>
  <div id="app">
    <Menu mode="horizontal" theme="dark" active-name="/" class="style_hori" @on-select="onMenuSelect" >
      <MenuItem class="style_hor_pic" name=""><a href="/"><img src="./assets/logo.jpg" class="style_pic"></a></MenuItem>
      <MenuItem name="Comics">漫画</MenuItem>
      <MenuItem name="fiction">小说</MenuItem>
      <MenuItem style="float: right; width: 10rem;" name=""><Input v-model="value" placeholder="Searching..." ></Input></MenuItem>
    </Menu>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  components :{
  },  
  data(){
    return {
      value: '',
    }
  },
  methods:{  
      onMenuSelect:function(name){  
        this.$router.push(name);
      }
  } 
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.style_hori {
  background: #000;
}
.style_pic {
  margin-top: 0.3rem; 
  #margin-left: 5rem;
}
.style_hor_pic {
  height:1rem;
}

</style>




