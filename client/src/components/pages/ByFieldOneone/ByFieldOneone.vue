<template>
    <div style="color:black;">

        <template v-if="step === 0">
            <center>
                <p></p>
                <h2>回答する分野を以下から選んでください</h2>
                
                <p></p>
                <v-card class="mx-auto" max-width="500">
                    <v-list>
                    <v-list-item-group v-model="field">
                        <v-list-item v-for="(item, i) in fields" :key="i">
                        <v-list-item-content>
                            <v-list-item-title v-text="item.q_field" @click="selected_field_num=item.num,step=1"></v-list-item-title>
                        </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                    </v-list>
                </v-card>
            </center>
        </template>

        
       <template v-if="step === 1" >
            <p></p><br>
            <p></p><br>
            <center>
                <div class="my-2">
                    <v-btn x-large color="success" dark style="width:70%; height:100px; font-size: 50px; " v-on:click="createQuestionDic(filterByField(info).slice(), 5),step=2">
                    一問一答を始める
                    </v-btn>
                </div> 
            </center> 
        </template>



        <!-- 問題テンプレート -->
        <template v-if="step === 2" >
            <p></p><br>
            <p></p><br>

            <center>
                <v-btn elevation="2" raised>{{arrangedQuestionsLis[questionNumber].questionSentence}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[0],questionNumber),step=3">{{arrangedQuestionsLis[questionNumber].coices[0]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[1],questionNumber),step=3">{{arrangedQuestionsLis[questionNumber].coices[1]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[2],questionNumber),step=3">{{arrangedQuestionsLis[questionNumber].coices[2]}}</v-btn><br>
                <p></p>
                <v-btn x-large color="success" dark v-on:click="judgAnswer(arrangedQuestionsLis[questionNumber].coices[3],questionNumber),step=3">{{arrangedQuestionsLis[questionNumber].coices[3]}}</v-btn>
            </center>        
        </template>

        <!-- 以下正解不正解アラート -->
        <template v-if="answerStatus === 'correct' && step === 3">
            <p></p><br>
            <p></p><br>
            <center><v-alert border="left" colored-border color="deep-purple accent-4" elevation="2" style="width:50%">
                正解<br>解説<br>
                {{arrangedQuestionsLis[questionNumber].comment}}<br>
                <v-btn elevation="2" v-on:click="nextQuestion()">次の問題へ</v-btn>
            </v-alert></center>
        </template>

        <template v-if="answerStatus === 'incorrect' && step === 3">
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
                    <v-btn x-large color="success" dark style="width:70%; height:100px; font-size: 50px; " v-on:click="initialization()">
                    分野選択に戻る
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
    name: "ByFieldOneone",
    data () {
    return {
        selected_field_num: 0,
        field: null,
        info: null,
        data: null,
        selectedQueston:[],
        step:0,
        qId:0,
        arrangedQuestionsLis:[],
        questionNumber:0,
        answerStatus:null,
        isFinish:false,
        correctCount:0,
        fields: [
            {
                num:1,
                q_field: '人体の構造と機能及び疾病'
            },{
                num:2,
                q_field: '心理学理論と心理的支援'
            },{
                num:3,
                q_field: '社会理論と社会システム'
            },{
                num:4,
                q_field: '現代社会と福祉'
            },{
                num:5,
                q_field: '福祉の理論と方法'
            },{
                num:6,
                q_field: '福祉行財政と福祉計画'
            },{
                num:7,
                q_field: '社会保障'
            },{
                num:8,
                q_field: '障害者に対する支援と障害者自立支援制度'
            },{
                num:9,
                q_field: '低所得者に対する支援と生活保護制度'
            },{
                num:10,
                q_field: '保健医療サービス'
            },{
                num:11,
                q_field: '権利擁護と成年後見制度'
            },{
                num:12,
                q_field: '社会調査の基礎'
            },{
                num:13,
                q_field: '相談援助の基盤と専門職'
            },{
                num:14,
                q_field: '相談援助の理論と方法'
            },{
                num:15,
                q_field: '福祉サービスの組織と経営'
            },{
                num:16,
                q_field: '高齢者に対する支援と介護保険制度'
            },{
                num:17,
                q_field: '児童や家庭に対する支援と児童・家庭福祉制度'
            },{
                num:18,
                q_field: '就労支援サービス'
            },{
                num:19,
                q_field: '更生保護制度'
            },
        ],

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
        filterByField(array){
            var byFieldArray = [];
            for (const elem of array) {
                if (elem.field === this.selected_field_num) {
                    byFieldArray.push(elem);
                }
            }
            return byFieldArray
        },
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
            this.selected_field_num=0,
            this.field=null,
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
                this.step=2
            }else{ 
             this.isFinish=true
             this.step=4
            }

        }
        
    }
}
</script>