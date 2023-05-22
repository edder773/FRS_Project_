<template>
  <div>
    <a href="/deposit">예금비교</a> |
    <a href="/saving">적금비교</a> |
    <router-view />
    <DepositList/>
  </div>
</template>

<script>
import DepositList from '@/components/DepositList.vue'
export default {
  name: 'ProductView',
  components: {
    DepositList
  }
}
</script>

<style>

</style>