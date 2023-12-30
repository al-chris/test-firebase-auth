document.addEventListener('DOMContentLoaded', function () {
    // Define the intersection observer configuration
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5, // Adjust the threshold based on your needs
    };

    // Create an intersection observer instance
    const observer = new IntersectionObserver(handleIntersection, options);

    // Define the callback function for intersection observer
    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Load the card content when it becomes visible
                loadCardContent(entry.target);
                // Unobserve the target to avoid redundant calls
                observer.unobserve(entry.target);
            }
        });
    }

    // Load card content dynamically (replace this with your API call logic)
    function loadCardContent(target) {
        // Example: Fetch card data from an API
        // Replace this with your actual API endpoint and data structure
        fetch('https://api.example.com/cards')
            .then(response => response.json())
            .then(data => {
                // Create a card element and append it to the target container
                const cardElement = createCardElement(data);
                target.appendChild(cardElement);
            })
            .catch(error => console.error('Error fetching card data:', error));
    }

    // Example: Create a card element
    function createCardElement(cardData) {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${cardData.image}" class="card-img-top" alt="${cardData.title}">
            <div class="card-body">
                <h5 class="card-title">${cardData.title}</h5>
                <p class="card-text">${cardData.description}</p>
                <p class="card-text">Slots: ${cardData.slots}</p>
                <a href="${cardData.detailsLink}" class="btn btn-primary">Details</a>
            </div>
        `;
        return card;
    }

    // Observe the card containers
    const featuredCards = document.getElementById('featured-cards');
    const newArrivals = document.getElementById('new-arrivals');
    const popularCards = document.getElementById('popular-cards');
    const trendingCards = document.getElementById('trending-cards');

    if (featuredCards) {
        observer.observe(featuredCards);
    }

    if (newArrivals) {
        observer.observe(newArrivals);
    }

    if (popularCards) {
        observer.observe(popularCards);
    }

    if (trendingCards) {
        observer.observe(trendingCards);
    }
});
