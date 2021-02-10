<template>
    <div style="color:black;">

        
       <template v-if="step === 0" >
            <p></p><br>
            <p></p><br>
            <center>
                <div class="my-2">
                    <v-btn x-large color="success" dark style="width:70%; height:100px; font-size: 50px; " v-on:click="createQuestionDic(filterByYear(info).slice(), 5),step=1">
                    一問一答を始める
                    </v-btn>
                </div>
            </center> 
        </template>



        <!-- 問題テンプレート -->
        <template v-if="step === 1" >
            <p></p><br>
            <p></p><br>

            <center>
                <v-btn elevation="2" raised>{{arrangedQuestionsLis[questionNumber].questionSentence}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[0],questionNumber),step=2">{{arrangedQuestionsLis[questionNumber].coices[0]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[1],questionNumber),step=2">{{arrangedQuestionsLis[questionNumber].coices[1]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[2],questionNumber),step=2">{{arrangedQuestionsLis[questionNumber].coices[2]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[3],questionNumber),step=2">{{arrangedQuestionsLis[questionNumber].coices[3]}}</v-btn>
            </center>        
        </template>

        <!-- 以下正解不正解アラート -->
        <template v-if="answerStatus === 'correct' && step === 2">
            <p></p><br>
            <p></p><br>
            <center><v-alert border="left" colored-border color="deep-purple accent-4" elevation="2" style="width:50%">
                正解<br>解説<br>
                {{arrangedQuestionsLis[questionNumber].comment}}<br>
                <v-btn elevation="2" v-on:click="nextQuestion()">次の問題へ</v-btn>
            </v-alert></center>
        </template>

        <template v-if="answerStatus === 'incorrect' && step === 2">
             <p></p><br>
            <p></p><br>
            <center><v-alert border="left" colored-border color="deep-purple accent-4" elevation="2" style="width:50%">
                不正解<br>解説<br>
                {{arrangedQuestionsLis[questionNumber].comment}}<br>
                <v-btn elevation="2" v-on:click="nextQuestion()">次の問題へ</v-btn>
            </v-alert></center>
        </template>





        <template v-if="isFinish">
             <p></p><br>
            <p></p><br>
            <center><v-alert border="left" colored-border color="deep-purple accent-4" elevation="2" style="width:50%">
                終了<br>
                {{correctCount}}問正解です。
            </v-alert></center>
            <center>
                <div class="my-2">
                    <v-btn x-large color="success" dark style="width:70%; height:100px; font-size: 50px; " v-on:click="initialization(); createQuestionDic(info.slice(), 5),step=1">
                    もう一度
                    </v-btn>
                </div>
            </center> 
        </template>


       




        

           
    </div>
</template>

<script>
import router from "../../../router";
import axios from 'axios';
export default {
    name: "ByYearOneoneThirtytwo",
    data () {
    return {
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
        this.get_questons();
    },
    methods: {
        checkLoggedIn() {
            this.$session.start();
            if (!this.$session.has("token")){
                router.push("/auth")
            }
        },
        get_questons() {
            //401だから認証されてないことが原因か？？http://localhost:8000/api/
            axios.get('http://localhost:8080/api/questions/').then(response => (this.info = response["data"])
            // eslint-disable-next-line
            ).catch(e => {
                 console.log(e)
            })
        },
        initialization(){
            this.data= null,
            this.selectedQueston=[],
            this.step=0,
            this.qId=0,
            this.arrangedQuestionsLis=[],
            this.questionNumber=0,
            this.answerStatus=null,
            this.isFinish=false,
            this.correctCount=0
        },
        filterByYear(array){
            var byYearArray = [];
            for (const elem of array) {
                if (elem.number_of_times === 30) {
                    byYearArray.push(elem);
                }
            }
            return byYearArray
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
        },
        //以下
        judgAnswer(answer,questionNumber){
            //正解不正解の判定&アラート画面表示
            let correctAnswer=this.arrangedQuestionsLis[questionNumber]["correctAnswer"]
            let usersAnswer=answer
            if (correctAnswer === usersAnswer) {
                this.answerStatus="correct"
                this.correctCount+=1
            }else{
                this.answerStatus="incorrect"
            }
        },
        nextQuestion(){
            //次の問題を表示させる
            if(this.questionNumber<4){
                this.questionNumber+=1
                this.step=1
            }else{ 
             this.isFinish=true
             this.step=3
            }

        }
        
    }
}
</script>