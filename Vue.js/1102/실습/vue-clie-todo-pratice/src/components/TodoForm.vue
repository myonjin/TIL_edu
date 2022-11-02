<template>
  <div>
    <h1>TodoForm</h1>
    <input type="text" v-model="todoTitle"
    @keyup.enter="craeteTodo"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods:{
    craeteTodo: function () {
      this.$emit('create-todo',this.todoTitle)
      this.todoTitle=null
      console.log('33')
    }
  }
}
</script>

<style>

</style>