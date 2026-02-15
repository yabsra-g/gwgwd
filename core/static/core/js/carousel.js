document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    // Select all items referencing the new class names I'll use in HTML
    let items = Array.from(document.querySelectorAll('.carousel-item'));

    // Initial State: center is roughly in the middle
    let activeIndex = Math.floor(items.length / 2);

    function updateCarousel() {
        const totalItems = items.length;

        items.forEach((item, index) => {
            // Reset classes
            item.className = 'carousel-item';

            // Calculate distance
            let diff = index - activeIndex;

            // Adjust diff to be within -totalItems/2 to totalItems/2 for shortest path
            if (diff > totalItems / 2) diff -= totalItems;
            if (diff < -totalItems / 2) diff += totalItems;

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
