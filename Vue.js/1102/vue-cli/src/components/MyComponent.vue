<template>
    <div class="border">
      <h1>나 김현진은 언제나 세계 동물의 권리를 위해 싸울준비가 되어있다!</h1>
      <MyComponentItem static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="partentGetEvent"
      @child-input="getDynamicData"
      />
        
    </div>



</template>

<script>
import MyComponentItem from '@/components/MyComponentitem.vue'

export default {
  name : 'MyComponent',
  components : {
    // 2. 등록하기
    MyComponentItem,

  },
  data : function () {
    return{
      dynamicProps : '이건 동적인 데이터!',
    }
  },
  methods:{
    partentGetEvent: function (childData) {
      console.log('용돈없어')
      console.log(childData)
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다`)
    }
  }

}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>