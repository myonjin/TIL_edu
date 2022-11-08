<template>
  <div id="app">
    <h3 ref="appText">{{text}}</h3>
    <!-- <button @click="increase" >Update Data</button> -->
    <h3 ref="appNumber">{{number}}</h3>
    <hr>
    <h1>Cat Image</h1>
    <button @click="getImg">Get cat</button>
    <br>
    <img :src="imgSrc" alt="#">

  </div>
</template>

<script>
import axios from 'axios'



export default {
  name: 'App',
  components: {
   
  },
  data(){
    return {
      imgSrc: null,
      text:'초기데이터',
      number : 0,
    }
  },
  computed:{
    
  },
  methods :{
    increase(){
      return this.number +=1
    },
    getImg(){

      const catImg = 'https://api.thecatapi.com/v1/images/search'
      axios.get(catImg)
        .then((response)=>{
          // console.log(response.data)
          const imgimg = response.data[0].url
        this.imgSrc = imgimg
      })
        .catch((error) =>{
          console.log(error)
        })
      
    }
  },
  beforeCreate() {
  },

  created() {
    const catImg = 'https://api.thecatapi.com/v1/images/search'
      axios.get(catImg)
        .then((response)=>{
          // console.log(response.data)
          const imgimg = response.data[0].url
        this.imgSrc = imgimg
      })
        .catch((error) =>{
          console.log(error)
        })
    // }
    // console.log('-------------Create')
    // console.log(this.text)
    // this.text='App.Vue가 created'
    // console.log(this.text)
    // this.increase()
    // console.log(this.$refs.appText)
  },
  // mounted() {
  //   const button = document.querySelector('button')
  //   button.innerText = '변경변경!'
  // },
  updated() {
    console.log('이미지 리소스가 업데이트 되었습니다.')
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
