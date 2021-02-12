<template>
    <div>
       
            
        <center class="wrapp">
        

            <p></p>
            <br>
            <p></p>
            <br>
            
            <h1 class="thick-font">Opaで解決できる課題
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
                        src="../../../assets/lp2.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font">自分の学習の進捗度合いが分からない</p>
                    </div>
                </div>
                    
                <div class="float-left">
                    <div class="wrapp">
                        <img class="pic"
                        src="../../../assets/lp3.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font"><center>どの範囲を理解していて、<br>どこが分からないのかが整理できない</center></p>
                    </div>
                </div>

                <div class="float-left">
                    <div class="wrapp">
                        <img class="pic"
                        src="../../../assets/lp4.png"
                        alt="Grapefruit slice atop a pile of other slices">

                        <p class="thin-font">試験の範囲が広すぎて、勉強時間が足りない</p>
                    </div>
                </div>
            </div>
        </div>


        <div class="wrapp">

            <v-btn class="ma-2;thin-font" :disabled="loading2" color="success" @click="loader = 'loading2'">
                学習を始める
                <template v-slot:loader>
                    <span>Loading...</span>
                </template>
            </v-btn>
        </div>

   

    
    </div>        

</template>

<script>
export default {
  name: 'LpTwo'
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
        width: 100%;
        margin-right: 8px;
        margin-bottom: 8px;
    }
    .wrapp {
        display: flex;
        flex-direction: column;
    }

</style>