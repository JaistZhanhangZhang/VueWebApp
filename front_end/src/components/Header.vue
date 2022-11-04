<template>
<div>
<div v-if="AuthStore.signedIn">
  <UserShow></UserShow>
</div>
<div v-else>
  <Sign></Sign></div>
</div>
</template>

<script setup lang="ts">

import Sign from './Sign.vue';
import UserShow from './UserShow.vue';
import { ref } from 'vue';
import {Auth} from '../store/store';
const AuthStore = Auth()
const UserInfo = localStorage.getItem('user');
//var signedIn = ref(false);//pinia

if (UserInfo){
  const User = JSON.parse(UserInfo);
  const expires = new Date(User.expires);
    if (expires > new Date()){
        AuthStore.signedIn = true;
        AuthStore.username = User.username;
        AuthStore.token = User.token;
        AuthStore.expires = User.expires;
    }
}
else{
  AuthStore.signedIn = false;
}
console.log(UserInfo);

</script>
<style></style>