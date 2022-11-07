<template>
  <div>
    <li>
      
      <button @click="deleteTodo">XX</button>


      <input type="text" v-model="inputData">
      <button @click="onClick">추가</button>
    </li>
  </div>
</template>

<script>

export default {
  name : 'TodoListItem',
  props: {
    todo : Object,
  },
  data: function () {
    return {
      inputData:'',
    }
  },
  methods:{
    deleteTodo: function () {
      this.$emit('delete-todo', this.todo)
    },
    onClick : function () {
      this.$emit('add-todo',this.inputData)
    }
  }
}
</script>

<style>

</style>