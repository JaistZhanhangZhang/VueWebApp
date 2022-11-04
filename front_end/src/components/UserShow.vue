<template>
<div> UserName:  {{ AuthStore.username }}
    <button @click="SignOut"> Signout </button>
    <button @click="ImageSubmit"> ImageSubmit </button>
</div>
</template>



<script setup lang="ts">
import {Auth} from '../store/store';
import {useRouter} from 'vue-router';
const router = useRouter();
const AuthStore = Auth()
function SignOut(){
    AuthStore.signedIn = false;
    localStorage.removeItem('user');
    window.location.href = '/';
}
function ImageSubmit(){
  router.push('/ImageSubmit');
}
</script>
<style></style>