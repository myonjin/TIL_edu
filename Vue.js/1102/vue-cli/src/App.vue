<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 -->
    <MyComponent/>
    
    
    <hello-world @click="onClick"></hello-world>
    <hello-world @click.native="onClick"></hello-world>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// 1.불러오기
// import MyComponentVue from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent'

export default {
  name: 'App',
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,

  },
  methods: {
    onClick: function () {
      console.log('Hello!')
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
