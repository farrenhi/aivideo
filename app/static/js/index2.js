document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    // const code_input = document.getElementById('code');
    const searchButton = document.querySelector('.search-button');
    const loadingSpinner = document.getElementById('loading-spinner');

    const link_box = document.getElementById('link_box');

    const sourceElement = document.getElementById('video_src');
    const videoElement = document.getElementById('video');
    const download_button = document.getElementById('downloadBtn');

    const start_btn = document.getElementById('start_btn');
    start_btn.addEventListener('click', go_to_main_page);
    function go_to_main_page() {
        document.getElementById('landing_page_box').style.display = 'none';
        document.getElementById('welcome-banner').style.display = 'flex';
    }

    searchButton.addEventListener('click', performSearch);
    function performSearch() {
        // Show the loading spinner
        // loadingSpinner.classList.remove('hidden');
        loadingSpinner.style.display = 'block';

        // user_code_input = code_input.value;
        userInput = searchInput.value;
        document.getElementById('video').style.display = 'none';

        // const url = `/api/attractions?keyword=${userInput}&code=${user_code_input}`;
        const url = `/api/shooting?keyword=${userInput}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                console.log(data.message);
                } else {
                // Hide the loading spinner once fetch is complete
                // loadingSpinner.classList.add('hidden');
                loadingSpinner.style.display = 'none';

                // Process and display new data
                videoElement.style.display = 'block';
                link_box.style.display = 'flex';

                sourceElement.src = data.data.video_url;
                download_button.href = data.data.video_url;
                // urlDisplay.textContent = data.data;

                videoElement.load();
                videoElement.play();
                }})
            .catch(error => {
                // Hide the loading spinner in case of an error
                loadingSpinner.classList.add('hidden');
                console.error('Fetch Error:', error);
                
            });
    }
});
