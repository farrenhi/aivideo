document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.querySelector('.search-button');
    // const dataContainer = document.getElementById('part2_twelve');

    // searchInput.addEventListener('input', performSearch);
    
    searchButton.addEventListener('click', performSearch);
    
    function performSearch() {
        // if (nextPage === null) return;
        console.log("clicked!");
        userInput = searchInput.value;
        const url = `/api/attractions?keyword=${userInput}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Clear existing data
                // dataContainer.innerHTML = '';
                
                // Process and display new data
                let attractions = data.data;
                console.log(attractions)

                // nextPage = 0

                // get_data_12(attractions); // Reuse the existing function
            })
            .catch(error => console.error('Error:', error));
    }

    // function performSearch() {
    //     userInput = searchInput.value;
    //     if (userInput !== userInput_previous) {
    //         nextPage = 0
    //     } 

    //     if (nextPage === null) return;
    //     dataContainer.innerHTML = '';
    //     userInput_previous = userInput;
    //     get_data_12();
        
    // }
});
