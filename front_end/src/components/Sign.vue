<template>

<button @click="signUp" class="button" active-class="active">Sign Up</button>
<button @click="signIn" class="button" active-class="active">Sign In</button>

</template>

<script setup lang="ts">
import {useRouter} from 'vue-router';
const router = useRouter();

function signUp(){
  router.push('/SignUp');
}
function signIn(){
  router.push('/SignIn');
}
</script>
<style>
</style>
