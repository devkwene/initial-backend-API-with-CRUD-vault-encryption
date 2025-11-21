import { useState } from "react";
import API from "../api/api";

export default function Register() {
  const [email, setEmail] = useState("");
  const [masterPassword, setMasterPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    try {
      const res = await API.post("/auth/register", {
        email,
        password: masterPassword,
      });
      setMessage("Registration successful! You can now log in.");
    } catch (err) {
      setMessage("Registration failed.");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Create Master Account</h2>

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

      <button onClick={handleRegister}>Register</button>

      <p>{message}</p>
    </div>
  );
}
