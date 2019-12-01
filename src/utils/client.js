import axios from "axios"

const API_BASE = "http://localhost:5000/api"

export const APIClient = axios.create({
  baseURL: API_BASE,
  timeout: 5000,
  withCredentials: true
})
