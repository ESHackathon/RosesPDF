<template>
  <v-app>
    <v-content>
      <v-container fluid>
        <v-slide-y-transition mode="out-in">
          <v-layout column align-center>
            <router-view />
          </v-layout>
        </v-slide-y-transition>
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
