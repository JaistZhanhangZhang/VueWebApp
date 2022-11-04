<template>
    <div>
        <h1>submit Image</h1>
        <form @submit.prevent="onSubmit" @keydown.enter.prevent="onSubmit">
            <div class="form-group">
                <label for="title">title: </label>
                <input type="text" class="form-control" id="title" placeholder="画像タイトルを入力してください。" v-model="title" />
            </div>

            <div class="form-group">
                <label for="tag">tag: </label>
                <input type="text" class="form-control" id="tag" placeholder="Tagを入力してください。" v-model="tag" />
            </div>

            <div class="form-group">
                <label for="Image">Image: </label>
                <input type="file" @change="uploadImage" />
            </div>

            <div><button type="submit" class="btn btn-primary">Submit</button></div>
        </form>
    <div v-if="error">
        {{ errorMessage }}
    </div >

    </div>
</template>
<script setup lang="ts">
import axios from "axios";
import { reactive, ref } from "vue";
import {Auth} from '../store/store';
const AuthStore = Auth()
const hostAddress = "http://localhost:8000";
var title = ref('');
var tag = ref('');
var errorMessage=ref('');
const error = ref(false);
var fileForUpload = reactive({
    file: null,
});

const uploadImage = (e) => {
    //console.log("uploadImage");
    let file = e.target.files[0];//拿到上传的file
    //console.log(file.name);
    //let param = new FormData();//创建form对象
    fileForUpload.file = file;//为创建的form对象增加上传的文件
    //param.append("id", "1");//如果需要上传其他字段，在这里增加
    //return param;
    console.log(fileForUpload);
}



const onSubmit = (e) => {

    //let config = { headers: { "Username": AuthStore.username } }//修改请求头
    let url = hostAddress + "/ImageSubmit";//上传的url
    const un = AuthStore.username;
    //const postMsg={"title":title.value,"tag":tag.value,"file":fileForUpload.file};
    let param = new FormData();//创建form对象
    if (fileForUpload.file && title.value != '' && tag.value != '') {
        errorMessage.value="";
        error.value = false;
        param.append("title", title.value);
        param.append("tag", tag.value);//如果需要上传其他字段，在这里增加
        param.append("file", fileForUpload.file);//为创建的form对象增加上传的文件
        param.append("Username", un)
        //console.log(param.get("file"));
        axios.post(url, param).then((res) => {
            errorMessage.value="画像をアップロードしました。";
            error.value = true;
        })}
        else{
            if(fileForUpload.file == null){
                errorMessage.value="ファイルを選択してください。";
                error.value = true;
                }
            if (title.value == '') {
            errorMessage.value="タイトルを入力してください。";
            error.value = true;
                }
            if (tag.value == '') {
                errorMessage.value="タグを入力してください。";
                error.value = true;
            }
        }
}

</script>
<style>
</style>