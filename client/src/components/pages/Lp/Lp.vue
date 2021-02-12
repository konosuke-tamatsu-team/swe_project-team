<template>
    <div>
        <LpOne class="topmain">
        </LpOne>

        <LpTwo class="topmain">
        </LpTwo>

        <LpTree class="topmain">
        </LpTree>

        
    </div>

    
</template>


<script>
import LpOne from './LpOne.vue'
import LpTwo from './LpTwo.vue'
import LpTree from './LpTree.vue'
export default {
    components: {
    LpOne,
    LpTwo,
    LpTree
  },
}
</script>

<style scoped>
.topmain {
    margin: 0 auto;
    min-width: 960px;
    width: 100%;
    max-width: 2560px;
    height: 880px;
 
    background-position: center;
    background-size: cover;
}
main {
    width: 960px;
    margin: 0 auto;
    display: flex;
    padding-top: 64px;
}

</style>