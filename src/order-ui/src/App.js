import React, { useState, useEffect } from "react";
import { fetchData, fetchResourceData, postData } from "./Api";
import "./App.css";

function App() {
  const [orders, setOrders] = useState([]);
  const [newOrder, setNewOrder] = useState({
    customer: "",
    size: "",
    amount: "",
  });
  const [validationError, setValidationError] = useState({});
  const [logs, setLogs] = useState([]);
  const [resources, setResources] = useState([]);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8765");
    socket.binaryType = 'arraybuffer';
  
    socket.addEventListener("open", () => {
      console.log("WebSocket connection opened");
    });
  
    socket.addEventListener("message", (message) => {
      const receivedData = message.data;
      const textDecoder = new TextDecoder('utf-8');
      const resultStr = textDecoder.decode(receivedData);
      const parsedData = JSON.parse(resultStr);
      setLogs((prevLogs) => [...prevLogs, parsedData]);
    })
  
    return () => {
      socket.close();
    };
  
  }, [setLogs]);

  useEffect(() => {
    fetchData()
      .then((result) => {
        setOrders(result);
      })
      .catch((error) => {
        console.error("Error fetching orders:", error);
      });

    fetchResourceData()
      .then((result) => {
        setResources(result);
      })
      .catch((error) => {
        console.error("Error fetching resources:", error);
      });

  }, []);

  const handleInputChange = (e) => {
    setNewOrder({ ...newOrder, [e.target.name]: e.target.value });
    setValidationError({});
  };

  const handleDropdownChange = (selectedSize) => {
    setNewOrder({ ...newOrder, size: selectedSize });
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
        setNewOrder({ customer: "", size: "", amount: "" });
        setValidationError({});
      })
      .catch((error) => {
        console.error("Error posting order:", error);
      });
  };

  return (
    <div className="app-container">
    <div className="order-form-container">
    <h1>New Order</h1>
      <form onSubmit={handleSubmit} className="order-form">
        <div className="form-group">
          <label htmlFor="customer" className="form-label">Customer:</label>
          <input
            type="text"
            id="customer"
            name="customer"
            value={newOrder.customer}
            onChange={handleInputChange}
            className={`form-input ${validationError.customer ? "error" : ""}`}
          />
        </div>
        <div className="form-group">
            <label htmlFor="size" className="form-label">Size:</label>
              <select
                id="size"
                name="size"
                value={newOrder.size}
                onChange={(e) => handleDropdownChange(e.target.value)}
                className={`form-input dropdown ${validationError.size ? "error" : ""}`}
              >
                <option value="" disabled>Select Size</option>
                {resources.map((resource) => (
                  <option key={resource.id} value={resource.size}>
                    {resource.size}  (Left: {resource.amount})
                  </option>
                ))}
              </select>
            </div>
        <div className="form-group">
          <label htmlFor="amount" className="form-label">Amount:</label>
          <input
            type="text"
            id="amount"
            name="amount"
            value={newOrder.amount}
            onChange={handleInputChange}
            className={`form-input ${validationError.amount ? "error" : ""}`}
          />
        </div>
        {Object.values(validationError).some((error) => error) && (
          <p className="error-message">All fields are mandatory</p>
        )}
        <button type="submit" className="submit-button">
          Place Order
        </button>
      </form>    </div>
      <div className="logs-container">
        <h1>Orders</h1>
        <table className="logs-table">
          <thead>
            <tr>
              <th>OrderId</th>
              <th>Customer</th>
              <th>Size</th>
              <th>Amount</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((order, index) => (
              <tr key={index}>
                <td>{order.id}</td>
                <td>{order.customer}</td>
                <td>{order.size}</td>
                <td>{order.amount}</td>
                <td>{order.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    <div className="log-container">
      <h1>Orders Progress</h1>
      <table className="log-table">
        <thead>
          <tr>
            <th>OrderId</th>
            <th>Timestamp</th>
            <th>Process</th>
            <th>System</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{log.orderId}</td>
              <td>{log.timestamp}</td>
              <td>{log.process}</td>
              <td>{log.system}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
  );
}

export default App;
