// OrderForm.js
import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
  const [order, setOrder] = useState({
    customer: '',
    size: '',
    amount: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setOrder({ ...order, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8090/api/order', order);
      console.log('Order submitted successfully!');
    } catch (error) {
      console.error('Error submitting order:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Customer:
        <input type="text" name="customer" value={order.customer} onChange={handleChange} />
      </label>
      <br />
      <label>
        Size:
        <input type="text" name="size" value={order.size} onChange={handleChange} />
      </label>
      <br />
      <label>
        Amount:
        <input type="text" name="amount" value={order.amount} onChange={handleChange} />
      </label>
      <br />
      <button type="submit">Submit Order</button>
    </form>
  );
};

export default OrderForm;
