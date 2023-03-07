let searchInput = document.getElementById('search-input');

searchInput.addEventListener('input', () => {

    query = searchInput.value;

    if (query === '') {
        document.getElementById('spin').style.visibility = 'hidden'
        const resultsContainer = document.querySelector('.results');
        resultsContainer.innerHTML = '';
    }

    else {
        search(query, 10, 'false')
    }

});


function search(query, max_results, adv) {
    if (query != undefined && max_results != undefined) {

        document.getElementById('spin').style.visibility = 'visible'

        fetch(`/search?q=${query}&max_results=${max_results}&adv=${adv}`)
            .then(response => response.json())
            .then(response => {
                
                if (query === document.getElementById('search-input').value) {
                    const resultsContainer = document.querySelector('.results');
                    resultsContainer.innerHTML = ''; 
                    const results = response['results'];
                    results.forEach(result => {
                        const resultDiv = document.createElement('div');
                        resultDiv.classList.add('result-item');
                        resultDiv.textContent = result['data'];
                        resultDiv.addEventListener('click', () => {
                            getinfo(result['id']);
                        });
                        resultsContainer.appendChild(resultDiv); 
                    });
                    const resultDiv = document.createElement('div');
                    resultDiv.classList.add('adv');
                    resultDiv.textContent = 'Do Advanced Search';
                    searchInput.disabled = false;
                    resultDiv.addEventListener('click', () => {
                        searchInput.disabled = true;
                        search(query, 10, 'true')
                    });
                    resultsContainer.appendChild(resultDiv); 


                    document.getElementById('spin').style.visibility = 'hidden'
                }

            }).catch(error => {
                console.error(error)
            });
    }
    else {
        throw new Error('query and max_results cannot be undefined')
    }
}

function getinfo(id){
    location.href = `/getinfo?id=${id}`
}
