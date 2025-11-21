import { useState } from "react";
import API from "../api/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [masterPassword, setMasterPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async () => {
    try {
      const res = await API.post("/auth/login", {
        email,
        password: masterPassword,
      });

      localStorage.setItem("token", res.data.access_token);
      setMessage("Login successful!");
    } catch (err) {
      setMessage("Invalid login credentials.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Login</h2>

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ display: "block", margin: "10px 0" }}
      />

      <input
        type="password"
        placeholder="Master Password"
        value={masterPassword}
        onChange={(e) => setMasterPassword(e.target.value)}
        style={{ display: "block", margin: "10px 0" }}
      />

      <button onClick={handleLogin}>Login</button>

      <p>{message}</p>
    </div>
  );
}
