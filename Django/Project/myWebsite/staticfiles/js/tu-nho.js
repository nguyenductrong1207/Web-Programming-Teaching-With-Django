document
  .getElementById("bookingForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var isValid = true;

    document.getElementById("nameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("phoneError").textContent = "";
    document.getElementById("dayComeError").textContent = "";
    document.getElementById("timeError").textContent = "";

    var name = document.getElementById("booking-form-user").value;
    var email = document.getElementById("booking-form-email").value;
    var phone = document.getElementById("booking-form-phone").value;
    var dateComing = document.getElementById("booking-form-date-coming").value;
    var timeComing = document.getElementById("booking-form-time-coming").value;

    if (name.trim() === "") {
      document.getElementById("nameError").textContent =
        "Tên khách hàng không được để trống";
      isValid = false;
    }

    if (email.trim() === "") {
      document.getElementById("emailError").textContent =
        "Email không được để trống";
      isValid = false;
    }

    if (phone.trim() === "") {
      document.getElementById("phoneError").textContent =
        "Số điện thoại không được để trống";
      isValid = false;
    }

    if (dateComing.trim() === "") {
      document.getElementById("dayComeError").textContent =
        "Ngày đến không được để trống";
      isValid = false;
    }

    if (timeComing.trim() === "") {
      document.getElementById("timeError").textContent =
        "Thời gian đến không được để trống";
      isValid = false;
    }

    if (isValid) {
      alert("Form submitted successfully!");
    }
  });

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 300 ||
    document.documentElement.scrollTop > 300
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
