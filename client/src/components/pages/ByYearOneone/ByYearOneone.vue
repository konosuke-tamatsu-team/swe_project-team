<template>
    <div style="color:black;">

        <div>
            <p></p>
            <h2>{{title}}</h2>   
            <v-btn depressed v-if="templateSwitch !== 'home'" @click="templateSwitch='home';title='過去問'" style="float: right">年度別出題のトップページへ戻る</v-btn>
        </div>

        <div>
            <template v-if="templateSwitch === 'home'">
                <v-list>
                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='ByYearOneoneThirtytwo';title='第32回（令和元年度）過去問'" >第32回（令和元年度）の過去問をとく</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='ByYearOneoneThirtyone';title='第31回（令和元年度）過去問'" >第31回（令和元年度）の過去問をとく</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='ByYearOneoneThirty';title='第30回（令和元年度）過去問'" >第30回（令和元年度）の過去問をとく</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                        

                        

                    </v-list>
            </template>
        </div>

        <template v-if="templateSwitch === 'ByYearOneoneThirtytwo'"> 
            <ByYearOneoneThirtytwo></ByYearOneoneThirtytwo>
        </template>

        <template v-if="templateSwitch === 'ByYearOneoneThirtyone'"> 
            <ByYearOneoneThirtyone></ByYearOneoneThirtyone>
        </template>

        <template v-if="templateSwitch === 'ByYearOneoneThirty'"> 
            <ByYearOneoneThirty></ByYearOneoneThirty>
        </template>



       




        

           
    </div>
</template>

<script>
import router from "../../../router";
import ByYearOneoneThirtytwo from './ByYearOneoneThirtytwo.vue'
import ByYearOneoneThirtyone from './ByYearOneoneThirtyone.vue'
import ByYearOneoneThirty from './ByYearOneoneThirty.vue'
export default {
    components: {
    ByYearOneoneThirtytwo,
    ByYearOneoneThirtyone,
    ByYearOneoneThirty
  },
    name: "ByYearOneone",
    data () {
    return {
      title:'年度別過去問出題',
      templateSwitch: 'home',
      info: null,
      data: null,
      selectedQueston:[],
      step:0,
      qId:0,
      arrangedQuestionsLis:[],
      questionNumber:0,
      answerStatus:null,
      isFinish:false,
      correctCount:0
      }
    },
    watch: {
    /** モーダルダイアログ開閉フラグ */
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
    }
}
</script>