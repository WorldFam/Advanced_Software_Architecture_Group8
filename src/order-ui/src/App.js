import React, { useState, useEffect } from 'react';
import { fetchData, postData } from './Api';
import './App.css';

function App() {
    const [orders, setOrders] = useState([]);
    const [newOrder, setNewOrder] = useState({ customer: '', size: '', amount: '' });
    const [validationError, setValidationError] = useState({});

    useEffect(() => {
        fetchData()
            .then((result) => {
                setOrders(result);
            })
            .catch((error) => {
                console.error('Error fetching orders:', error);
            });
    }, []);

    const handleInputChange = (e) => {
        setNewOrder({ ...newOrder, [e.target.name]: e.target.value });
        setValidationError({});
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!newOrder.customer || !newOrder.size || !newOrder.amount) {
            setValidationError({
                customer: !newOrder.customer,
                size: !newOrder.size,
                amount: !newOrder.amount,
            });
            return;
        }

        postData(newOrder)
            .then(() => fetchData())
            .then((result) => {
                setOrders(result);
                setNewOrder({ customer: '', size: '', amount: '' });
                setValidationError({});
            })
            .catch((error) => {
                console.error('Error posting order:', error);
            });
    };

    return (
        <div className="order-form-container">
            <h1>New Order</h1>
            <ul className="order-list">
                {orders.map((order, index) => (
                    <li key={index}>{`${order.customer} - Size: ${order.size}, Amount: ${order.amount}`}</li>
                ))}
            </ul>
            <form onSubmit={handleSubmit} className="order-form">
                <div className="form-group">
                    <label htmlFor="customer">Customer:</label>
                    <input
                        type="text"
                        id="customer"
                        name="customer"
                        value={newOrder.customer}
                        onChange={handleInputChange}
                        className={`form-input ${validationError.customer ? 'error' : ''}`}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="size">Size:</label>
                    <input
                        type="text"
                        id="size"
                        name="size"
                        value={newOrder.size}
                        onChange={handleInputChange}
                        className={`form-input ${validationError.size ? 'error' : ''}`}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="amount">Amount:</label>
                    <input
                        type="text"
                        id="amount"
                        name="amount"
                        value={newOrder.amount}
                        onChange={handleInputChange}
                        className={`form-input ${validationError.amount ? 'error' : ''}`}
                    />
                </div>
                {Object.values(validationError).some((error) => error) && (
                    <p className="error-message">All fields are mandatory</p>
                )}
                <button type="submit" className="submit-button">
                    Place Order
                </button>
            </form>
        </div>
    );
}

export default App;
