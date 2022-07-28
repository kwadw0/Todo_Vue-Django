<script>
import axios from 'axios';

export default {
    data() {
        return {
            info: null
        };
    },
    mounted() {
        axios
            .get('http://127.0.0.1:8000/api/')
            .then(reponse => (this.info = reponse.data))

    }
}
</script>
<template>
    <div class="container mt-4">
        <div class="row justify-content-md-center">
            <div class="col-md-6">
                <div class="card mt-2" v-for="todo in info" :key="id" style="width: 35rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{todo.title}}</h5>
                        <p class="card-text">{{todo.description}}
                        </p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
</style>