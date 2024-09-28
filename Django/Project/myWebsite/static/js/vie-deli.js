$(document).ready(function () {
  $("#go-top-btn").click(function () {
    $("html").animate({ scrollTop: 0 }, 500);
    return false;
  });
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $("#go-top-btn").fadeIn();
    } else {
      $("#go-top-btn").fadeOut();
    }
  });
});

$(document).ready(function () {
  $(".nav-bar-icon").click(function () {
    $(".main-menu").animate({ width: "100%" }, 200);
  });

  $(".close-btn").click(function () {
    $(".main-menu").animate({ width: "0" }, 200);
  });

  $(".search-icon").click(function () {
    showSearch();
  });
});

function showSearch() {
  let windowWidth = $(window).width();

  if (windowWidth >= 700) {
    $(".overlay").fadeIn(300);

    $(".close-search-btn").click(function () {
      $(".overlay").fadeOut(300);
    });

    $(".search-btn").click(function () {
      $(".overlay").fadeOut(300);
    });
  } else {
    $(".search-mobile").fadeIn(300);
    $(".search-icon").animate({ width: "0%" }, 300);

    $(".search-mobile i").click(function () {
      $(".search-mobile").fadeOut(300);
      $(".search-icon").animate({ width: "8%" }, 300);
    });
  }
}

// Form Validate
document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Clear previous errors
    document.getElementById("nameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("phoneError").textContent = "";

    // Get form values
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var phone = document.getElementById("phone").value.trim();

    // Validation flags
    var valid = true;

    // Validate name
    if (name === "") {
      document.getElementById("nameError").textContent = "Vui lòng nhập họ tên";
      valid = false;
    }

    // Validate email
    if (email === "") {
        document.getElementById("emailError").textContent = "Vui lòng nhập email";
        valid = false;
      }

    // Validate phone
    if (phone === "") {
        document.getElementById("phoneError").textContent = "Vui lòng nhập sdt";
        valid = false;
      }

    if (valid) {
      alert("Form submitted successfully!");
    }
  });
