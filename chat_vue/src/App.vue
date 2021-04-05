<template>
  <div id="nav">
    <nav class="header__nav">
      <ul class="header__list">
        <li class="header__list__item">
          <router-link class="header__list__link" to="/">
            <h4 class="header__list__link">Home</h4>
          </router-link>
        </li>
        <li class="header__list__item">
          <router-link class="header__list__link" to="/">
            <h4 class="header__list__link">My Chats</h4>
          </router-link>
        </li>
        <li class="header__list__item">
          <router-link class="header__list__link" to="/login">
            <h4 class="header__list__link">sign in</h4>
          </router-link>
        </li>
        <li class="header__list__item">
          <router-link class="header__list__link" to="/">
            <h4 class="header__list__link">sign up</h4>
          </router-link>
        </li>
        <li class="header__list__item">
          <router-link class="header__list__link" to="/">
          <h4 class="header__list__link">logout</h4>
          </router-link>
        </li>
      </ul>
    </nav>
  </div>
  <router-view/>
</template>

<style>

input::placeholder {
  color: white;
  font-style: italic;
}

html {
  scroll-behavior: smooth;
  overflow-x: hidden;
  width: 100%;
  height: 100%;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}

body {
  min-height: 100vh;
  overflow-x: hidden;
  background: url('login.jpeg') center/ cover no-repeat;
}

a {
  text-decoration: none;
}

.container {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  text-align: center;
}

button {
  text-decoration: none;
  cursor: pointer;
  border: none;
  color: white;
  border-radius: 100px;
  background-color: rgba(255,20,147, .7);
  padding: 15px;
  text-align: center;
  margin-left: 10px;
  font-size: 15px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding-top: 30px;
  padding-bottom: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.header__nav {
  width: 100%;
  text-transform: uppercase;
  padding: 5px;
}

.header__list {
  list-style-type: none;
  text-decoration: none;
  display: flex;
  flex-direction: row;
  text-align: center;
  justify-content: center;
}

.header__list__item {
  padding-left: 40px;
}

.header__list__link {
  color: white;
  text-transform: uppercase;
  font-size: 15px;
}
</style>
