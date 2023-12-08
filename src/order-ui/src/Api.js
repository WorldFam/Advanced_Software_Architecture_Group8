const ORDER_BASE_URL = 'http://localhost:8090';

export const fetchData = async () => {
    const response = await fetch(`${ORDER_BASE_URL}/api/order`);
    const data = await response.json();
    return data;
};

export const postData = async (newForecast) => {
    const response = await fetch(`${ORDER_BASE_URL}/api/order`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newForecast),
    });

    if (!response.ok) {
        throw new Error(`Failed to add order: ${response.status}`);
    }
};

const SUPPLY_BASE_URL = 'http://localhost:9093';

export const fetchResourceData = async () => {
    const response = await fetch(`${SUPPLY_BASE_URL}/resource`, {
        method: 'GET',
        credentials: 'include',
    });
    const data = await response.json();
    return data;
};