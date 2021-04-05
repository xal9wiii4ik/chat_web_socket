<template>
  <div class="container">
    <div class="main">
      <form class="chats__form" @submit.prevent="chatHandler">
        <h4 class="chats__form__text"> You can connect to exist chat.</h4>
        <input v-model="roomName1" type="text" class="chats__form__input" placeholder="enter the name of chat">
        <button class="chats__form__button"> connect </button>
      </form>
      <h4 class="chats__form__text"> If you want to create permanent you should sign in</h4>
      <form class="chats__form" v-if="is_login" @submit.prevent="permanentChatHandler">
        <h4 class="chats__form__text"> You can create a permanent chat.</h4>
        <input v-model="roomName2" type="text" class="chats__form__input" placeholder="enter the name of chat">
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
      user_id: '',
      roomName1: '',
      roomName2: '',
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
      }else {
        this.is_login = false
      }
    },
    async chatHandler() {
      const data = {
        room: this.roomName1
      }
      const response = await fetch(`http://127.0.0.1:8000/chat/${data.room}/un_constant/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('access_token')}`
        }
      })
      const res = await response.json()
      if (response.status === 200) {
        await this.$router.push(`/chat/${data.room}/un_constant`)
      }
      else {
        console.log(res)
      }
    },
    async permanentChatHandler() {
      const data = {
        room: this.roomName2
      }
      const response = await fetch(`http://127.0.0.1:8000/chat/${data.room}/constant/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify(data)
      })
      const res = await response.json()
      if (response.status === 201) {
        await this.$router.push(`/chat/${data.room}/constant`)
      }
      else {
        console.log(res)
      }
    }
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