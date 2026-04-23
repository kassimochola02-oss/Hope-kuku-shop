// Function for payment interaction
function showPay(method) {
  const amount = "1,200";
  if (method === "Bitcoin") {
    alert(
      `Generating Lightning Invoice for ${amount} KES equivalent in Sats...`,
    );
  } else {
    alert(`Requesting M-Pesa STK Push for ${amount} KES to Rich Chicken Hub.`);
  }
}

// Fun Scroll Effect
window.addEventListener("scroll", () => {
  const nav = document.querySelector("nav");
  if (window.scrollY > 50) {
    nav.style.background = "rgba(255, 102, 0, 0.9)";
    nav.style.transition = "0.5s";
  } else {
    nav.style.background = "transparent";
  }
});

// Interactive Image Alert for the Map tag
document.querySelector("area").addEventListener("mouseover", function () {
  console.log("Customer is hungry for chicken!");
});
