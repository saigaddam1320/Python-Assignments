// ---------- 1. Factorial Calculator ----------
function factorial(n) {
    if (n < 0) return "❌ Invalid (negative)";
    let result = 1;
    for (let i = 1; i <= n; i++) result *= i;
    return result;
  }
  
  console.log("Factorial(5) =", factorial(5)); // example log

  document.getElementById("num1")
document.getElementById("num2")
document.getElementById("calc-result")
  
    if (isNaN(num1) || isNaN(num2)) {
      resultBox.textContent = "Enter both numbers!";
      return;
    }
  
    let result;
    switch (op) {
      case "add": result = num1 + num2; break;
      case "sub": result = num1 - num2; break;
      case "mul": result = num1 * num2; break;
      case "div":
        result = num2 === 0 ? "Cannot divide by zero" : num1 / num2;
        break;
    }
    resultBox.textContent = `Result: ${result}`;
  }  
  // ---------- 3. Contact Form Validation ----------
  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contact-form");
    if (!form) return;
  
    form.addEventListener("submit", (e) => {
      e.preventDefault();
  
      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const message = document.getElementById("message").value.trim();
      const errorBox = document.getElementById("error");
  
      errorBox.style.display = "none";
  
      if (!name || !email || !message) {
        errorBox.textContent = "All fields are required.";
        errorBox.style.display = "block";
        return;
      }
  
      const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
      if (!emailRegex.test(email)) {
        errorBox.textContent = "Invalid email format.";
        errorBox.style.display = "block";
        return;
      }
  
      alert(`Thanks ${name}! Your message has been sent ✅`);
      form.reset();
    });
  });
  