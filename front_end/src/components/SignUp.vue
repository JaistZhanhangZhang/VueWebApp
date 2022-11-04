<template>
  <div>
    <h1>Sign up</h1>
    <form @submit.prevent="onSubmit" @keydown.enter.prevent="onSubmit">
      <div class="form-group">
        <label for="name">Name:  </label>
        <input type="text" class="form-control" id="name" placeholder="名前を入力してください。" v-model="name" />
      </div>
      <div class="form-group">
        <label for="email">Email:  </label>
        <input type="email" class="form-control" id="email" placeholder="メールアドレスを入力してください。" v-model="email" />
      </div>
      <div class="form-group">
        <label for="password">Password:  </label>
        <input type="password" class="form-control" id="password" placeholder="パスワードを入力してください。" v-model="password" />
      </div>
      <div class="form-group">
        <label for="password_confirmation">Password confirmation:  </label>
        <input type="password" class="form-control" id="password_confirmation" placeholder="パスワードを再入力してください。" v-model="password_confirmation" />
      
      </div>
      <div><button type="submit" class="btn btn-primary">Submit</button></div>
    </form>
  </div>
    <div v-if="error" class="alert alert-danger">
      {{ errorMessage }}
    </div>
  
</template>

<script setup lang="ts">
import {ref} from "vue";
import axios  from "axios";
const hostAddress = "http://localhost:8000";
/*const user={
  name:ref(''),
  email:ref(''),
  password:ref(''),
  
}*/

const password_confirmation=ref('')
const error=ref(false);

const name = ref('');
const password = ref('');
const email = ref('');
const errorMessage=ref('');

function onSubmit(){
  if(password.value!=password_confirmation.value){
    error.value=true;
    errorMessage.value='Password confirmation does not match';
    return;
  }
  else{
    error.value=false;
    errorMessage.value='';
    var user = {"name":name.value,"email":email.value,"password":password.value};
    axios.post(hostAddress+'/SignUp',user).then(res=>{
      
      if(res.data["Error"]=="1"){
        error.value=true;
        errorMessage.value=res.data["Message"];
      }
      else{
        error.value=true;
        errorMessage.value=res.data["Message"];
        name.value='';
        email.value='';
        password.value='';
        password_confirmation.value='';

        setTimeout(()=>{
          window.location.href='/';
        },3000);

      }
    }).catch(err=>{
      console.log(err);
    }
    );
    
  }

  console.log(user);
}

</script>
<style scoped>
#form-group{
  margin-bottom:1rem;
}
#form-control{
  margin-bottom:.5rem;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
