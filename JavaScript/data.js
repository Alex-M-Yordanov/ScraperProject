function createProductHTML(product) {
    return `
        <div class="product">
            <p><strong>Name:</strong> ${product.title}</p>
            <p><strong>Price:</strong> ${product.price}</p>
            <p><strong>Link:</strong> <a href="${product.link}" target="_blank">View Product</a></p>
        </div>
    `;
}


function generateProductColumns(results) {

    const ardesColumn = document.getElementById('ardes-column');
    const emagColumn = document.getElementById('emag-column');
    const technopolisColumn = document.getElementById('technopolis-column');
    const sortButton = document.getElementById('sortButton');

    ardesColumn.innerHTML = '<h2>Ardes.bg</h2>';
    emagColumn.innerHTML = '<h2>Emag.bg</h2>';
    technopolisColumn.innerHTML = '<h2>Technopolis.bg</h2>';

    
    // fill  columns
    results['ardes.bg'].forEach(product => {
        ardesColumn.innerHTML += createProductHTML(product);
    });
    results['emag.bg'].forEach(product => {
        emagColumn.innerHTML += createProductHTML(product);
    });
    results['technopolis.bg'].forEach(product => {
        technopolisColumn.innerHTML += createProductHTML(product);
    });
   
    // hadle event listener for the sorting button
    sortButton.style.display = 'block';
    
    function createSortDataHandler(results) {
        return function() {
            sortProductsByPrice(results);
        };
      }
    sortButton.removeEventListener('click', sortButton.sortDataHandler);
    sortButton.sortDataHandler = createSortDataHandler(results);
    sortButton.addEventListener('click', sortButton.sortDataHandler);
   
}


// Sorting logic

let sortOrderAscending = true;

function sortFunction(a, b) {
    
    const priceA = parseFloat(a.price);
    const priceB = parseFloat(b.price);
    return sortOrderAscending ? priceA - priceB : priceB - priceA;
    
}

async function sortProductsByPrice(results) {

    const ardesColumn = document.getElementById('ardes-column');
    const emagColumn = document.getElementById('emag-column');
    const technopolisColumn = document.getElementById('technopolis-column');

    // Sort products 
    const sorted_ardes = results['ardes.bg'].sort(sortFunction);
    const sorted_emag = results['emag.bg'].sort(sortFunction);
    const sorted_technopolis = results['technopolis.bg'].sort(sortFunction);

    // Clear columns
    ardesColumn.innerHTML = '<h2>Ardes.bg</h2>';
    emagColumn.innerHTML = '<h2>Emag.bg</h2>';
    technopolisColumn.innerHTML = '<h2>Technopolis.bg</h2>';

    // fill columns with sorted products
    sorted_ardes.forEach(product => {
        ardesColumn.innerHTML += createProductHTML(product);
    });
    sorted_emag.forEach(product => {
        emagColumn.innerHTML += createProductHTML(product);
    });
    sorted_technopolis.forEach(product => {
        technopolisColumn.innerHTML += createProductHTML(product);
    });

    // change sorting order
    sortOrderAscending = !sortOrderAscending;
}


function main(){   
    //recieve data from backend 
    async function searchFormSubmitHandler(event) {
        event.preventDefault(); 
        const keywords = document.getElementById('keywords').value; 
        const response = await fetch('http://127.0.0.1:5000/search', {
            method: 'POST', 
            headers: { 'Content-Type': 'application/json' }, 
            body: JSON.stringify({ keywords: keywords }) 
        });
        const data = await response.json(); 
        generateProductColumns(data); 
    }
    
    document.getElementById('searchForm').addEventListener('submit', searchFormSubmitHandler);
}

document.addEventListener('DOMContentLoaded', main);

