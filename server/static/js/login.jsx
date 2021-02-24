'use strict';
function Login() {

	// function will go here
	return (
		<div>
			<h1>Log In</h1>
			<Form.Group controlId="formBasicEmail">
				<Form.Label>Email address</Form.Label>
				<Form.Control type="email" placeholder="Enter email" onChange={handleChange} />
				<Form.Text className="text-muted">
				We'll never share your email with anyone else.
				</Form.Text>
			</Form.Group>

			<Form.Group controlId="formBasicPassword">
				<Form.Label>Password</Form.Label>
				<Form.Control type="password" placeholder="Password" onChange={handleChange}/>
			</Form.Group>

			<Button variant="primary">Log In</Button>
			
			<h5>New user? <Button href="/register" variant="primary">Register here!</Button></h5>
		</div>
	)
}
// set states

const loginForm = (props) => {
	const [login, setLogin] = React.setLogin({
		login: true,
		email: "",
		password: ""
	});
}

console.log(loginForm)

// handle the updating of rthe state as a user fills out the registraton form 
const handleChange = (e) => {
// e is for event 
	let change = {};	
	change[e.target] = e.target.value
	console.log(change)
	this.setState(change)
	// what is e.target?
	// does the handle change need to have the prevent default?
	
	// in heathers, what is "..." before the prevState
} 
// have  a function that handles the changes
// go to server py and do something (Don't know what yet)

// step 1-- states **
// step 2 -- handle change (login or registration)
// step 3 -- make a method to handle login and then go to server.py and create a route
		// that handles the login 

const handleLogin = (e) => {
	e.preventDefault();
	if(state.email.length && state.password.length) {
		const payload = {'email': state.email, 'password': state.password};
		fetch('/user_login', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(payload)
		})
	}
}
// step 4 -- crud functions that are called inside of the route above 
	// handles getting user by email to check if its a valid email 
	// OR handles register and saving a user to the DB if they are new
// step 5 -- go back to JS and work with the .then, JSOn response, localStorage (session)
// onChange-- don't forget to add the functions to the on change




// class Login extends React.Component  {
// 	constructor(props) {
// 		super(props);
// 	}
// 	render(){
// 		return (
// 			<div>
// 				<h1>Log In</h1>
// 				<Form.Group controlId="formBasicEmail">
// 					<Form.Label>Email address</Form.Label>
// 					<Form.Control type="email" placeholder="Enter email" />
// 					<Form.Text className="text-muted">
// 					We'll never share your email with anyone else.
// 					</Form.Text>
// 				</Form.Group>
	
// 				<Form.Group controlId="formBasicPassword">
// 					<Form.Label>Password</Form.Label>
// 					<Form.Control type="password" placeholder="Password" />
// 				</Form.Group>
	
// 				<Button variant="primary">Log In</Button>
				
// 			</div>
// 		)
// 	}


// 	// function will go here
	
// }


// ReactDOM.render(<Map />, document.getElementById('map'));

