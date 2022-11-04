import {defineStore} from "pinia";
import { getTransitionRawChildren } from "vue";
//import { StoreName } from "./store-name";

export const Auth = defineStore("Auth", {
    state:()=> {
        return {
            username: '',
            token: '',
            signedIn: false,
            expires: "",
        }
    },
    getters: {},
    actions: {},     
        },)