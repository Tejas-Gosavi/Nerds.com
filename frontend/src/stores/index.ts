import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
import type User from './user.interface';

export const useNerdsStore = defineStore('nerds', () => {
	const url: string = "http://127.0.0.1:8000";
	const temp: User = {};
	const login = useStorage('login', false);
	const user = useStorage('user', temp);
	const brands = useStorage('brands', {});
	const types = useStorage('types', {});
	
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

