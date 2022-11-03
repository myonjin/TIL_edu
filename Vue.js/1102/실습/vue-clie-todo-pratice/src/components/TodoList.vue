<template>
  <div>
    <h1>TodoList</h1>
    <ul v-for="(todo, index) in todos" :key="index">
      <!-- {{todos[0].title}} -->
      <TodoListItem :todo="todo" @delete-todo="deleteTodo"/>

    </ul>
    <TodoListItem @add-todo="onAddTodo"></TodoListItem>
  </div>
</template>

<script>
// import TodoListItem from '@/components/TodoListItem'
import TodoListItem from './TodoListItem.vue'

export default {
  name : 'TodoList',
  components:{
    TodoListItem,
    

  },
  props:{
    todos: Array,

  },
  methods :{
    deleteTodo : function (todo) {
      this.$emit('delete-todo',todo)
    },
    onAddTodo : function (inputData) {
      console.log(inputData)
    }

  }
}
</script>

<style>

</style>