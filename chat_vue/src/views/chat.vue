<template>
<div class="container">
  <div class="dialogs">
    <div class="dialog" v-for="dialog in dialogs"
         :key="dialog.id">
      <div class="dialog__items">
        <p class="dialog__message" v-if="dialog.username">{{ dialog.username }}</p>
        <p class="dialog__message" v-if="!dialog.username">NoName</p>
        <p class="dialog__message">{{ dialog.message }}</p>
      </div>
    </div>
  </div>
  <form class="chats__form" @submit="sendMes" onsubmit="return false;">
    <input v-model="message" type="text" class="chats__form__input" placeholder="Enter your message">
    <button class="chats__form__button">send</button>
  </form>
  <form class="chats__form" v-if="chatType" @submit="inviteUser" onsubmit="return false;">
    <input v-model="username" type="text" class="chats__form__input" placeholder="Enter username to invite">
    <button class="chats__form__button">send</button>
  </form>
</div>
</template>

<script>
export default {
  name: "chat",
  data() {
    return {
      dialogs: [],
      message: '',
      chatSocket: '',
      userName: '',
      username: '',
      chatType: false
    }
  },
  created() {
    this.connect()
  },
  destroyed() {
    this.chatSocket.close();
    this.dialogs = [];
  },
  methods: {
    connect() {
      this.chatSocket = new WebSocket(
          'ws:'
          +
          '127.0.0.1:8000/'
          +
          'ws/'
          +
          'chat/'
          +
          this.$route.params.room_name
          +
          '/'
          +
          this.$route.params.chat_type
          +
          '/'
          +
          '?token='
          +
          localStorage.getItem('access_token')
      );
      this.userName = localStorage.getItem("username")
      this.chatSocket.onopen = () => {
        this.chatSocket.onmessage = ({data}) => {
          this.dialogs.push(JSON.parse(data));
          console.log(data);
          console.log(this.dialogs)
        };
      };
      if (this.$route.params.chat_type === 'constant'){
        this.chatType = true
      }
    },
    sendMes() {
      console.log()
      this.chatSocket.send(JSON.stringify({
        'message': this.message, 'username': this.userName
      }));
      this.message = "";
    },
    async inviteUser() {
      const data = {
        'user': this.username,
        'room': this.$route.params.room_name
      }
      const response = await fetch('http://127.0.0.1:8000/invite_person/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify(data)
      })
      const person = await response.json()
      if (response.status === 201) {
        console.log(person)
      }else{
        console.log(person)
      }
    }
  }
}
</script>

<style scoped>
.dialogs {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border: 1px solid rgba(180, 180, 180, .5);
  border-radius: 20px;
  width: 70%;
  align-items: center;
  justify-content: center;
  overflow-y: scroll;
  background-color: rgba(180, 180, 180, .5);
  height: 100vh;
  max-height: 450px;
}

.dialog {
  color: white;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: end;
}

.dialog__items {
  display: flex;
  padding-top: 20px;
  padding-left: 40px;
  flex-direction: column;
}

.dialog__message {
  padding-top: 5px;
}

.chats__form {
  margin-top: 20px;
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
</style>