import { useEffect, useState } from "react";
import API from "../api/api";

export default function Dashboard() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    API.get("/vault/items")
      .then(res => {
        setItems(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Your Vault</h1>

      {items.length === 0 ? (
        <p>No items yet. Add one!</p>
      ) : (
        <ul>
          {items.map((i) => (
            <li key={i.id}>
              <strong>{i.site_name}</strong> — {i.username}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
