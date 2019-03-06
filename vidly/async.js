console.log('Before');
getUser(11).then( (user) => {
	console.log(user);
	getCourses(user).then((courses) => {
		console.log(courses);
	})
});
console.log('After');

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



