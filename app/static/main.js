document.addEventListener("DOMContentLoaded", () => {
  const flashMessages = document.querySelectorAll(".flash");
  flashMessages.forEach((flash) => {
    setTimeout(() => flash.classList.add("show"), 100);
    setTimeout(() => flash.classList.remove("show"), 3100);
  });
});

function validateForm() {
  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const nameError = document.querySelector(".name-error");
  const phoneError = document.querySelector(".phone-error");
  const nameRegex = /^[\u4e00-\u9fa5]{2,4}$/;
  const phoneRegex = /^\d{11}$/;

  let valid = true;

  if (!nameRegex.test(name)) {
    nameError.textContent = "请输入正确的姓名";
    valid = false;
  } else {
    nameError.textContent = "";
  }

  if (!phoneRegex.test(phone)) {
    phoneError.textContent = "请输入正确的电话";
    valid = false;
  } else {
    phoneError.textContent = "";
  }

  return valid;
}
