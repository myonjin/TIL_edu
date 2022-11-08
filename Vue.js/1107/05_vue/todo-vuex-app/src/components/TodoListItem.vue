<template>
  <div>
    <span @click="updateTodoStatus" :class="{'a': todo.isCompleted}"
    
     >{{todo.title}}</span>
    <button @click="deleteTodo">Delete</button>
  
  </div>
</template>

<script>
export default {
  name:'TodoListitem',
  props: {
    todo:Object,
  },
  methods: {
    deleteTodo(){
      // console.log('삭제메서드 ') ,   // 뭘삭제할껀데
      this.$store.dispatch('deleteTodo',this.todo)
    }// 작성하고 actions으로
    ,
    updateTodoStatus(){
        this.$store.dispatch('updateTodoStatus',this.todo)
        console.log(this.todo)
    }
  },
}
</script>

<style>
  .a {
    text-decoration: line-through;
  }
</style>