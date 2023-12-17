interface PersonalData {
	firstName: string
	lastName: string
	phoneNumber: string
};

interface Address {
	buildingAddress: string
	streetName: string
	landmark: string
	city: string
	district: string
	state: string
};

export default interface User {
	email?: string
	personalData?: PersonalData
	address?: Address
}