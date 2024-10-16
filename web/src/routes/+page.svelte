<script>
  import Footer from '../components/Footer.svelte';

  let name = '';
  let username = '';
  let email = '';
  let checked = false;
  let result = undefined;

  async function subscribe() {
    const params = {
      name: name,
      username: username,
      email: email,
      checked: checked,
    };
    let response = await fetch(`/api/subscribe?name=${name}&username=${username}&email=${email}&checked=${checked}`);
    let data = await response.json();
    result = data;
  }
  function cancel() {
  }
</script>

<svelte:head>
  <title>FastSvelte App</title>
</svelte:head>

<section class="hero">
  <div class="hero-body">
    <p class="title">
      FastSvelte App
    </p>
  </div>
</section>

<div class="section">
  <div class="container">
    <div class="content">

      <div class="notification is-danger">
        <button class="delete"></button>
        This form is an example.
        You don't need type your information.
        Subscribe button is a mock.
      </div>

      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input class="input" type="text" placeholder="Text input" bind:value="{name}">
        </div>
      </div>
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left has-icons-right">
          <input class="input is-success" type="text" placeholder="Text input" bind:value="{username}">
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </div>
        {#if username}
        <p class="help is-success">This username is available</p>
        {/if}
      </div>
      <div class="field">
        <label class="label">Email</label>
        <div class="control has-icons-left has-icons-right">
          <input class="input is-danger" type="email" placeholder="Email input" bind:value="{email}">
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
        </div>
        {#if email.length < 3}
        <p class="help is-danger">This email is invalid</p>
        {/if}
      </div>
      <div class="field">
        <div class="control">
          <label class="checkbox">
            <input type="checkbox" bind:checked={checked}>
            I agree to the <a href="#">terms and conditions</a>
          </label>
        </div>
      </div>
      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link" on:click={subscribe}>Subscribe!</button>
        </div>
        <div class="control">
          <button class="button is-link is-light" on:click={cancel}>Cancel</button>
        </div>
      </div>

      {#if result && result.status == "success"}
      <div class="notification is-info">
        <button class="delete"></button>
        {JSON.stringify(result)}
      </div>
      {:else if result && result.status == "failed"}
      <div class="notification is-danger">
        <button class="delete"></button>
        {JSON.stringify(result)}
      </div>
      {/if}

    </div>
  </div>
</div>

<Footer>A Template by @cympfh. Please use freely under MIT LICENSE.</Footer>

<style>
  @import "https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css";
  @import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css";
</style>
