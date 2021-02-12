<template>
    <div>
       
            
        <center class="wrapp">
        

            <p></p>
            <br>
            <p></p>
            <br>
            <p></p>
            <br>
            <p></p>
            <br>
            <p></p>
            <br>
            <p></p>
            <br>
            
            <h1 class="thick-font">機能<br>要修正
            </h1>

            <p></p>
            <br>
            <p></p>

        </center>
            
        <div class="wrapp">
            <div>           
                <div class="float-left">
                    <div class="wrapp">
                        <img class="pic"
                        src="../../../assets/lp3_3.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font">分野ごとの出題</p>
                    </div>
                </div>
                    
                <div class="float-left">
                    <div class="wrapp">
                        <img class="pic"
                        src="../../../assets/lp3_2.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font">年度ごとの出題</p>
                    </div>
                </div>

                <div class="float-left">
                    <div class="wrapp">
                        <img class="pic"
                        src="../../../assets/lp3_1.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font">過去問に取り組む</p>
                    </div>
                </div>
            </div>
        </div>


        <div class="wrapp">
            <p></p>
            <v-btn class="ma-2;thin-font" :disabled="loading2" color="success" @click="loader = 'loading2'">
                学習を始める
                <template v-slot:loader>
                    <span>Loading...</span>
                </template>
            </v-btn>
        </div>


        <p></p>
            <br>
            <p></p>
            
         
        

        <div style="width:100%;background:#81C784;">
            <center>
                <div>Opa</div>
            </center>
        </div>
            

   

    
    </div>        

</template>

<script>
export default {
  name: 'LpTree'
}
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
        font-size: 30%;
        font-family: Noto Sans,Tsukushi A Round Gothic,ヒラギノ丸ゴ ProN”\, Hiragino Maru Gothic ProN,Meiryo,メイリオ;
        font-size: 16px;
        font-weight: 160
    }
    .example{
        float: left;
    }
    .float-left {
        float: left;
        width: 32%;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    .pic {
        float: left;
        width: 80%;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    .wrapp {
        display: flex;
        flex-direction: column;
    }

</style>