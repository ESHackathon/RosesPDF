<template>
  <v-container text-xs-center>
    <v-layout row>
      <v-flex xs4 offset-xs4>
        <router-view></router-view>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'errors-layout',
    data  () {
      return {}
    },
    methods: {}
  }
</script>

<style lang="scss" scoped>
</style>
