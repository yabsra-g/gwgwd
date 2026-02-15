document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    // Select all items referencing the new class names I'll use in HTML
    let items = Array.from(document.querySelectorAll('.carousel-item'));

    // Initial State: center is index 2 (0, 1, [2], 3, 4) for 5 items
    let activeIndex = 2;

    function updateCarousel() {
        items.forEach((item, index) => {
            // Reset classes
            item.className = 'carousel-item';

            // Calculate distance in a circular manner for 5 items
            let diff = index - activeIndex;

            // Adjust diff to be within -2 to 2 for shortest path
            if (diff > 2) diff -= 5;
            if (diff < -2) diff += 5;

            if (diff === 0) {
                item.classList.add('active');
            } else if (diff === -1) {
                item.classList.add('prev-1');
            } else if (diff === -2) {
                item.classList.add('prev-2');
            } else if (diff === 1) {
                item.classList.add('next-1');
            } else if (diff === 2) {
                item.classList.add('next-2');
            }
        });
    }

    // Click to select
    items.forEach((item, index) => {
        item.addEventListener('click', () => {
            if (activeIndex !== index) {
                activeIndex = index;
                updateCarousel();
            }
        });
    });

    // Auto-play
    setInterval(() => {
        activeIndex = (activeIndex + 1) % items.length;
        updateCarousel();
    }, 4000);

    // Initial call
    updateCarousel();
});
