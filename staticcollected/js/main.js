document.addEventListener("DOMContentLoaded", () => {

    const sortBtn = document.getElementById("sortBtn");
    const sortMenu = document.getElementById("sortMenu");
    const sortChevron = document.getElementById("sortChevron");
    const selectedSort = document.getElementById("selectedSort");

    // Toggle dropdown
    sortBtn.addEventListener("click", () => {
        const open = sortMenu.classList.contains("scale-y-100");

        if (open) {
            // Close animation
            sortMenu.classList.add("opacity-0", "scale-y-0", "translate-x-10", "pointer-events-none");
            sortMenu.classList.remove("opacity-100", "scale-y-100", "translate-x-0", "pointer-events-auto");

            sortBtn.classList.add("border-gray-500");
            sortChevron.classList.remove("rotate-180");
        } else {
            // Open animation
            sortMenu.classList.remove("opacity-0", "scale-y-0", "translate-x-10", "pointer-events-none");
            sortMenu.classList.add("opacity-100", "scale-y-100", "translate-x-0", "pointer-events-auto");

            // Remove border while open
            sortBtn.classList.remove("border-gray-500");
            sortBtn.classList.add("border-transparent");

            sortChevron.classList.add("rotate-180");
        }
    });

    // Update selected option
    document.querySelectorAll(".sort-option").forEach(option => {
        option.addEventListener("click", () => {
            selectedSort.textContent = option.textContent;

            // Close after selecting
            sortMenu.classList.add("opacity-0", "scale-y-0", "translate-x-10", "pointer-events-none");
            sortMenu.classList.remove("opacity-100", "scale-y-100", "translate-x-0", "pointer-events-auto");

            sortBtn.classList.add("border-gray-500");
            sortBtn.classList.remove("border-transparent");
            sortChevron.classList.remove("rotate-180");
        });
    });

    // Click outside to close dropdown
    document.addEventListener("click", (e) => {
        if (!sortBtn.contains(e.target) && !sortMenu.contains(e.target)) {
            sortMenu.classList.add("opacity-0", "scale-y-0", "translate-x-10", "pointer-events-none");
            sortMenu.classList.remove("opacity-100", "scale-y-100", "translate-x-0", "pointer-events-auto");

            sortBtn.classList.add("border-gray-500");
            sortBtn.classList.remove("border-transparent");

            sortChevron.classList.remove("rotate-180");
        }
    });

});


// productcard
document.addEventListener("DOMContentLoaded", () => {

    const gridBtn = document.getElementById("gridViewBtn");
    const listBtn = document.getElementById("listViewBtn");
    const productGrid = document.getElementById("productGrid");
    const cards = document.querySelectorAll(".theme-card-wrapper");

    /* ---------------- GRID VIEW ---------------- */
    function enableGrid() {

        gridBtn.classList.add("bg-[#76C01D]", "text-[#0056B3]");
        listBtn.classList.remove("bg-[#76C01D]", "text-[#0056B3]");

        productGrid.classList.remove("grid-cols-1", "rounded-full");
        productGrid.classList.add("sm:grid-cols-2", "lg:grid-cols-2");

        cards.forEach(card => {
            const gridView = card.querySelector(".grid-view");
            const listView = card.querySelector(".list-view");

            listView.classList.add("hidden");
            gridView.classList.remove("hidden");

            // Tailwind animation
            card.classList.remove("slide-up");
            card.classList.add("scale-in");
        });
    }

    /* ---------------- LIST VIEW ---------------- */
    function enableList() {

        listBtn.classList.add("bg-[#76C01D]", "text-[#0056B3]");
        gridBtn.classList.remove("bg-[#76C01D]", "text-[#0056B3]");

        productGrid.classList.add("grid-cols-1");
        productGrid.classList.remove("sm:grid-cols-2", "lg:grid-cols-2");

        cards.forEach(card => {
            const gridView = card.querySelector(".grid-view");
            const listView = card.querySelector(".list-view");

            gridView.classList.add("hidden");
            listView.classList.remove("hidden");

            // Tailwind animation
            card.classList.remove("scale-in");
            card.classList.add("slide-up");
        });
    }

    gridBtn.addEventListener("click", enableGrid);
    listBtn.addEventListener("click", enableList);

    enableGrid();
});

// cart icon
document.addEventListener("DOMContentLoaded", function () {

    const modal = document.getElementById("cart-modal");
    const modalImage = document.getElementById("modal-image");
    const modalPrice = document.getElementById("modal-price");
    const closeModal = document.getElementById("close-modal");

    // Close modal
    function hideModal() {
        modal.classList.add("hidden");
    }

    closeModal?.addEventListener("click", hideModal);

    modal?.addEventListener("click", function (e) {
        if (e.target === modal) hideModal();
    });

    // Listen for ANY cart button
    document.body.addEventListener("click", async function (event) {

        const btn = event.target.closest(".add-to-cart-btn");
        if (!btn) return;

        event.preventDefault();

        const themeId = btn.dataset.id;
        const image = btn.dataset.image;
        const price = btn.dataset.price;

        // AJAX request to add item
        const response = await fetch(`/cart/add-ajax/${themeId}/`);
        const data = await response.json();

        if (data.success) {
            modalImage.src = image;
            modalPrice.textContent = "$" + price;
            modal.classList.remove("hidden");
        }
    });
});


// FAQ
document.querySelectorAll(".faq-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
        const content = btn.nextElementSibling;
        const icon = btn.querySelector("i");

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            icon.classList.remove("rotate-180");
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            icon.classList.add("rotate-180");
        }
    });
});

// Signin

function openModal() {
    document.getElementById("authModal").classList.remove("hidden");
}

function closeModal() {
    document.getElementById("authModal").classList.add("hidden");
}

// checkout
document.getElementById("continueBtn").addEventListener("click", function () {

    let valid = true;

    function validate(id, condition) {
        const field = document.getElementById(id);
        const error = document.getElementById("err_" + id);

        if (condition) {
            field.classList.remove("border-red-500");
            error.classList.add("hidden");
        } else {
            valid = false;
            field.classList.add("border-red-500");
            error.classList.remove("hidden");
        }
    }

    validate("firstName", firstName.value.trim() !== "");
    validate("lastName", lastName.value.trim() !== "");
    validate("email", /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value));
    validate("phone", /^[0-9]{10}$/.test(phone.value));
    validate("flat", flat.value.trim() !== "");
    validate("address", address.value.trim() !== "");
    validate("city", city.value.trim() !== "");
    validate("state", state.value.trim() !== "");
    validate("pincode", /^[0-9]{6}$/.test(pincode.value));

    if (valid) {
        document.getElementById("step1").classList.add("hidden");
        document.getElementById("step2").classList.remove("hidden");
    }
});

document.getElementById("backBtn").addEventListener("click", function () {
    document.getElementById("step2").classList.add("hidden");
    document.getElementById("step1").classList.remove("hidden");
});

// payment
document.getElementById("payNowBtn").addEventListener("click", function () {

    // Generate Transaction ID
    const txnId = Math.floor(Math.random() * 900000000000 + 100000000000);

    // Format Date
    const today = new Date();
    const options = { day: "2-digit", month: "long", year: "numeric" };
    const formattedDate = today.toLocaleDateString("en-US", options);

    // Fill Modal
    document.getElementById("txnId").innerText = txnId;
    document.getElementById("txnDate").innerText = formattedDate;

    // Show Modal
    document.getElementById("paymentModal").classList.remove("hidden");

    // 🔥 Clear Cart AJAX request
    fetch("/clear-cart-ajax/")
        .then(response => response.json())
        .then(data => console.log("Cart cleared:", data.success));
});
