<template>
  <div class="">
    <hr>
    <h2>이곳은 Helloworld.vue 입니다</h2>
    <h3>{{ msg }}</h3>
   
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
