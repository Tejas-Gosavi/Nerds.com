import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
import type User from '@/interface/user.interface';

export const useUserStore = defineStore('users', () => {
	const url: string = "http://127.0.0.1:8000";
	const tempUser: User = {};
	const login = useStorage('login', false);
	const user = useStorage('user', tempUser);
	
	const isUserLoggedIn = () => {
		return login.value;
	}
	const setUser = (l: any, u: any) => {
		login.value = l;
		user.value = { ...u };
		window.location.reload();
	}
	const getUser = () => {
		return user.value.email;
	}
	const getPersonalData = () => {
		return user.value.personalData;
	}
	const setPersonalData = (data: any) => {
		user.value.personalData = data;
	}
	const getAddress = () => {
		return user.value.address;
	}
	const setAddress = (data: any) => {
		user.value.address = data;
	}
	return { url, isUserLoggedIn, setUser, getUser, 
			getPersonalData, setPersonalData, 
			getAddress, setAddress };
})

