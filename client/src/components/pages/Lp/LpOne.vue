<template>
    <div>
        <div >
            
            <center>
            

            <p></p>
     
            
            <h1 class="thick-font">Opa ?
            </h1>

            <p></p>
           
            <div class="thin-font">社会福祉士の資格とりたい。でも範囲広すぎ。
            </div>
             <p></p>

            
            

            <div class="thin-font">Opaで社会福祉士国家試験の勉強効率を最大化しませんか？
            </div>

            <div class="inline-block_test">
                <img class="fit-picture" style="padding-top: 80;"
                src="../../../assets/lp1.png"
                alt="Grapefruit slice atop a pile of other slices">
            </div>

            <center>
            <v-btn
                class="ma-2;thin-font"
                :loading="loading2"
                :disabled="loading2"
                color="success"
                @click="login()"
                >
                学習を始める
                <template v-slot:loader>
                    <span>Loading...</span>
                </template>
            </v-btn>
            <p></p>
            </center>

            </center>

        </div>



        
    </div>        

</template>

<script>
import router from "../../../router";
export default {
  name: 'LpOne',
  methods: {
    login() {
      router.push("/auth")
    },
  }
};

</script>

<style scoped>
    .back-ground {
    width:100%; 
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

    .thin-font{
        font-size: 100%;
        font-family: Noto Sans,Tsukushi A Round Gothic,ヒラギノ丸ゴ ProN”\, Hiragino Maru Gothic ProN,Meiryo,メイリオ;
        font-size: 32px;
        font-weight: 320
    }

</style>