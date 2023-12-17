import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
import type { Brand, comicType, Comic } from '@/interface/comic.interface';

export const useComicStore = defineStore('comics', () => {
	const s3Bucket: string = "https://nerds.s3.ap-south-1.amazonaws.com";
	const tempBrand: Brand[] = [];
	const tempComicTypes: comicType[] = [];
	const tempComics: Comic[] = [];
	const brands = useStorage('brands', tempBrand);
	const comicTypes = useStorage('comicTypes', tempComicTypes);
	const comics = useStorage('comics', tempComics);

	const getBrands = () => {
		return brands.value;
	}

	const getComicTypes = () => {
		return comicTypes.value;
	}

	const setBrands = (b: any) => {
		brands.value = b;
	}

	const setComicTypes = (ct: any) => {
		comicTypes.value = ct;
	}

	const setComics = (cs: any[]) => {
		cs.forEach((c) => {
			const b = brands.value.find(b => b.id == c.brand_id);
			if(b) c.brand = b;

			const ct = comicTypes.value.find(ct => ct.id == c.comic_type_id);
			if(ct) c.comic_type = ct; 
		})
		comics.value = cs;
	}

	const getComics = () => {
		return comics.value;
	}

	return { s3Bucket, getBrands, getComicTypes, setBrands, setComicTypes, setComics, getComics };
})

