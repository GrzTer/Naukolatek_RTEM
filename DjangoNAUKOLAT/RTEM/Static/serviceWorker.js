// // serviceWorker.js
// self.addEventListener('push', event => {
//     const data = event.data.json();
//     self.registration.showNotification(data.title, {
//         body: 'Notification from RealTimeEnergyManager',
//         icon: '/path/to/icons/icon-192x192.png'
//     });
// });
//
// function fetchEnergyPrice() {
//     fetch('https://api.energyprovider.com/pricing/current')
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('energyPrice').innerText = `Current Price: ${data.price} per kWh`;
//         })
//         .catch(error => console.error('Error fetching energy prices:', error));
// }
//
// // Call this function on page load and at regular intervals
// fetchEnergyPrice();
// setInterval(fetchEnergyPrice, 60000); // Update every minute
