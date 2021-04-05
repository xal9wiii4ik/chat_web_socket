<template>
<div class="container">
  <div class="rooms">
    <div class="room" v-for="room in rooms"
         :key="room.id">
      <div class="room__items">
        <p class="room__item__name">{{ room.name }}</p>
        <a :href="`/chat/${room.name}/constant`" class="room__item__link">move</a>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "my_chats",
  data() {
    return {
      rooms: []
    }
  },
  mounted() {
    this.getMyRooms()
  },
  methods: {
    async getMyRooms() {
      const response = await fetch('http://127.0.0.1:8000/rooms/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('access_token')}`
        },
      })
      if (response.status === 200) {
        this.rooms = await response.json()

      }else{
        console.log('not found')
      }
    }
  }
}
</script>

<style scoped>

.rooms {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  width: 70%;
  align-items: center;
  justify-content: center;
  overflow-y: scroll;
  height: 100vh;
  max-height: 450px;
}

.room__items {
  display: flex;
  flex-direction: row;
  padding: 40px;
  justify-content: space-between;
}

.room__item__name {
  font-style: italic;
  color: white;
  padding-right: 20px;
  font-size: 20px;
}

.room__item__link {
  color: white;
  text-transform: uppercase;
  font-size: 20px;
}

</style>