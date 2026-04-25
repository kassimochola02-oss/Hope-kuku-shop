// Helper for user interaction when choosing M-Pesa.
function showMpesa() {
  alert(
    "Tap the M-Pesa button, then enter your phone number to complete the payment.",
  );
}

// Optional helper for Bitcoin wallet flow.
function showBitcoin() {
  const lightningAddress = "hopekuku@blink.sv";
  window.location.href = `lightning:${lightningAddress}`;
}

// Fun Scroll Effect, only if a nav exists on the page.
window.addEventListener("scroll", () => {
  const nav = document.querySelector("nav");
  if (!nav) return;

  if (window.scrollY > 50) {
    nav.style.background = "rgba(255, 102, 0, 0.9)";
    nav.style.transition = "0.5s";
  } else {
    nav.style.background = "transparent";
  }
});

// Only attach the map hover listener if an area exists.
const mapArea = document.querySelector("area");
if (mapArea) {
  mapArea.addEventListener("mouseover", function () {
    console.log("Customer is hungry for chicken!");
  });
}
