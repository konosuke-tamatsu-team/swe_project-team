<template>
    <div class="back-ground">
        <div class="wrapp">
            
            <div style="width:auto">
                <div>
                    <img class="float-left" style="padding-top: 80;"
                    src="../../assets/top2.png"
                    alt="Grapefruit slice atop a pile of other slices">
                </div>
                <div>
                    <img class="float-left" style="padding-top: 80;"
                    src="../../assets/top3.png"
                    alt="Grapefruit slice atop a pile of other slices">
                </div>
                <div>
                    <img class="float-left" style="padding-top: 80;"
                    src="../../assets/top4.png"
                    alt="Grapefruit slice atop a pile of other slices">
                </div>
            </div>
            
            <div style="width:auto">
                
                <div class="thick-font" style="padding-left:150px; padding-top:100px;">
                    社会福祉士国家試験<br>
                    学習の<span style="color:#EC407A">効率</span>を<span style="color:#FFEB3B">最大化</span>しませんか
                </div>
            </div>

            <div>
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
    .float-left {
        float: left;
        width: 30%;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    .wrapp {
        display: flex;
        flex-direction: column;
        align-items: center;
    }


</style>

<sctipt>
</script>