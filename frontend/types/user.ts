// types/user.ts

export type User = {
  id: string;
  email: string;
  name: string;
  avatar_url: string | null;
  created_at: string; // ISO 8601 datetime string
};

// For forms/input validation
export type UserCreate = {
  email: string;
  name: string;
  avatar_url?: string | null;
};

// For updating user data
export type UserUpdate = {
  name?: string;
  avatar_url?: string | null;
};

// Auth-related user state
export type AuthUser = User | null;

// For authentication status
export type AuthState = {
  user: AuthUser;
  isLoading: boolean;
  error: string | null;
};