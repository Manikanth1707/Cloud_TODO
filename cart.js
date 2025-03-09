// Retrieve cart items from localStorage
const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
const cartItemsContainer = document.getElementById('cart-items');

// Display cart items
function displayCartItems() {
    cartItemsContainer.innerHTML = ''; // Clear existing items
    cartItems.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.innerHTML = `
            <h3>${item.ProductName}</h3>
            <p>Price: $${item.Price}</p>
            <p>Quantity: ${item.Quantity}</p>
            <hr>
        `;
        cartItemsContainer.appendChild(itemDiv);
    });
}

// Function to place an order
async function placeOrder() {
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;

    if (!address || !phone || !email) {
        alert('Please fill in all fields.');
        return;
    }

    const order = {
        OrderID: Date.now().toString(), // Unique Order ID
        Items: cartItems,
        Address: address,
        Phone: phone,
        Email: email,
        PaymentMethod: 'Cash on Delivery',
        OrderStatus: 'Pending'
    };

    // Save order in DynamoDB using AWS SDK
    await saveOrderToDynamoDB(order);

    // Clear the cart
    localStorage.removeItem('cart');
    alert('Order placed successfully!');

    // Redirect to a confirmation or home page
    window.location.href = 'index.html';
}

// Function to save order to DynamoDB
async function saveOrderToDynamoDB(order) {
    // Initialize the Amazon Cognito credentials provider
    AWS.config.region = 'us-east-1'; // Region
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
        IdentityPoolId: 'us-east-1:faed0ece-35f1-4c37-9722-9c4bfbe10707', // Replace with your Identity Pool ID
    });

    const docClient = new AWS.DynamoDB.DocumentClient();

    const params = {
        TableName: 'Order.html', // Replace with your Orders table name
        Item: order
    };

    try {
        await docClient.put(params).promise();
        console.log('Order saved:', order);
    } catch (err) {
        console.error('Error saving order:', err);
    }
}

// Display the cart items on page load
displayCartItems();
