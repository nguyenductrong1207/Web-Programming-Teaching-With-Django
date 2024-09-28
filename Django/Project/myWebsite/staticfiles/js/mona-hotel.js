// go to button
let mybutton = document.getElementById("myBtn");

window.onscroll = function () {
  scrollFunction();
  myFunction();
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

// sticky menu
var navbar = document.getElementById("nav");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}

// menu nav
function openNav() {
  document.getElementById("navMobile").style.width = "200px";
}

function closeNav() {
  document.getElementById("navMobile").style.width = "0";
}

// form validate
document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Clear previous errors

    // Get form values

    // Validation flags
    var valid = true;

    // Validate name

    // Validate phone

    // Validate dayCome

    // Validate dayOut

    // Validate quantity

    if (valid) {
      alert("Form submitted successfully!");
    }
  });
