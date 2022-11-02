<template>
  <div id="app">

    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="createTodo"/>

  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList, 
  },
  data: function () {
    return {
      todos :[],
    }
  },
  methods:{
    createTodo: function (todoTitle) {
      const todo={
        title:todoTitle
      }
      this.todos.push(todo)

    },
    deleteTodo : function (todo) {
      const index = this.todos.indexOf(todo) //올라온 값이 인덱스 몇번인지
      this.todos.splice(index, 1) // 해당인덱스 빼고 다시삭제
    }
  }

}
</script>

<style>

</style>
