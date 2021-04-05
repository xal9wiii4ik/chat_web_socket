<template>
<div class="container">
  <form class="login_form" @submit.prevent="submitLoginHandler">
    <div class="input__items">
      <div class="input__item">
        <h3 class="input__item__text">username</h3>
        <input v-model="login" type="text" class="input__item__input" placeholder="login">
      </div>
      <div class="input__item">
        <h3 class="input__item__text">password</h3>
        <input v-model="password" type="text" class="input__item__input" placeholder="password">
      </div>
      <div class="input__item">
        <a href="#" class="input__item__txt">Forgot Password</a>
      </div>
      <div class="input__item">
        <button class="input__item__button">sign in</button>
      </div>
    </div>
  </form>
</div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      login: '',
      password: '',
      email: ''
    }
  },
  methods: {
    async submitLoginHandler() {
      try {
        const data = {
          username: this.login,
          password: this.password
        }
        const response = await fetch('http://127.0.0.1:8000/auth/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        const token = await response.json()
        if (response.status === 200) {
          localStorage.setItem('access_token', token.access)
          localStorage.setItem('refresh_token', token.refresh)
          localStorage.setItem('username', data.username)
          localStorage.setItem('user_id', token.id)
          await this.$router.push('/')
          location.reload()
        } else {
          console.log(token)
        }
      } catch (e) {
        alert(e);
      }
    },
  //   async submitRememberHandler() {
  //     try {
  //       const data = {
  //         email: this.email
  //       }
  //       const response = await fetch(`http://localhost:8000/auth/reset_password/`, {
  //         method: 'POST',
  //         headers: {
  //           'Content-Type': 'application/json',
  //         },
  //         body: JSON.stringify(data)
  //       })
  //       if (response.status === 200) {
  //         console.log('200')
  //       } else {
  //         console.log('400')
  //       }
  //     } catch (e) {
  //       console.log(e)
  //     }
  //   }
  },
}
</script>
<style scoped>
.login_form {
  margin: 0 auto;
  width: 50%;
  padding-top: 50px;
  display: flex;
  flex-direction: column;
}

.input__items {
  display: flex;
  flex-direction: column;
}

.input__item {
  padding-top: 20px;
  padding-bottom: 20px;
}

.input__item__text {
  color: white;
  font-size: 15px;
  text-transform: uppercase;
  text-align: left;
  padding-bottom: 10px;
}

.input__item__input {
  outline: none;
  width: 100%;
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

.input__item__button {
  width: 100%;
  color: white;
  border-radius: 100px;
  background-color: rgba(255, 20, 147, .7);
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 20px;
  text-transform: uppercase;
}

.input__item__txt {
  font-size: 20px;
  color: rgb(180, 180, 180);
}

</style>