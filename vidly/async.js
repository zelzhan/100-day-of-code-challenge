/* ASYNCHROUNOUS JAVASCRIPT PRACTICE */
console.log('Before');
// Async with promises
getUser(11)
	.then( (user) => {
		console.log(user);
		return getCourses(user)
	})
	.then((courses) => {
		logCourses(courses);
	})
console.log('After');



// Async with async/await function
setTimeout(() => {
	getEverything(100);
	}, 3000);

async function getEverything(id){
	let user = await getUser(id);
	console.log(user);
	let courses = await getCourses(user);
	logCourses(courses);	
}

function getUser(id) {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			console.log('Imitation of request to the database...')
			resolve({id: id, name: "Elzhan"});
		}, 1000)		
	})	
}

function getCourses(user){
	console.log('Calling the registrar API...')
	return new Promise((resolve, reject) => {
		setTimeout(() => {
		resolve(['course1', 'course2', 'course3']);	
		}, 1500)	
	})
}

function logUser(user){
	console.log(user);
	getCourses(user, logCourses)
}

function logCourses(courses){
	console.log(courses);
}