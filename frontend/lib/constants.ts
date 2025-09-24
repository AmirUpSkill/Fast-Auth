export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// ---  Auth URLs from API contract ---
export const GOOGLE_AUTH_LOGIN_URL = `${API_BASE_URL}/api/v1/auth/google/login`;
export const GOOGLE_AUTH_CALLBACK_URL = `${API_BASE_URL}/api/v1/auth/google/callback`;
export const USERS_ME_URL = `${API_BASE_URL}/api/v1/users/me`;
export const LOGOUT_URL = `${API_BASE_URL}/api/v1/auth/logout`;

// ---  App constants --- 
export const APP_NAME = 'Fast Auth';
export const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';