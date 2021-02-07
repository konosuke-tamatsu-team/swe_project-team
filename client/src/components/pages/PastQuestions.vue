<template>
    <div>
        <div>
            <p></p>
            <h2>{{title}}</h2>   
            <v-btn depressed v-if="templateSwitch !== 'home'" @click="templateSwitch='home';title='過去問'" style="float: right">戻る</v-btn>
        </div>
        
        <div>
            <template v-if="templateSwitch === 'home'">
                <v-list>
                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='PQThirtyTwo';title='第32回（令和元年度）過去問'" >第32回（令和元年度）の過去問をみる</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='PQThirtyOne';title='第31回（令和元年度）過去問'">第31回（令和元年度）の過去問をみる</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                        <v-btn class="ma-2" outlined color="indigo">
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title @click="templateSwitch='PQThirty';title='第30回（令和元年度）過去問'">第30回（令和元年度）の過去問をみる</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        </v-btn>

                    </v-list>
            </template>
        </div>

        <template v-if="templateSwitch === 'PQThirty'">
            <PQThirty></PQThirty>
        </template>
        <template v-if="templateSwitch === 'PQThirtyOne'">
            <PQThirtyOne></PQThirtyOne>
        </template>
        <template v-if="templateSwitch === 'PQThirtyTwo'">
            <PQThirtyTwo></PQThirtyTwo>
        </template>
        
      
        

    </div>
</template>

<script>
import PQThirty from './PastQuestions/PQThirty.vue'
import PQThirtyOne from './PastQuestions/PQThirtyOne.vue'
import PQThirtyTwo from './PastQuestions/PQThirtyTwo.vue'
export default {
    components: {
        PQThirty,
        PQThirtyOne,
        PQThirtyTwo
     },
    name: "PastQuestions",
    data () {
    return {
        templateSwitch:'home',
        title:'過去問',
      }
    },
}
</script>