<template>
    <div style="color:black;">

        
        
        <v-btn elevation="21" text x-large v-on:click="createQuestionDic(info.slice(), 2),step=1">
            一問一答を始める
        </v-btn>




        <template v-if="step === 1" >
           
               {{arrangedQuestionsLis[0].questionSentence}}
               {{arrangedQuestionsLis[0].coices[0]}}
               {{arrangedQuestionsLis[0].coices[1]}}
               {{arrangedQuestionsLis[0].coices[2]}}
               {{arrangedQuestionsLis[0].coices[3]}}

        
        </template>

           
    </div>
</template>

<script>
import router from "../../router";
import axios from 'axios';
export default {
    name: "OneOne",
    data () {
    return {
      info: null,
      data: null,
      selectedQueston:[],
      step:0,
      qId:0,
      arrangedQuestionsLis:[],
      questionNumber:0,

      }
    },
    watch: {
    /** モーダルダイアログ開閉フラグ */
    },
    mounted: function() {
        this.checkLoggedIn();
        this.get_ones();
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
        },
        createQuestionDic(array, num){
            //問題用の辞書を返す関数
            //他の関数を呼び出す
            let selectedQuestionLis=this.randomSelect(array, num)
            let arrangedQuestionsLis=[];
            for(let dic of selectedQuestionLis){
                let onlychoicelis=this.crateOnlyChoice(dic)
                let shuffledChoicesLis=this.lisShuffle(onlychoicelis)
                console.log(shuffledChoicesLis)
                console.log(tempdic)
                let tempdic ={id:dic["id"],questionSentence:dic['question'],correctAnswer:dic['aChoice'],coices:shuffledChoicesLis,comment:dic['comment'],author:dic['author']}
                arrangedQuestionsLis.push(tempdic);
            }
            this.arrangedQuestionsLis=arrangedQuestionsLis
        },
        randomSelect(array, num){
            //apiでとってきた全ての問題からnum問だけランダムに選んで返す関数
            let selectedQuestionLis = [];
            while(selectedQuestionLis.length < num && array.length > 0){
                const rand = Math.floor(Math.random() * array.length);
                selectedQuestionLis.push(array[rand]);
                array.splice(rand, 1);
            }
            return selectedQuestionLis
        } ,
        crateOnlyChoice(dic) {
            //選択肢のみのリストを作成する関数
            let choiceLis = [dic['aChoice'],dic['dChoice1'],dic['dChoice2'],dic['dChoice3'],dic['dChoice4']]
            return choiceLis;
        },  
        lisShuffle(arr) {
            //選択肢のリストをシャッフルして返す関数
            var n = arr.length;
            var temp, i;
            while (n) {
                i = Math.floor(Math.random() * n--);
                temp = arr[n];
                arr[n] = arr[i];
                arr[i] = temp;
            }
            return arr;
        }
    }
}
</script>