<template>
<div class="container">
  <form class="login_form">
    <div class="input__items">
      <div class="input__item">
        <h3 class="input__item__text">username</h3>
        <input type="text" class="input__item__input" placeholder="login">
      </div>
      <div class="input__item">
        <h3 class="input__item__text">password</h3>
        <input type="text" class="input__item__input" placeholder="login">
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

    }
  }
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