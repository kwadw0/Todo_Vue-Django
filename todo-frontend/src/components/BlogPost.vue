<script>
export default {
    data() {
        return {
            postApi: [
                {
                    "id": 1,
                    "post": "Learn Vue"
                },
                {
                    "id": 2,
                    "post": "Learn Nvidia"
                },
                {
                    "id": 3,
                    "post": "Make sure to mine"
                }

            ]
        };
    }
}
</script>
<template>
    <div class="container">
        <div class="grid">
            <div class="col">
                <div class="row">
                    <p class="text-success h3 mt-3" v-for="post in postApi" :key="post.id">{{post.post}}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
</style>