import type { User } from './user';

export type ApiResponse<T> = {
    data: T;
}

export type ApiError = {
    detail: string;
}
export type UserResponse = ApiResponse<User>;

export type LogoutResponse = {
    message: string;
}