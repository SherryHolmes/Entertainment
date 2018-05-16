import Vue from 'vue'  
import Vuex from 'vuex'  
  
Vue.use(Vuex); 

export default new Vuex.Store({
    state: {
        count: 0,
        startTime: '开始时间',
    },
    mutations: {
        increment (state, startData) {
            state.count = startData;
        },
        setStartTime (state, startData){
            state.startTime = startData;
        }
    }
});

