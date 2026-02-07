document.addEventListener("DOMContentLoaded", function () {
  const carousels = document.querySelectorAll("[data-carousel]");
  if (!carousels.length) return;

  carousels.forEach((carousel) => {
    const images = Array.from(carousel.querySelectorAll(".sg-image"));
    const prevBtn = carousel.querySelector(".sg-prev");
    const nextBtn = carousel.querySelector(".sg-next");
    const caption = carousel.nextElementSibling && carousel.nextElementSibling.classList.contains("sg-caption")
      ? carousel.nextElementSibling
      : null;

    if (!images.length || !prevBtn || !nextBtn) return;

    let idx = Math.max(0, images.findIndex(img => img.classList.contains("is-active")));
    if (idx < 0) idx = 0;

    function render() {
      images.forEach((img, i) => {
        img.classList.toggle("is-active", i === idx);
      });
      if (caption) {
        caption.textContent = images[idx].getAttribute("alt") || "";
      }
    }

    prevBtn.addEventListener("click", function (e) {
      e.preventDefault();
      idx = (idx - 1 + images.length) % images.length;
      render();
    });

    nextBtn.addEventListener("click", function (e) {
      e.preventDefault();
      idx = (idx + 1) % images.length;
      render();
    });

    render();
  });
});
