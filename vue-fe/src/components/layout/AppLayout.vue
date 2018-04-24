<template>
  <v-app>
    <v-content>
      <v-container fluid>
        <v-layout row>
          <v-flex sm12 md8 offset-md2>
            <header>
              <div class="logo"></div>
            </header>
          </v-flex>
        </v-layout>
        <router-view />
      </v-container>
    </v-content>
    <v-footer class="pa-3">
      <v-spacer></v-spacer>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'app-layout',
    data () {
      return { }
    },
    methods: {
    }
  }
</script>

<style lang="scss" scoped>
  header {
    margin: 0 0 20px 0;

    div.logo {
      background-image: url('/static/images/roses-logo.png');
      background-size: cover;
      width: 248px;
      height: 120px;
    }
  }
</style>
