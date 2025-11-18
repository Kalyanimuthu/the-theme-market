document.addEventListener("DOMContentLoaded", function () {
    const weekBtn = document.getElementById("btn-week");
    const monthBtn = document.getElementById("btn-month");
    const weekContainer = document.getElementById("week-container");
    const monthContainer = document.getElementById("month-container");

    weekBtn.addEventListener("click", () => {
        weekBtn.classList.add("bg-lime-500", "text-white");
        monthBtn.classList.remove("bg-lime-500", "text-white");

        weekContainer.classList.remove("hidden");
        monthContainer.classList.add("hidden");
    });

    monthBtn.addEventListener("click", () => {
        monthBtn.classList.add("bg-lime-500", "text-white");
        weekBtn.classList.remove("bg-lime-500", "text-white");

        monthContainer.classList.remove("hidden");
        weekContainer.classList.add("hidden");
    });
});
