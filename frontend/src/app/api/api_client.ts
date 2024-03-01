import assert from 'assert';
import axios from 'axios';

assert(process.env.API_PORT);

export const apiClient = axios.create({
  baseURL: `http://localhost:${process.env.API_PORT}`,
});
