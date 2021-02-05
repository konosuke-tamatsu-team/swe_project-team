<template>
    <div style="color:orange;">
        対戦
        <div id="app">
            
            {{ info }}
           
        <button v-on:click="get_ones">Greet</button>
        <button v-on:click="a">dataに</button>
        </div>
    </div>
</template>

<script>
import router from "../../router";
import axios from 'axios';
export default {
    name: "Match",
    data () {
    return {
      info: null,
      data: null,
      }
    },
    mounted: function() {
    this.checkLoggedIn();
    },
    methods: {
        checkLoggedIn() {
            this.$session.start();
            if (!this.$session.has("token")){
                router.push("/auth")
            }
        },
        get_ones() {
            //401だから認証されてないことが原因か？？http://localhost:8000/api/
            axios.get('http://localhost:8080/api/questions/').then(response => (this.info = response["data"])
            // eslint-disable-next-line
            ).catch(e => {
                 console.log(e)
            })
            
            //this.a()
        },
        a(){
            console.log(typeof(this.info))
            this.data= this.info[0]
         
        }
    }
}
</script>