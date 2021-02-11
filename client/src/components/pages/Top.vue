<template>
    <div class="back-ground">
        <div>
            

            <div class="inline-block_test">
                <img class="fit-picture" style="padding-top: 80;"
                src="../../assets/top2.png"
                alt="Grapefruit slice atop a pile of other slices">
            </div>
            <div class="inline-block_test">
                <img class="fit-picture" style="padding-top: 80;"
                src="../../assets/top3.png"
                alt="Grapefruit slice atop a pile of other slices">
            </div>
             <div class="inline-block_test">
                <img class="fit-picture" style="padding-top: 80;"
                src="../../assets/top4.png"
                alt="Grapefruit slice atop a pile of other slices">
            </div>

            <div>
                <div class="thick-font" style="padding-left:150px; padding-top:100px;">
                    社会福祉士国家試験<br>
                    学習の<span style="color:#EC407A">効率</span>を<span style="color:#FFEB3B">最大化</span>しませんか
                

                    <v-btn>
                        <span @click="register()" class="mr-2">無料登録</span>
                        <v-icon>mdi-open-in-new</v-icon>
                    </v-btn>

 
                    
                    <v-btn>
                        <span @click="login()" class="mr-2">ログイン</span>
                        <v-icon>mdi-open-in-new</v-icon>
                    </v-btn>

                </div>
            </div>


        </div>
    </div>

</template>

<script>
import router from "../../router";
export default {
  
  name: 'Top',

  methods: {
    
    login() {
      router.push("/auth")
    },
    register(){
      router.push("/registration")
    },
  }
};
</script>

<style>
    .back-ground {
    width:100%; 
    height:100%;
    background: linear-gradient(#4CAF50,#C5E1A5);
    }
    .fit-picture {
    width: 450px;
    }
    .inline-block_test {
    display: inline-block;      /* インラインブロック要素にする */
    padding:  20px;             /* 余白指定 */
    height: 100px;              /* 高さ指定 */
    }
    .thick-font{
        font-size: 200%;
        font-family: Noto Sans,Tsukushi A Round Gothic,ヒラギノ丸ゴ ProN”\, Hiragino Maru Gothic ProN,Meiryo,メイリオ;
        font-size: 72px;
        font-weight: 700
    }

</style>

<sctipt>
</script>