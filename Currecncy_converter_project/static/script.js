const amountInput = document.getElementById('amount');
const fromCurrency = document.getElementById('Coun-Currency-from');
const toCurrency = document.getElementById('Coun-Currency-to');
const resultCard = document.getElementById('resultCard');
const conversionResult = document.getElementById('conversionResult');
const lastUpdated = document.getElementById('lastUpdated');
const loadingIndicator = document.getElementById('loading');
const newsSection = document.getElementById('newsSection');
const newsArticles = document.getElementById('newsArticles');

// Fetch exchange rates
async function fetchRates() {
    try {
        loadingIndicator.classList.remove('hidden');
        const response = await fetch('/get_rates');
        const data = await response.json();
        const currencies = Object.keys(data.conversion_rates);

        currencies.forEach(currency => {
            const option1 = document.createElement('option');
            option1.value = currency;
            option1.textContent = currency;
            fromCurrency.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = currency;
            option2.textContent = currency;
            toCurrency.appendChild(option2);
        });
        loadingIndicator.classList.add('hidden');
    } catch (error) {
        console.error('Error fetching rates:', error);
    }
}

// Fetch news
async function fetchNews() {
    try {
        const response = await fetch('/get_news');
        const data = await response.json();
        data.articles.forEach(article => {
            const articleDiv = document.createElement('div');
            articleDiv.innerHTML = `
                <h3>${article.title}</h3>
                <p>${article.description}</p>
                <a href="${article.url}" target="_blank">Read more</a>
            `;
            newsArticles.appendChild(articleDiv);
        });
        newsSection.classList.remove('hidden');
    } catch (error) {
        console.error('Error fetching news:', error);
    }
}

// Perform currency conversion
async function convertCurrency() {
    const amount = amountInput.value;
    const from = fromCurrency.value;
    const to = toCurrency.value;

    if (amount === '' || isNaN(amount)) {
        alert('Please enter a valid amount');
        return;
    }

    try {
        loadingIndicator.classList.remove('hidden');
        const response = await fetch(`/get_rates`);
        const data = await response.json();
        const exchangeRate = data.conversion_rates[to];
        const convertedAmount = (amount * exchangeRate).toFixed(2);
        conversionResult.textContent = `${amount} ${from} = ${convertedAmount} ${to}`;
        lastUpdated.textContent = new Date().toLocaleString();
        resultCard.classList.remove('hidden');
        loadingIndicator.classList.add('hidden');
    } catch (error) {
        console.error('Error converting currency:', error);
    }
}

// Initialize on page load
window.onload = () => {
    fetchRates();
    fetchNews();
};

// Add event listener to convert button
document.getElementById('convertBtn').addEventListener('click', convertCurrency);
