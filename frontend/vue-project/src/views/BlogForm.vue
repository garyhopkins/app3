<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const formData = ref({
  title: "",
  body: "",
  positive_number: "",
});

let response_status = ref("nothing yet");
let response_payload = ref("nothing yet");

const router = useRouter();

//console.log(response_status);

const submitForm = () => {
  axios
    .post("http://localhost:8080/post-list/", formData.value)
    .then(function (response) {
      response_status.value = response.status;
      response_payload.value = response.data;
      console.log(response_status.value);
      router.push({
        name: "home",
      });
    })
    .catch(function (error) {
      response_status.value = error.response.status;
      response_payload.value = error.response.data;
      console.log(error);
    })
    .finally(function () {});

  formData.value = {
    title: "",
    body: "",
    posnum: "",
  };
};
</script>

<template>
  <div class="title">Add New Blog Posting</div>
  <br />

  <form id="form1" @submit.prevent="submitForm()">
    <label for="title">Title:</label>
    <input v-model="formData.title" name="title" /><br /><br />

    <label for="body">Body:</label>
    <input v-model="formData.body" name="body" /><br /><br />

    <label for="posnum">Positive Number:</label>
    <input v-model="formData.positive_number" name="posnum" /><br /><br />

    <input type="submit" value="Submit" />
  </form>

  <p>Response payload is {{ response_payload }}</p>
  <p>Response status is {{ response_status }}</p>

  <a href="/">Back Home</a>
</template>

<style scoped>
.title {
  font-size: x-large;
}
</style>