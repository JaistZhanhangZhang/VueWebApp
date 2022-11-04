<template>
<h1>Sign in</h1>
<form @submit.prevent="onSubmit" @keydown.enter.prevent="onSubmit">
  <div class="form-group">
    <label for="name">Name:  </label>
    <input type="text" class="form-control" id="name" placeholder="名前を入力してください。" v-model="name" />
  </div>
  <div class="form-group">
    <label for="password">Password:  </label>
    <input type="password" class="form-control" id="password" placeholder="パスワードを入力してください。" v-model="password" />
  </div>
  <div class="form-group">
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>
<div>
    <div v-if="error" class="alert alert-danger">
        {{ errorMessage }}
    </div>
</div>
</template>

<script setup lang="ts">
import {ref} from "vue";
import axios  from "axios";

const hostAddress = "http://localhost:8000";
const name = ref('');
const password = ref('');
const error=ref(false);
const errorMessage=ref('');

function onSubmit(){
    if(password.value==''){
        error.value=true;
        errorMessage.value='Password is empty';
        return;
    }
    else{
        error.value=false;
        errorMessage.value='';
        var user = {"name":name.value,"password":password.value};
        axios.post(hostAddress+'/SignIn',user).then(res=>{
            console.log(res);
        if(res.data.Error=='0'){
            console.log(res.data);
            localStorage.setItem('user',JSON.stringify(res.data));

            window.location.href='/';
        }
        else{
            error.value=true;
            errorMessage.value=res.data.Message;
        }
        }).catch(err=>{
        error.value=true;
        errorMessage.value='Name or password is incorrect';
        }).finally(()=>{
        password.value='';
        });
    }

}
</script>
<style>
</style>
