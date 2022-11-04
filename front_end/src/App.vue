<template>

<div id="header">
  <div id="Home"><button @click="BackToHome">Home</button></div>
  <div id="user"><Header></Header></div>
  
</div>
<div id="footer"><router-view></router-view></div>

</template>
<script setup lang="ts">
import Sign from './components/Sign.vue';
import UserShow from './components/UserShow.vue';
import Header from './components/Header.vue';
function BackToHome(){
  window.location.href = '/';
}
</script>
<style>
.Home{
  width:10%;
  float:left;
}
.user{
  width:90%;
  float:right;
}
#header{
  width:100%;
  height:20%;
  background-color: #f5f5f5;
  border-bottom: 1px solid #e7e7e7;
}
#footer{
  width:100%;
  height:80%;
  background-color: #f5f5f5;
  border-top: 1px solid #e7e7e7;
}
</style>