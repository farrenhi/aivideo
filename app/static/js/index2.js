document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const code_input = document.getElementById('code');
    const searchButton = document.querySelector('.search-button');
    const loadingSpinner = document.getElementById('loading-spinner');

    searchButton.addEventListener('click', performSearch);

    function performSearch() {
        // Show the loading spinner
        // loadingSpinner.classList.remove('hidden');
        loadingSpinner.style.display = 'block';

        user_code_input = code_input.value;
        userInput = searchInput.value;
        document.getElementById('video').style.display = 'none';
        let sourceElement = document.getElementById('video_src');
        let videoElement = document.getElementById('video');
        const url = `/api/attractions?keyword=${userInput}&code=${user_code_input}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Hide the loading spinner once fetch is complete
                // loadingSpinner.classList.add('hidden');
                loadingSpinner.style.display = 'none';

                // Process and display new data
                document.getElementById('video').style.display = 'block';

                sourceElement.src = data.data;
                videoElement.load();
                videoElement.play();
            })
            .catch(error => {
                // Hide the loading spinner in case of an error
                loadingSpinner.classList.add('hidden');
                console.error('Error:', error);
            });
    }
});
