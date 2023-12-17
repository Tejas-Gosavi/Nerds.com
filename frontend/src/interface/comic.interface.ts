interface Brand {
    id?: number,
    brand_title?: string,
    brand_slug?: string,
    brand_to_feature?: boolean,
    brand_is_active?: boolean
}

interface comicType {
    id?: number,
    comic_type_title?: string,
    comic_type_slug?: string,
    comic_type_to_feature?: boolean,
    comic_type_is_active?: boolean
}
interface Comic {
    id?: number,
    brand?: Brand,
    comic_type?: comicType,
    volume?: null | any,
    title?: string,
    slug?: string,
    main_image?: string,
    other_image1?: string,
    other_image2?: string,
    detail?: string,
    price?: number,
    published_date?: string,
    page_count?: number,
    age_rating?: string,
    in_stock?: boolean,
    is_active?: boolean,
    created_at?: string,
    updated_at?: string
}

export type { Brand, comicType, Comic };