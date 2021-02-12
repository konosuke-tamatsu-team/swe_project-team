<template>
  <v-app>
    <v-app-bar
      app
      color="green"
      dark
    >
      <div @click="toTop()" class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://konosuke.s3-ap-northeast-1.amazonaws.com/logo.jpg"
          transition="scale-transition"
          width="40"
        />


        <div @click="toTop()" class="shrink mt-1 hidden-sm-and-down" style="width:100;font-size: 200%;">Opa</div>

       
      </div>

      <v-spacer></v-spacer>

      <v-btn text>
        <span @click="toLp()" class="mr-2">このアプリについて</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>

      <v-btn text>
        <span @click="register()" class="mr-2">無料登録</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>

      <v-btn text>
        <span @click="login()" class="mr-2">ログイン</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>


    
  </v-app>


  

</template>



<script>
import router from "./router";
export default {
  
  name: 'App',

  data: () => ({
    info:null
    //
  }),
  methods: {
    
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")){
          router.push("/auth")
      }
    },
    login() {
      router.push("/auth")
    },
    register(){
      router.push("/registration")
    },
    toTop(){
      router.push("/")
    },
    toLp(){
      router.push("/lp")
    }
  }
};
</script>
