import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Client = () => {
  const [clients, setClients] = useState([]);

  // Fetch client data from FastAPI server
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/clients')  // Adjust based on your FastAPI endpoint
      .then((response) => {
        setClients(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the client data!", error);
      });
  }, []);

  return (
    <div>
      <h1>Clients</h1>
      <ul>
        {clients.map((client, index) => (
          <li key={index}>
            <h2>{client.name}</h2>
            <p>Email: {client.email}</p>
            <p>Phone: {client.cellphone}</p>
            <p>Purchases: {client.purchases.length}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Client;
