import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Comics from '@/components/Comics/Comics'
import Fiction from '@/components/Fiction'
import ComicChapter from '@/components/Comics/ComicChapter'
import ComicPicShow from '@/components/Comics/ComicPicShow'

Vue.use(Router)

export default new Router({
  mode: 'history', 
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/Comics',
      name: 'Comics',
      component: Comics
    },
    {
      path: '/fiction',
      name: 'fiction',
      component: Fiction
    },
    {
      path: '/Comics/ComicChapter',
      name: 'ComicChapter',
      component: ComicChapter
    },
    {
      path: '/Comics/ComicPicShow',
      name: 'ComicPicShow',
      component: ComicPicShow
    }
  ]
})
