<template>
    <v-app>
        <v-navigation-drawer app v-model="drawer" clipped >
            <v-container>
                <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title grey--text text--darken-2">
                    機能
                    </v-list-item-title>
                </v-list-item-content>
                </v-list-item>
                <v-divider></v-divider>
                <v-list>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='OneOne'">ランダム出題</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='ByYearOneone'">年度ごとランダム出題</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='ByFieldOneone'">分野ごとランダム出題</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='WrongQuestions'">間違えた問題</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='Configuration'">設定</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='PastQuestions'">過去問を見る</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title @click="templateSwitch='Match'">対戦</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-container>
        </v-navigation-drawer>
        <v-app-bar color="primary" dark app clipped-left>
        <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>SWE</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn text v-on:click="logout()">ログアウト</v-btn>
            <v-menu offset-y>
            <template v-slot:activator="{on}">
            <v-btn v-on="on" text>Support<v-icon>mdi-menu-down</v-icon></v-btn>
            </template>
            <v-list>
            <v-list-item>
            <v-list-item-content>
            <v-list-item-title>Consulting and support</v-list-item-title>
            </v-list-item-content>
            </v-list-item>
            <v-list-item>
            <v-list-item-content>
                <v-list-item-title>Discord community</v-list-item-title>
            </v-list-item-content>
            </v-list-item>
            </v-list>
            
            </v-menu>
        </v-toolbar-items>
        </v-app-bar>    
        <v-footer color="primary" dark app>
            SWE
        </v-footer>
        <template v-if="templateSwitch === 'Home'">
            <Home></Home>
        </template>
        <template v-if="templateSwitch === 'OneOne'">
            <OneOne></OneOne>
        </template>
        <template v-if="templateSwitch === 'ByYearOneone'">
            <ByYearOneone></ByYearOneone>
        </template>
        <template v-if="templateSwitch === 'ByFieldOneone'">
            <ByFieldOneone></ByFieldOneone>
        </template>
        <template v-if="templateSwitch === 'WrongQuestions'">
            <WrongQuestions></WrongQuestions>
        </template>
        <template v-if="templateSwitch === 'Configuration'">
            <Configuration></Configuration>
        </template>
        <template v-if="templateSwitch === 'PastQuestions'">
            <PastQuestions></PastQuestions>
        </template>
        <template v-if="templateSwitch === 'Match'">
            <Match></Match>
        </template>
       
  </v-app>
</template>

<script>
import axios from 'axios';
import router from "../../router";
import OneOne from './OneOne.vue'
import ByYearOneone from './ByYearOneone/ByYearOneone.vue'
import ByFieldOneone from './ByFieldOneone/ByFieldOneone.vue'
import WrongQuestions from './WrongQuestion.vue'
import Configuration from './Configuration.vue'
import PastQuestions from './PastQuestions.vue'
import Home from './Home.vue'
import Match from './Match.vue'
export default {
    components: {
    OneOne,
    ByYearOneone,
    ByFieldOneone,
    WrongQuestions,
    Configuration,
    PastQuestions,
    Match,
    Home
  },
  data(){
    return{
        drawer: null,
        templateSwitch:'Home',
        nav_lists:[
            {name: 'Getting Started',icon: 'mdi-vuetify'},
            {name: 'Customization',icon: 'mdi-cogs'},
            {name: 'Styles & animations',icon: 'mdi-palette'},
            {name: 'UI Components',icon: 'mdi-view-dashboard'},
            {name: 'Directives',icon: 'mdi-function'},
            {name: 'Preminum themes',icon: 'mdi-vuetify'},
        ],
    }
  },
  methods: {
    logout(){
      axios.post('http://localhost:8080/api/v1/rest-auth/logout/').then(response => (this.info = response,router.push("/auth"))
            // eslint-disable-next-line
            ).catch(e => {
                 console.log(e)
            })
    },
  }
}
</script>