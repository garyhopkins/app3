<script setup>
import { ref } from "vue";
import axios from "axios";

// Setting both variables as ref so they can be manipulated by the DOM

let blogPosts = ref([]);

// Setting isLoading to True help identify to the user that the API call is still loading and is not coompleted when it's True

let isLoading = ref(true);

// Make the API call and put the response.data into blogPosts
// Once the above has finished, set the isLoading variable to False

const makeGetCall = () => {
  axios
    .get("http://localhost:8080/post-list/")
    .then((response) => {
      blogPosts.value = response.data;
    })
    .then(() => (isLoading.value = false));
}

makeGetCall();

const deleteViaAPI = (id) => {
    axios.delete("http://localhost:8080/post-list/" + id + "/")
    .then((response) => {
      makeGetCall()
    })
}

// Setting to an empty array to test GET call with 0 results
/*
axios
  .get("http://localhost:8080/post-list/")
  .then((response) => {
    blogPosts.value = [];
  })
  .then(() => (isLoading.value = false))
*/

const deleteBlogPost = (id) => {
  console.log("Deleting blog post", id);
  blogPosts.value = blogPosts.value.filter((b) => {
    return b.id !== id;
  });
  console.log(blogPosts.value.length, "remaining");
};

// Testing Axios POST
/*
axios.post('http://localhost:8080/post-list/', {
  title: "Submitted via Axios",
  body: "New Body",
  positive_number: 500
})
*/
</script>

<template>
  <div class="title">Here are my blog posts</div>

  <p v-if="isLoading === true">Loading.....</p>

  <p v-else-if="blogPosts.length === 0">0 results returned</p>

  <table v-else>
    <tr>
      <th>ID</th>
      <th>Title</th>
      <th>Body</th>
      <th>Delete Me</th>
      <th>Delete Me via API</th>
    </tr>
    <tr v-for="blogpost in blogPosts" :key="blogpost.id">
      <td>{{ blogpost.id }}</td>
      <td>{{ blogpost.title }}</td>
      <td>{{ blogpost.body }}</td>
      <td>
        <button class="delete-button-blue" @click="deleteBlogPost(blogpost.id)">
          Delete ID# {{ blogpost.id }} via Vue
        </button>
      </td>
      <td>
        <button class="delete-button" @click="deleteViaAPI(blogpost.id)">
          Delete ID# {{ blogpost.id }} via API
        </button>
      </td>
    </tr>
  </table>

  <a href="/addblog">Add New Blog Posting</a>
</template>

<style scoped>
.delete-button {
  color: red;
}

.delete-button-blue {
  color: blue;
  border-style: double;
}

.title {
  font-size: x-large;
}

button.huge {
  font-size: 5em;
}
</style>