<template>
  <div class="navbar-wrapper">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Feed Automator</b-navbar-brand>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>
.navbar-wrapper {
  position: sticky;
  top: 0;
  left: 0;
  box-shadow: 1px 1px 1px 1px rgba(50, 50, 50, 0.5);
  margin-bottom: 10px;
  z-index: 1;
}
</style>
