document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const code_input = document.getElementById('code');
    const searchButton = document.querySelector('.search-button');

    const videoElement = document.getElementById('video');
    const linkBoxElement = document.getElementById('link_box');
    // const linkBoxElement = document.querySelector('.link_box');

    const sourceElement = document.getElementById('video_src');
    const download_button = document.getElementById('downloadBtn');
    
    searchButton.addEventListener('click', performSearch);
    
    function performSearch() {
        console.log("clicked!");
        user_code_input = code_input.value;
        userInput = searchInput.value;

        const url = `/api/attractions?keyword=${userInput}&code=${user_code_input}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {               
                // Process and display new data
                sourceElement.src = data.data; // if local storage: '/' + data.data;
                download_button.href = data.data;

                videoElement.style.display = 'block';
                linkBoxElement.style.display = 'block';
                
                linkBoxElement.load();
                videoElement.load(); // Reload the video element
                videoElement.play(); // Play the video
  
            })
            .catch(error => console.error('Error:', error));
    }
});
