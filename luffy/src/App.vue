<template>
  <div id="app">
    <LuffyHeader />
    <router-view/>
  </div>
</template>

<script>
import LuffyHeader from '@/Common/LuffyHeader'
export default {
  name: 'App',
  components:{LuffyHeader},
}
</script>

<style scoped>

</style>
