<script setup>
import { ref, onMounted } from "vue";

const allowed = ref(false);
const expectedHash = "8bdb8a4e290b4228be173b495635360c28fe4815b6cb8491d6745597fd400192";

async function sha256Hex(text) {
  const data = new TextEncoder().encode(text);
  const buf = await crypto.subtle.digest("SHA-256", data);
  return [...new Uint8Array(buf)]
    .map(b => b.toString(16).padStart(2, "0"))
    .join("");
}

onMounted(async () => {
  const input = prompt("Enter password");
  if (!input) {
    document.write("<h1 style='text-align:center;margin-top:20%'>Access denied</h1>");
    return;
  }
  const hash = await sha256Hex(input);
  if (hash === expectedHash) {
    allowed.value = true;
  } else {
    document.write("<h1 style='text-align:center;margin-top:20%'>Access denied</h1>");
  }
});
</script>

<template>
  <div v-if="allowed">
    <h1>You did it!</h1>
    <p>
      Visit
      <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a>
      to read the documentation
    </p>
  </div>
</template>

<style scoped></style>