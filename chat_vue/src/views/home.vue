<template>
  <div class="container">
    <div class="main">
      <form class="chats__form">
        <h4 class="chats__form__text"> You can connect to exist chat.</h4>
        <input type="text" class="chats__form__input" placeholder="enter the name of chat">
        <button class="chats__form__button"> connect </button>
      </form>
      <h4 class="chats__form__text"> If you want to create permanent you should sign in</h4>
      <form class="chats__form" v-if="is_login">
        <h4 class="chats__form__text"> You can create a permanent chat.</h4>
        <input type="text" class="chats__form__input" placeholder="enter the name of chat">
        <button class="chats__form__button"> connect </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {
      is_login: false,
      user_id: ''
    }
  },
  async mounted() {
    await this.getLogin()
  },
  methods: {
    async getLogin() {
      if (localStorage.getItem('access_token')) {
        this.is_login = true
        this.user_id = localStorage.getItem('user_id')
        console.log(this.user_id)
      }else {
        this.is_login = false
      }
    },
  }
}
</script>

<style scoped>
.main {
  padding-top: 50px;
  display: flex;
  flex-direction: column;
}

.chats__form {
  padding: 30px;
}

.chats__form__text {
  padding-bottom: 10px;
  color: white;
  font-style: italic;
  font-size: 20px;
}

.chats__form__input {
  outline: none;
  width: 30%;
  border-radius: 100px;
  border-color: transparent;
  font-size: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  background-color: rgba(180, 180, 180, .5);
  color: white;
  text-decoration: none;
}

.chats__form__button {
  margin-left: 10px;
  color: white;
  border-radius: 100px;
  background-color: rgba(255,20,147, .7);
  padding: 15px;
  text-align: center;
  font-size: 15px;
}
</style>