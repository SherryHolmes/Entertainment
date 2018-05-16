// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//import './assets/bootstrap/css/bootstrap.min.css'
//import './assets/bootstrap/js/bootstrap.min'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import store from './store/store'
import axios from 'axios'

Vue.use(iView);
Vue.prototype.$ajax= axios
Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
