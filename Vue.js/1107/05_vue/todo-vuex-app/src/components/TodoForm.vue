<template>
  <div>
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
  
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle : null,
    }
  },
  methods: {
    createTodo(){
      // console.log(this.todoTitle)
      // 메서드(컴포넌트가) => 액션호출 => 뮤테이션 => state
      //              dispatch()   commit()   push
      if (this.todoTitle){
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>